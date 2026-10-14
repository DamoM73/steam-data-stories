# SQL

!!! learn "On this page we will learn"
    - the SQL used in this course
    - the order the clauses of a query go in
    - how each SQL clause matches the Polars we already know
    - where each one is explained

**SQL** is a language for asking a database questions and changing its data. We use it with **SQLite**, a database program that keeps a whole database in one file and is built into Python. Our database, ***steam.db***, has a `games` table and a `wishlist` table, described in [Why Databases?](../sql/01_why_databases.md#tables-records-and-fields).

## Connecting from marimo

One Python cell connects our notebook to the database:

```python title="sql_intro.py — first cell"
--8<-- "examples/sql/01_why_databases/sql01.py"
```

Then each query goes in its own SQL cell: click the **SQL** button under a cell, and choose `conn` in the cell's connection dropdown. marimo shows the answer in the table viewer, and stores it as a Polars DataFrame in the cell's output variable (`_df` to start with). See [Why Databases?](../sql/01_why_databases.md#our-first-query).

## Data types

| SQLite | What it holds | Polars |
| :-- | :-- | :-- |
| `INTEGER` | whole numbers | `Int64` |
| `REAL` | numbers with a decimal point | `Float64` |
| `TEXT` | text, in single quotes in a query, like `'Valve'` | `String` |
| `NULL` | no value: the value is missing | null |

## The order of the clauses

A query's clauses always go in this order. Every query needs `SELECT` and `FROM`; the rest are only used when we need them.

1. `SELECT` → which fields to show, or what to calculate
2. `FROM` → which table to use
3. `WHERE` → which records to keep, before grouping
4. `GROUP BY` → how to split the records into groups
5. `HAVING` → which groups to keep, after grouping
6. `ORDER BY` → how to sort the answer
7. `LIMIT` → how many records to show

```sql title="an example with every clause"
SELECT developers, COUNT(*) AS games, ROUND(AVG(review_score), 1) AS mean_score
FROM games
WHERE indie = 1
GROUP BY developers
HAVING COUNT(*) >= 5
ORDER BY mean_score DESC
LIMIT 10
```

## Polars and SQL

| Polars | SQL | Where we learned it |
| :-- | :-- | :-- |
| `select("Name", "Price")` | `SELECT name, price` | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#choosing-fields) |
| `filter(pl.col("Price") > 50)` | `WHERE price > 50` | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#choosing-records) |
| `sort("Price", descending=True)` | `ORDER BY price DESC` | [Sorting and Summarising](../sql/04_sorting_summarising.md#sorting-records) |
| `head(10)` | `LIMIT 10` | [Sorting and Summarising](../sql/04_sorting_summarising.md#sorting-records) |
| `alias("reviews")` | `AS reviews` | [Sorting and Summarising](../sql/04_sorting_summarising.md#naming-our-answers) |
| `group_by("Group").agg(...)` | `GROUP BY indie` | [Summarising Groups in SQL](../sql/05_summarising_groups.md#indie-and-not-indie) |
| `filter` after `agg` | `HAVING COUNT(*) >= 5` | [Summarising Groups in SQL](../sql/05_summarising_groups.md#keeping-some-groups-with-having) |
| `pl.len()` | `COUNT(*)` | [Sorting and Summarising](../sql/04_sorting_summarising.md#summarising-the-whole-table) |
| `pl.col("Price").mean()` | `AVG(price)` | [Sorting and Summarising](../sql/04_sorting_summarising.md#summarising-the-whole-table) |
| `pl.col("Price").is_null()` | `price IS NULL` | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#missing-values) |
| `pl.col("Name").str.contains("Zombie")` | `name LIKE '%zombie%'` | [Combining Conditions](../sql/03_combining_conditions.md#like) |
| `&` and <code>&#124;</code> | `AND` and `OR` | [Combining Conditions](../sql/03_combining_conditions.md#and) |

## Choosing records

| SQL | Keeps the records where… | Where we learned it |
| :-- | :-- | :-- |
| `price = 0` | the value is equal (one `=`, not two) | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#choosing-records) |
| `indie != 1` | the value is not equal | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#choosing-records) |
| `price < 5`, `price > 50`, `price <= 1`, `price >= 10` | the value is less than, more than, or equal to as well | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#choosing-records) |
| `developers = 'Valve'` | the text is exactly the same, including capitals | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#text-values) |
| `metacritic IS NULL`, `metacritic IS NOT NULL` | the value is missing, or isn't missing (never `= NULL`) | [Choosing Columns and Rows in SQL](../sql/02_columns_rows.md#missing-values) |
| `indie = 1 AND price < 5` | both conditions are true | [Combining Conditions](../sql/03_combining_conditions.md#and) |
| `price < 1 OR price > 50` | either condition is true | [Combining Conditions](../sql/03_combining_conditions.md#or) |
| `(a OR b) AND c` | the brackets are worked out first (`AND` comes before `OR` without them) | [Combining Conditions](../sql/03_combining_conditions.md#brackets) |
| `developers IN ('Valve', 'Team Cherry')` | the value is in the list | [Combining Conditions](../sql/03_combining_conditions.md#in) |
| `price BETWEEN 10 AND 20` | the value is in the range, including both ends | [Combining Conditions](../sql/03_combining_conditions.md#between) |
| `name LIKE '%zombie%'` | the text matches the pattern; `%` stands for any characters, and capitals are ignored | [Combining Conditions](../sql/03_combining_conditions.md#like) |
| `release_date >= '2024-01-01'` | the date is on or after 1 January 2024 (dates written year first) | [Combining Conditions](../sql/03_combining_conditions.md#comparing-dates) |

## Sorting and summarising

| SQL | What it does | Where we learned it |
| :-- | :-- | :-- |
| `ORDER BY price` | sorts from smallest to biggest | [Sorting and Summarising](../sql/04_sorting_summarising.md#sorting-records) |
| `ORDER BY price DESC` | sorts from biggest to smallest | [Sorting and Summarising](../sql/04_sorting_summarising.md#sorting-records) |
| `ORDER BY review_score DESC, positive DESC` | sorts by a second field when the first is a tie | [Sorting and Summarising](../sql/04_sorting_summarising.md#breaking-ties) |
| `LIMIT 10` | shows only the first 10 records | [Sorting and Summarising](../sql/04_sorting_summarising.md#sorting-records) |
| `positive + negative AS reviews` | calculates a value and names it | [Sorting and Summarising](../sql/04_sorting_summarising.md#naming-our-answers) |
| `COUNT(*)` | counts records | [Sorting and Summarising](../sql/04_sorting_summarising.md#summarising-the-whole-table) |
| `COUNT(metacritic)` | counts the values that aren't `NULL` | [Sorting and Summarising](../sql/04_sorting_summarising.md#counting-missing-values) |
| `MIN(price)`, `MAX(price)` | the smallest and biggest values | [Sorting and Summarising](../sql/04_sorting_summarising.md#summarising-the-whole-table) |
| `AVG(price)` | the mean (SQLite has no median) | [Sorting and Summarising](../sql/04_sorting_summarising.md#summarising-the-whole-table) |
| `ROUND(AVG(price), 2)` | rounds to 2 decimal places | [Sorting and Summarising](../sql/04_sorting_summarising.md#summarising-the-whole-table) |
| `GROUP BY developers` | one record per group, with the aggregate functions worked out for each group | [Summarising Groups in SQL](../sql/05_summarising_groups.md#grouping-by-developer) |
| `HAVING COUNT(*) >= 5` | keeps only the groups where the condition is true | [Summarising Groups in SQL](../sql/05_summarising_groups.md#keeping-some-groups-with-having) |

## Changing data

These change ***steam.db*** as soon as the cell runs, and there's no undo. Before every `UPDATE` or `DELETE FROM`, run the same `WHERE` clause in a `SELECT` to check which records will change.

| SQL | What it does | Where we learned it |
| :-- | :-- | :-- |
| `INSERT INTO wishlist (name, price, priority) VALUES ('Dead Cells', 24.99, 2)` | adds a record; an `INTEGER PRIMARY KEY` is numbered automatically | [Changing Data](../sql/06_changing_data.md#adding-records) |
| `VALUES ('A', 1.99, 3), ('B', 2.99, 4)` | adds several records at once | [Changing Data](../sql/06_changing_data.md#adding-records) |
| `UPDATE wishlist SET price = 4.99 WHERE id = 3` | changes the records the `WHERE` clause picks out | [Changing Data](../sql/06_changing_data.md#changing-records) |
| `DELETE FROM wishlist WHERE priority >= 4` | removes the records the `WHERE` clause picks out | [Changing Data](../sql/06_changing_data.md#removing-records) |
| `UPDATE` or `DELETE FROM` with no `WHERE` | changes or removes **every** record | [Changing Data](../sql/06_changing_data.md#forgetting-where) |

## Looking at a table

| SQL | What it does | Where we learned it |
| :-- | :-- | :-- |
| `SELECT * FROM games LIMIT 5` | shows the first 5 records, with every field | [Why Databases?](../sql/01_why_databases.md#our-first-query) |
| `PRAGMA table_info(games)` | shows each field's name and data type, and which is the primary key | [Why Databases?](../sql/01_why_databases.md#looking-at-a-tables-structure) |
