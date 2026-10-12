# Polars

!!! learn "On this page we will learn"
    - the Polars methods and expressions used in this course
    - where each one is explained
    - how to load JSON files, so we can use more datasets in our project

!!! terms "Terminology"
    - **JSON** – a text format for sharing data, which stores each record between `{ }` and each list between `[ ]`.
    - **struct** – a Polars column type where each value is a small record holding several named values.
    - **list column** – a Polars column where each value is a list of items, like the types of a Pokémon.

**Polars** is a Python library for working with tables of data. We import it with `import polars as pl`. This course uses **Polars 2.0**.

Most examples on this page use `games`, a DataFrame of Steam games, and each row links to the lesson where it's explained in full. The JSON examples use small files about D&D monsters and Pokémon.

## Key ideas

| Term | Meaning | Where we learned it |
| :-- | :-- | :-- |
| DataFrame | a table of data with rows and columns | [Exploring Our Data](../hook/02_exploring_data.md#load-the-data) |
| Series | a single column, like `games["Price"]` | [Asking a Question Data Can Answer](../hook/03_asking_questions.md#counting-values) |
| expression | a description of what to do with a column, like `pl.col("Price") > 0`, that Polars works out for every row at once | [Choosing Columns and Rows](../cleaning/05_select_filter.md#choosing-rows) |
| data type | the kind of values a column holds, like `Int64`, `Float64`, `String` or `Date` | [Exploring Our Data](../hook/02_exploring_data.md#what-kind-of-data-is-in-each-column) |
| null | no value: the value is missing | [Data, Privacy and Ethics](../hook/04_privacy_ethics.md#finding-personal-information-in-our-data) |

## Loading and saving

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `pl.read_csv("data/steam_games.csv")` | loads a CSV file | [Exploring Our Data](../hook/02_exploring_data.md#load-the-data) |
| `games.write_parquet("data/clean_games.parquet")` | saves a Parquet file | [Fixing Our Data](../cleaning/06_fixing_data.md#saving-our-clean-data) |
| `pl.read_parquet("data/clean_games.parquet")` | loads a Parquet file | [Making New Columns](../insights/07_new_columns.md#a-new-notebook) |
| `pl.read_json("data/monsters.json")` | loads a JSON file that holds a list of records | [Loading JSON files](#loading-json-files) |
| `pl.read_ndjson("data/monsters.ndjson")` | loads a JSON file that has one record on each line | [Loading JSON files](#loading-json-files) |
| `pl.read_parquet(mo.notebook_dir() / "data" / "clean_games.parquet")` | loads a file from the ***data*** folder next to our notebook, so it also works on the class server | [Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server) |

## Loading JSON files

Lots of datasets, especially ones that come from websites and games, are shared as **JSON** files instead of CSV files. JSON stores data as text, using `{ }` around each record and `[ ]` around lists. Polars can load JSON too, so we're not stuck if the dataset we want for our project isn't a CSV.

### Look at the file first

Before we load a JSON file, open it in VS Code and look at its first character. That tells us which shape it is, and which code to use:

| The file looks like | Shape | Code |
| :-- | :-- | :-- |
| `[{"name": "Goblin", …}, {"name": "Owlbear", …}]` | a list of records, one for each row | `pl.read_json("data/monsters.json")` |
| one `{ … }` record on each line, often in a file ending in ***.ndjson*** or ***.jsonl*** | one record per line | `pl.read_ndjson("data/monsters.ndjson")` |
| `{"count": 2, "results": [{ … }, { … }]}` | the records are inside another record | `pl.read_json(…)`, then `explode` and `unnest`, as shown below |

!!! tip "Big JSON files"
    A large JSON file can be too big to open comfortably in VS Code. If it's slow, look at it in a web browser instead: drag the file into a Chrome or Firefox tab, and tick **Pretty-print** if it's offered, to see its structure laid out neatly.

### A list of records

This is the most common shape, and it loads just like a CSV file. Each record becomes a row, and each name in the record becomes a column.

```python title="clean_monsters.py"
monsters = pl.read_json("data/monsters.json")
monsters
```

### Records inside another record

Data from a website often wraps the records inside another record, with the list under a name like `results` or `data`. Polars loads this as **one** row, with all the records squashed into one column. To turn it into a proper table, we keep only that column, give each record its own row with `explode`, then spread its values into columns with `unnest`.

```python title="clean_pokemon.py"
pokemon = (
    pl.read_json("data/pokemon.json")
    .select("results")
    .explode("results")
    .unnest("results")
)
pokemon
```

### Values inside values

A JSON record can hold a smaller record, or a list, as one of its values. Polars keeps these in special column types:

- a smaller record, like `"speed": {"walk": 30, "fly": 80}`, becomes a **struct** column, which shows values like `{30,80}`
- a list, like `"types": ["fire", "flying"]`, becomes a **list** column, which shows values like `["fire", "flying"]`

Things like `group_by` and charts work best with ordinary columns, so we usually turn these into ordinary columns first:

| Code | What it does |
| :-- | :-- |
| `monsters.unnest("speed")` | spreads every value in the `speed` struct into its own column, called `walk` and `fly` |
| `pl.col("speed").struct.field("walk").alias("Walk speed")` | takes one value out of a struct, as a new column |
| `pl.col("types").list.len().alias("Number of types")` | counts the items in each list |
| `pl.col("types").list.join(", ")` | joins the items in each list into one piece of text, like `fire, flying`, so we can use `str.contains` |
| `pokemon.explode("types")` | gives every item in the list its own row, copying the rest of the row. Charizard becomes two rows: one `fire`, one `flying` |

The last three go inside `with_columns`, just like the expressions in [Making New Columns](../insights/07_new_columns.md).

!!! warning "Watch out for repeated names"
    If a struct has a value with the same name as a column we already have, like a `name` inside a `stats` struct, `unnest` stops with a `DuplicateError`. Use `struct.field` to take out only the values we need, and give each one a new name with `alias`.

!!! warning "Explode changes what a row means"
    After `explode`, one row is no longer one Pokémon: Charizard is counted twice. That's what we want when we're counting how many Pokémon have each type, but not when we're counting Pokémon. Write down what one row represents before and after, just like we did for the Steam data.

## Looking at data

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `games.shape` | the number of rows and columns | [Exploring Our Data](../hook/02_exploring_data.md#how-big-is-our-data) |
| `games.schema` | the name and data type of each column | [Exploring Our Data](../hook/02_exploring_data.md#what-kind-of-data-is-in-each-column) |
| `games.head(5)` | the first 5 rows | [Exploring Our Data](../hook/02_exploring_data.md#reactive-cells) |
| `games.describe()` | summary statistics for every column | [Asking a Question Data Can Answer](../hook/03_asking_questions.md#summary-statistics) |
| `games["Metacritic score"].value_counts(sort=True)` | how often each value appears, most common first | [Asking a Question Data Can Answer](../hook/03_asking_questions.md#counting-values) |
| `games["Support email"].null_count()` | the number of nulls in a column | [Data, Privacy and Ethics](../hook/04_privacy_ethics.md#finding-personal-information-in-our-data) |
| `games.null_count()` | the number of nulls in every column | [Fixing Our Data](../cleaning/06_fixing_data.md#values-that-mean-missing) |
| `games.height` | the number of rows | [Choosing Columns and Rows](../cleaning/05_select_filter.md#choosing-rows) |
| `games["Release date"].min()` and `.max()` | the smallest and largest values in a column | [Fixing Our Data](../cleaning/06_fixing_data.md#text-into-dates) |

## Choosing columns and rows

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `games.drop("Support email")` | removes a column | [Data, Privacy and Ethics](../hook/04_privacy_ethics.md#removing-columns-we-dont-need) |
| `games.select("Name", "Price")` | keeps only these columns | [Choosing Columns and Rows](../cleaning/05_select_filter.md#choosing-columns) |
| `games.filter(pl.col("Price") > 0)` | keeps only the rows where the condition is true | [Choosing Columns and Rows](../cleaning/05_select_filter.md#choosing-rows) |
| `(condition_1) & (condition_2)` | and: both conditions must be true | [Choosing Columns and Rows](../cleaning/05_select_filter.md#combining-conditions) |
| `(condition_1) | (condition_2)` | or: at least one condition must be true | [Choosing Columns and Rows](../cleaning/05_select_filter.md#combining-conditions) |
| `pl.col("Release year").is_between(2010, 2024)` | true if the value is between the two numbers, including both | [Trends and Relationships](../insights/11_trends_relationships.md#summarising-by-two-columns) |
| `games.sort("Name")` | sorts the rows | [Fixing Our Data](../cleaning/06_fixing_data.md#repeated-names) |
| `games.sort("Price", descending=True)` | sorts the rows from biggest to smallest | [Outliers and Predictions](../insights/12_outliers_predictions.md#checking-the-outliers) |

## Making and changing columns

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `games.with_columns(expression, …)` | adds or replaces columns | [Fixing Our Data](../cleaning/06_fixing_data.md#text-into-dates) |
| `.alias("Review score")` | names the column an expression makes | [Making New Columns](../insights/07_new_columns.md#calculating-a-review-score) |
| `pl.col("Positive") / pl.col("Negative")` | does maths with columns, row by row | [Making New Columns](../insights/07_new_columns.md#calculating-a-review-score) |
| `.round(1)` | rounds to 1 decimal place | [Making New Columns](../insights/07_new_columns.md#calculating-a-review-score) |
| `pl.when(…).then(…).otherwise(…)` | chooses a value for each row, like `if` and `else` | [Making New Columns](../insights/07_new_columns.md#years-and-groups) |
| `pl.lit("Indie")` | the same value in every row | [Making New Columns](../insights/07_new_columns.md#years-and-groups) |

## Text and dates

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `pl.col("Genres").str.contains("Indie")` | true if the text contains this | [Asking a Question Data Can Answer](../hook/03_asking_questions.md#defining-our-terms) |
| `pl.col("Release date").str.to_date("%b %d, %Y")` | turns text into dates, using a format code | [Fixing Our Data](../cleaning/06_fixing_data.md#text-into-dates) |
| `pl.col("Release date").dt.year()` | the year of each date | [Making New Columns](../insights/07_new_columns.md#years-and-groups) |

Date format codes:

| Code | Meaning | Example |
| :-- | :-- | :-- |
| `%Y` | four-digit year | `2017` |
| `%m` | month number | `02` |
| `%b` | short month name | `Feb` |
| `%B` | full month name | `February` |
| `%d` | day of the month | `24` |

## Missing and repeated values

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `pl.col("Metacritic score").replace(0, None)` | turns every 0 into a null | [Fixing Our Data](../cleaning/06_fixing_data.md#values-that-mean-missing) |
| `pl.col("Name").is_duplicated()` | true if the value appears more than once | [Fixing Our Data](../cleaning/06_fixing_data.md#repeated-names) |
| `games["AppID"].is_unique().all()` | true if every value is different | [Fixing Our Data](../cleaning/06_fixing_data.md#repeated-names) |

## Summarising

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `games["Genres"].str.contains("Indie").sum()` | counts the `True` values | [Asking a Question Data Can Answer](../hook/03_asking_questions.md#defining-our-terms) |
| `games.group_by("Group").agg(…)` | splits the rows into groups and summarises each one | [Summarising Groups](../insights/08_summarising_groups.md#comparing-our-two-groups) |
| `games.group_by("Release year", "Group").agg(…)` | groups by two columns at once | [Trends and Relationships](../insights/11_trends_relationships.md#summarising-by-two-columns) |
| `pl.len()` | the number of rows | [Summarising Groups](../insights/08_summarising_groups.md#comparing-our-two-groups) |
| `.mean()`, `.median()`, `.min()`, `.max()`, `.sum()` | summarises a column | [Summarising Groups](../insights/08_summarising_groups.md#mean-or-median) |
| `games["Price"].quantile(0.25)` | the value a quarter of the way through, when the values are sorted | [Outliers and Predictions](../insights/12_outliers_predictions.md#quartiles) |
| `per_year["Games"].diff()` | the change from the row before | [Outliers and Predictions](../insights/12_outliers_predictions.md#making-a-prediction) |
| `per_group["Median review score"][0]` | the first value in a column | [Publishing Our Data Story](../resolution/15_publishing.md#putting-numbers-in-our-text) |
| `recent["Games"][-1]` | the last value in a column | [Outliers and Predictions](../insights/12_outliers_predictions.md#making-a-prediction) |

!!! warning "Give every summary its own name"
    Inside `agg`, two summaries of the same column need different names. Without `alias`, `pl.col("Price").median()` and `pl.col("Price").mean()` would both be called `Price`, and Polars stops with a `DuplicateError`. See [Common Errors](common_errors.md#duplicateerror).

!!! tip "The official documentation"
    The [Polars user guide](https://docs.pola.rs/){ target="_blank" rel="noopener" } explains every method in detail, with examples.
