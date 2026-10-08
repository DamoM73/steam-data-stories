# Polars

!!! learn "On this page we will learn"
    - the Polars methods and expressions used in this course
    - where each one is explained

**Polars** is a Python library for working with tables of data. We import it with `import polars as pl`. This course uses **Polars 2.0**.

The examples on this page use `games`, a DataFrame of Steam games. Each row links to the lesson where it's explained in full.

## Key ideas

| Term | Meaning | Lesson |
| :-- | :-- | :-- |
| DataFrame | a table of data with rows and columns | [2](../hook/02_exploring_data.md#load-the-data) |
| Series | a single column, like `games["Price"]` | [3](../hook/03_asking_questions.md#counting-values) |
| expression | a description of what to do with a column, like `pl.col("Price") > 0`, that Polars works out for every row at once | [5](../cleaning/05_select_filter.md#choosing-rows) |
| data type | the kind of values a column holds, like `Int64`, `Float64`, `String` or `Date` | [2](../hook/02_exploring_data.md#what-kind-of-data-is-in-each-column) |
| null | no value: the value is missing | [4](../hook/04_privacy_ethics.md#finding-personal-information-in-our-data) |

## Loading and saving

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.read_csv("data/steam_games.csv")` | loads a CSV file | [2](../hook/02_exploring_data.md#load-the-data) |
| `games.write_parquet("data/clean_games.parquet")` | saves a Parquet file | [6](../cleaning/06_fixing_data.md#saving-our-clean-data) |
| `pl.read_parquet("data/clean_games.parquet")` | loads a Parquet file | [7](../insights/07_new_columns.md#a-new-notebook) |
| `pl.read_parquet(mo.notebook_dir() / "data" / "clean_games.parquet")` | loads a file from the ***data*** folder next to our notebook, so it also works on the class server | [15](../resolution/15_publishing.md#getting-ready-for-the-class-server) |

## Looking at data

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.shape` | the number of rows and columns | [2](../hook/02_exploring_data.md#how-big-is-our-data) |
| `games.schema` | the name and data type of each column | [2](../hook/02_exploring_data.md#what-kind-of-data-is-in-each-column) |
| `games.head(5)` | the first 5 rows | [2](../hook/02_exploring_data.md#reactive-cells) |
| `games.describe()` | summary statistics for every column | [3](../hook/03_asking_questions.md#summary-statistics) |
| `games["Metacritic score"].value_counts(sort=True)` | how often each value appears, most common first | [3](../hook/03_asking_questions.md#counting-values) |
| `games["Support email"].null_count()` | the number of nulls in a column | [4](../hook/04_privacy_ethics.md#finding-personal-information-in-our-data) |
| `games.null_count()` | the number of nulls in every column | [6](../cleaning/06_fixing_data.md#values-that-mean-missing) |
| `games.height` | the number of rows | [5](../cleaning/05_select_filter.md#choosing-rows) |
| `games["Release date"].min()` and `.max()` | the smallest and largest values in a column | [6](../cleaning/06_fixing_data.md#text-into-dates) |

## Choosing columns and rows

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.drop("Support email")` | removes a column | [4](../hook/04_privacy_ethics.md#removing-columns-we-dont-need) |
| `games.select("Name", "Price")` | keeps only these columns | [5](../cleaning/05_select_filter.md#choosing-columns) |
| `games.filter(pl.col("Price") > 0)` | keeps only the rows where the condition is true | [5](../cleaning/05_select_filter.md#choosing-rows) |
| `(condition_1) & (condition_2)` | and: both conditions must be true | [5](../cleaning/05_select_filter.md#combining-conditions) |
| `(condition_1) | (condition_2)` | or: at least one condition must be true | [5](../cleaning/05_select_filter.md#combining-conditions) |
| `pl.col("Release year").is_between(2010, 2024)` | true if the value is between the two numbers, including both | [11](../insights/11_trends_relationships.md#summarising-by-two-columns) |
| `games.sort("Name")` | sorts the rows | [6](../cleaning/06_fixing_data.md#repeated-names) |

## Making and changing columns

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.with_columns(expression, …)` | adds or replaces columns | [6](../cleaning/06_fixing_data.md#text-into-dates) |
| `.alias("Review score")` | names the column an expression makes | [7](../insights/07_new_columns.md#calculating-a-review-score) |
| `pl.col("Positive") / pl.col("Negative")` | does maths with columns, row by row | [7](../insights/07_new_columns.md#calculating-a-review-score) |
| `.round(1)` | rounds to 1 decimal place | [7](../insights/07_new_columns.md#calculating-a-review-score) |
| `pl.when(…).then(…).otherwise(…)` | chooses a value for each row, like `if` and `else` | [7](../insights/07_new_columns.md#years-and-groups) |
| `pl.lit("Indie")` | the same value in every row | [7](../insights/07_new_columns.md#years-and-groups) |

## Text and dates

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.col("Genres").str.contains("Indie")` | true if the text contains this | [3](../hook/03_asking_questions.md#defining-our-terms) |
| `pl.col("Release date").str.to_date("%b %d, %Y")` | turns text into dates, using a format code | [6](../cleaning/06_fixing_data.md#text-into-dates) |
| `pl.col("Release date").dt.year()` | the year of each date | [7](../insights/07_new_columns.md#years-and-groups) |

Date format codes:

| Code | Meaning | Example |
| :-- | :-- | :-- |
| `%Y` | four-digit year | `2017` |
| `%m` | month number | `02` |
| `%b` | short month name | `Feb` |
| `%B` | full month name | `February` |
| `%d` | day of the month | `24` |

## Missing and repeated values

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.col("Metacritic score").replace(0, None)` | turns every 0 into a null | [6](../cleaning/06_fixing_data.md#values-that-mean-missing) |
| `pl.col("Name").is_duplicated()` | true if the value appears more than once | [6](../cleaning/06_fixing_data.md#repeated-names) |
| `games["AppID"].is_unique().all()` | true if every value is different | [6](../cleaning/06_fixing_data.md#repeated-names) |

## Summarising

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games["Genres"].str.contains("Indie").sum()` | counts the `True` values | [3](../hook/03_asking_questions.md#defining-our-terms) |
| `games.group_by("Group").agg(…)` | splits the rows into groups and summarises each one | [8](../insights/08_summarising_groups.md#comparing-our-two-groups) |
| `games.group_by("Release year", "Group").agg(…)` | groups by two columns at once | [11](../insights/11_trends_relationships.md#summarising-by-two-columns) |
| `pl.len()` | the number of rows | [8](../insights/08_summarising_groups.md#comparing-our-two-groups) |
| `.mean()`, `.median()`, `.min()`, `.max()`, `.sum()` | summarises a column | [8](../insights/08_summarising_groups.md#mean-or-median) |
| `games["Price"].quantile(0.25)` | the value a quarter of the way through, when the values are sorted | [12](../insights/12_outliers_predictions.md#finding-outliers) |
| `per_year["Games"].diff()` | the change from the row before | [12](../insights/12_outliers_predictions.md#making-a-prediction) |
| `per_group["Median review score"][0]` | the first value in a column | [15](../resolution/15_publishing.md#putting-numbers-in-our-text) |
| `recent["Games"][-1]` | the last value in a column | [12](../insights/12_outliers_predictions.md#making-a-prediction) |

!!! warning "Give every summary its own name"
    Inside `agg`, two summaries of the same column need different names. Without `alias`, `pl.col("Price").median()` and `pl.col("Price").mean()` would both be called `Price`, and Polars stops with a `DuplicateError`. See [Common Errors](common_errors.md#duplicateerror).

!!! tip "The official documentation"
    The [Polars user guide](https://docs.pola.rs/){ target="_blank" rel="noopener" } explains every method in detail, with examples.
