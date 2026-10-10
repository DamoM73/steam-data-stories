# Polars

!!! learn "On this page we will learn"
    - the Polars methods and expressions used in this course
    - where each one is explained

**Polars** is a Python library for working with tables of data. We import it with `import polars as pl`. This course uses **Polars 2.0**.

The examples on this page use `games`, a DataFrame of Steam games. Each row links to the lesson where it's explained in full.

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
| `pl.read_parquet(mo.notebook_dir() / "data" / "clean_games.parquet")` | loads a file from the ***data*** folder next to our notebook, so it also works on the class server | [Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server) |

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
