# Polars

!!! learn "On this page we will learn"
    - the Polars methods and expressions used in this course
    - where each one is explained

**Polars** is a Python library for working with tables of data. We import it with `import polars as pl`. This course uses **Polars 2.0**.

The examples on this page use `games`, a DataFrame of Steam games. Each table links to the lesson where the method is explained in full.

## Key ideas

| Term | Meaning |
| :-- | :-- |
| **DataFrame** | a table of data with rows and columns |
| **Series** | a single column, like `games["Price"]` |
| **expression** | a description of what to do with a column, like `pl.col("Price") > 0`, that Polars works out for every row at once |
| **data type** | the kind of values a column holds, like `Int64`, `Float64`, `String`, `Boolean`, `Date` or `List(String)` |
| **null** | no value |
| **NaN** | "not a number": the result of a calculation with no answer, like 0 ÷ 0 |

## Loading and saving

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.read_csv("data/steam_games.csv")` | loads a CSV file | [2](../hook/02_exploring_data.md#load-the-data) |
| `pl.read_parquet("data/clean_games.parquet")` | loads a Parquet file | [9](../insights/09_new_columns.md#a-new-notebook) |
| `games.write_parquet("data/clean_games.parquet")` | saves a Parquet file | [8](../cleaning/08_text_lists.md#saving-our-clean-data) |
| `pl.DataFrame({"AppID": [1, 2], "Name": ["A", "B"]})` | makes a DataFrame from a dictionary of lists | [3](../hook/03_asking_questions.md#defining-our-terms) |
| `pl.DataFrame(list_of_dictionaries)` | makes a DataFrame from a list of dictionaries, like JSON | [13](../insights/13_api.md#reading-json) |

## Looking at data

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.shape` | the number of rows and columns | [2](../hook/02_exploring_data.md#how-big-is-our-data) |
| `games.height` | the number of rows | [5](../cleaning/05_select_filter.md#choosing-rows) |
| `games.schema` | the name and data type of each column | [2](../hook/02_exploring_data.md#what-kind-of-data-is-in-each-column) |
| `games.head(5)` | the first 5 rows | [2](../hook/02_exploring_data.md#reactive-cells) |
| `games.describe()` | summary statistics for every column | [3](../hook/03_asking_questions.md#summary-statistics) |
| `games["Genres"].value_counts(sort=True)` | how often each value appears, most common first | [3](../hook/03_asking_questions.md#counting-values) |
| `games.null_count()` | the number of nulls in each column | [7](../cleaning/07_missing_values.md#counting-nulls) |

## Choosing columns and rows

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.select("Name", "Price")` | keeps only these columns | [5](../cleaning/05_select_filter.md#choosing-columns) |
| `games.drop("Website")` | removes a column | [4](../hook/04_privacy_ethics.md#removing-columns-we-dont-need) |
| `games.filter(pl.col("Price") > 0)` | keeps only rows where the condition is true | [5](../cleaning/05_select_filter.md#choosing-rows) |
| `games.filter(condition_1, condition_2)` | keeps rows where every condition is true | [7](../cleaning/07_missing_values.md#writing-checks) |
| `(condition_1) & (condition_2)` | and: both must be true | [5](../cleaning/05_select_filter.md#combining-conditions) |
| `(condition_1) | (condition_2)` | or: at least one must be true | [5](../cleaning/05_select_filter.md#combining-conditions) |
| `~(condition)` | not: the condition must be false | [5](../cleaning/05_select_filter.md#combining-conditions) |
| `pl.col("AppID").is_in(a_list)` | true if the value is in the list | [5](../cleaning/05_select_filter.md#finding-our-storys-games) |
| `pl.col("Price").is_between(1, 60)` | true if the value is between the two numbers, including both | [11](../insights/11_charts_compare.md#histograms) |
| `games.sort("Price", descending=True)` | sorts rows, largest first | [10](../insights/10_summarising_groups.md#games-per-year) |
| `games.unique(subset=["AppID", "Time"])` | removes rows that repeat these columns | [14](../insights/14_combining.md#cleaning-the-history) |

## Making and changing columns

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.with_columns(expression, …)` | adds or replaces columns | [6](../cleaning/06_data_types.md#text-into-dates) |
| `.alias("New name")` | names the column an expression makes | [6](../cleaning/06_data_types.md#text-into-numbers) |
| `pl.col("Price").cast(pl.Int64)` | changes a column's data type | [6](../cleaning/06_data_types.md#text-into-numbers) |
| `pl.lit("Free")` | the same value in every row | [9](../insights/09_new_columns.md#years-and-price-bands) |
| `pl.when(…).then(…).when(…).then(…).otherwise(…)` | chooses a value with `if`, `elif` and `else` | [9](../insights/09_new_columns.md#years-and-price-bands) |
| `.round(1)` | rounds to 1 decimal place | [9](../insights/09_new_columns.md#calculating-a-review-score) |

## Missing values

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.col("Peak CCU").replace(0, None)` | turns every 0 into a null | [7](../cleaning/07_missing_values.md#hidden-missing-values) |
| `.fill_nan(None)` | turns every NaN into a null | [9](../insights/09_new_columns.md#nan-is-not-null) |
| `pl.col("Name").is_not_null()` | true if the value isn't null | [7](../cleaning/07_missing_values.md#writing-checks) |
| `pl.col("Name").is_duplicated()` | true if the value appears more than once | [7](../cleaning/07_missing_values.md#duplicates) |
| `games["AppID"].is_unique().all()` | true if every value is different | [7](../cleaning/07_missing_values.md#writing-checks) |
| `games.drop_nulls("Genres")` | removes rows with a null in this column | [10](../insights/10_summarising_groups.md#grouping-by-genre) |

## Text

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.col("Support email").str.contains("@gmail.com")` | true if the text contains this | [4](../hook/04_privacy_ethics.md#finding-personal-information-in-our-data) |
| `pl.col("Name").str.to_lowercase()` | changes text to lowercase | [8](../cleaning/08_text_lists.md#matching-text) |
| `pl.col("Release date").str.to_date("%b %d, %Y")` | turns text into dates, using a format code | [6](../cleaning/06_data_types.md#text-into-dates) |
| `pl.col("added").str.to_datetime()` | turns text into dates and times | [14](../insights/14_combining.md#cleaning-the-history) |
| `pl.col("Genres").str.split(",")` | splits text into a list | [8](../cleaning/08_text_lists.md#text-into-lists) |

Date format codes:

| Code | Meaning | Example |
| :-- | :-- | :-- |
| `%Y` | four-digit year | `2025` |
| `%m` | month number | `10` |
| `%b` | short month name | `Oct` |
| `%B` | full month name | `October` |
| `%d` | day of the month | `30` |

## Lists

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `.list.first()` and `.list.last()` | the first or last item of each list | [6](../cleaning/06_data_types.md#text-into-numbers) |
| `pl.col("Tags").list.contains("PvE")` | true if the list contains this item | [8](../cleaning/08_text_lists.md#searching-lists) |
| `games.explode("Genres")` | makes one row for each item in each list | [8](../cleaning/08_text_lists.md#counting-labels) |

## Dates and times

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `pl.col("Release date").dt.year()` | the year of each date | [9](../insights/09_new_columns.md#years-and-price-bands) |
| `.dt.replace_time_zone("UTC")` | says which time zone the times are in | [14](../insights/14_combining.md#cleaning-the-history) |
| `.dt.convert_time_zone("Australia/Brisbane")` | changes the times to another time zone | [14](../insights/14_combining.md#cleaning-the-history) |
| `.dt.total_days()` | the number of whole days in a length of time | [14](../insights/14_combining.md#players-per-month) |
| `pl.duration(hours=3)` | a length of time | [14](../insights/14_combining.md#checking-for-gaps) |

## Summarising

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `games.group_by("Release year").agg(…)` | splits rows into groups and summarises each one | [10](../insights/10_summarising_groups.md#games-per-year) |
| `pl.len()` | the number of rows | [10](../insights/10_summarising_groups.md#games-per-year) |
| `.mean()`, `.median()`, `.min()`, `.max()`, `.sum()` | summary of a column | [10](../insights/10_summarising_groups.md#mean-or-median) |
| `games["Price"].quantile(0.25)` | the value a quarter of the way through | [12](../insights/12_trends_outliers.md#finding-outliers) |
| `.diff()` | the change from the previous row | [12](../insights/12_trends_outliers.md#making-a-prediction) |
| `.over("AppID")` | does a calculation separately for each group, keeping every row | [14](../insights/14_combining.md#checking-for-gaps) |

## Combining

| Code | What it does | Lesson |
| :-- | :-- | :-- |
| `history.join(story_games, on="AppID")` | puts matching rows side by side | [14](../insights/14_combining.md#joining-dataframes) |
| `join(…, how="left")` | keeps every row of the first DataFrame | [14](../insights/14_combining.md#why-not-join-on-names) |
| `pl.concat([first, second])` | puts DataFrames one under the other | [13](../insights/13_api.md#getting-the-next-page) |

!!! tip "The official documentation"
    The [Polars user guide](https://docs.pola.rs/) explains every method in detail, with examples.
