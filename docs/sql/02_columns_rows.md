# 2. Choosing Columns and Rows in SQL

!!! learn "In this lesson we will learn"
    - how to choose fields with `SELECT`
    - how to choose records with `WHERE` and comparison operators
    - how to write text values in a query
    - how to find missing values with `IS NULL` and `IS NOT NULL`
    - how `SELECT` and `WHERE` match Polars' `select` and `filter`

!!! terms "Terminology"
    - **clause** – a part of an SQL query that starts with a keyword and does one job, like FROM games.
    - **comparison operator** – a symbol, like = or >, that compares two values and gives true or false.

## Introduction

When we cleaned our data, the first job was to cut the table down to the columns and rows our question needed. In [Choosing Columns and Rows](../cleaning/05_select_filter.md), we used `select` to choose columns and `filter` to choose rows. SQL does the same two jobs, with `SELECT` and `WHERE`.

Start marimo with `marimo edit sql_intro.py`, and run the connection cell so `conn` is ready.

## Choosing fields

So far we've used `SELECT *` to show every field. Most of the time we only need a few. Let's say we want to compare prices and reviews: then we need each game's name, price and review score, and nothing else. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/02_columns_rows/q04.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Add `developers` to the list of fields. Does it matter where in the list we put it?

??? note "Code explanation"
    - `SELECT name, price, review_score` → chooses three fields, in this order, separated by commas.
    - `FROM games` → gets the records from the `games` table.

The answer has all 10,250 records, but only three fields. The fields appear in the order we listed them, not the order they're stored in the table.

Each line of our query is a **clause**: a part of a query that starts with a keyword and does one job. `SELECT` chooses the fields and `FROM` chooses the table. Putting each clause on its own line makes a query easier to read. SQL doesn't need the line breaks, but we'll keep using them.

## Choosing records

To choose records, we add a `WHERE` clause with a condition. Only the records where the condition is true are kept. Let's find the most expensive games: those that cost more than $50. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/02_columns_rows/q05.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. How many games do you think cost more than $50?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change `price > 50` to `price = 0`. How many games are free?

??? note "Code explanation"
    - `SELECT name, price` → chooses the name and price fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE price > 50` → keeps only the records where the price is more than 50.

Only **32** games cost more than $50. 24 of them cost $59.99, and the 7 most expensive cost $69.99, like NBA 2K25 and EA SPORTS FC™ 25. The number of records is shown under the table.

The `>` in our condition is a **comparison operator**: a symbol that compares two values and gives true or false. SQL has six of them:

| Operator | Meaning | Example | Records |
| :-- | :-- | :-- | --: |
| `=` | equal to | `price = 0` | 1,411 |
| `!=` | not equal to | `indie != 1` | 4,007 |
| `<` | less than | `review_score < 20` | 11 |
| `>` | more than | `price > 50` | 32 |
| `<=` | less than or equal to | `price <= 1` | 2,258 |
| `>=` | more than or equal to | `review_score >= 99` | 42 |

!!! warning "One equals sign"
    In Python and Polars, we compare with two equals signs: `pl.col("Price") == 0`. In SQL, we compare with **one**: `price = 0`. SQL doesn't use `=` to store values, so it doesn't need two.

## Text values

To compare a field with some text, we put the text in **single quotes**. Let's find the games made by Team Cherry, the Adelaide studio that made Hollow Knight. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/02_columns_rows/q06.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change `'Team Cherry'` to `'Valve'`. How many games did Valve make?

??? note "Code explanation"
    - `SELECT name, release_date, price` → chooses the name, release date and price fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE developers = 'Team Cherry'` → keeps only the records whose `developers` field is exactly the text `Team Cherry`.

There's one record: Hollow Knight, released on `2017-02-24`.

What happens if we leave out the quotes? Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/02_columns_rows/q06a.sql"
```

<!-- SCREENSHOT: assets/s02_no_such_column.png — the SQL cell with WHERE developers = Valve and the red error under it: OperationalError: no such column: Valve -->

Let's read the error in parts:

- **OperationalError** → SQLite couldn't run our query
- **no such column: Valve** → without quotes, SQLite thinks `Valve` is the name of a field, and our table has no field called `Valve`

So text values always go in single quotes. Field names, like `developers`, never do. Delete this cell before we move on.

!!! tip "Text must match exactly"
    `=` only matches text that's exactly the same, including capital letters: `developers = 'valve'` finds no games, because the developer is `Valve`. When we combine conditions, we'll see how to search for text that only contains a word.

## Missing values

Only some games have a Metacritic score. The rest have `NULL` in the `metacritic` field. To find the games that do have a score, we can't use a comparison operator, because `NULL` means "no value", and no value can't be compared with anything. Instead, SQL has `IS NULL` and `IS NOT NULL`. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/02_columns_rows/q07.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change `IS NOT NULL` to `IS NULL`. How many games have no Metacritic score?

??? note "Code explanation"
    - `SELECT name, metacritic` → chooses the name and Metacritic score fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE metacritic IS NOT NULL` → keeps only the records that have a value in the `metacritic` field.

**2,933** games have a Metacritic score. With `IS NULL`, we get the other **7,317**: the same number of nulls we found when we [fixed our data](../cleaning/06_fixing_data.md#values-that-mean-missing).

!!! warning "Never use = NULL"
    `WHERE metacritic = NULL` doesn't give an error, but it finds **0** records, because nothing is ever equal to "no value". Always use `IS NULL` or `IS NOT NULL`.

## SQL and Polars

Here's the same question, the name and price of every game over $50, in Polars and in SQL:

| Polars | SQL |
| :-- | :-- |
| `games.select("Name", "Price")` | `SELECT name, price FROM games` |
| `.filter(pl.col("Price") > 50)` | `WHERE price > 50` |

- `select` → `SELECT`: both choose columns
- `filter` → `WHERE`: both keep the rows where a condition is true

There's one difference in the order. In Polars, we can `select` and `filter` in either order. In SQL, the clauses always go in the same order, `SELECT`, then `FROM`, then `WHERE`, even though SQLite uses `WHERE` to choose the records before it picks out the fields.

## Check your SQL

Answer these questions with new SQL cells in ***sql_intro.py***. Remember to choose `conn` in each one.

1. Which games cost exactly $19.99? Show their name and price.
2. Which games have a review score less than 20? Show their name, review score, and numbers of positive and negative reviews.
3. Show the name and release date of every game made by `Supergiant Games`.
4. How many games are **not** Indie games?
5. Write a query that finds every game whose Metacritic score is missing. Why does `WHERE metacritic = NULL` not work?
