# 1. Why Databases?

!!! learn "In this lesson we will learn"
    - what a relational database is, and why we'd use one instead of a CSV file
    - what tables, records, fields and primary keys are
    - the data types SQLite uses, and what `NULL` means
    - how to connect a marimo notebook to a database
    - how to write our first SQL query

!!! terms "Terminology"
    - **database** – an organised collection of data, stored so that programs can find it, add to it and change it quickly and safely.
    - **SQL** – Structured Query Language: a language for asking a database questions and changing its data.
    - **relational database** – a database that stores its data in tables, which can be linked to each other.
    - **SQLite** – a small database program that keeps a whole database in a single file, and is built into Python.
    - **table** – a set of data about one kind of thing, stored in rows and columns, like the games table.
    - **record** – one row of a table, holding all the data about one thing, such as one game.
    - **field** – one column of a table, holding one piece of data that every record has, such as a game's price.
    - **primary key** – a field whose value is different for every record, so it can pick out exactly one record.
    - **connection** – a link between a program and a database file, which carries SQL to the database and brings the answers back.
    - **query** – a question we ask a database, written in SQL.
    - **SQL cell** – a marimo cell where we write SQL instead of Python, and see the answer in the table viewer.
    - **keyword** – a word with a special meaning in SQL, like SELECT or WHERE, usually written in capitals.

## Introduction

In our data story, all our data lived in a CSV file, and we loaded it into a DataFrame to work on it. That works well when one person is exploring one table. But think about a website like Steam. Millions of people are buying games, writing reviews and changing their wishlists at the same moment, and every one of those changes has to be saved straight away, without anyone overwriting anyone else's.

That's a job for a **database**: an organised collection of data, stored so that programs can find it, add to it and change it quickly and safely. Almost every website and app we use keeps its data in a database. Next year, we'll build a website that stores its users and their data in one.

To work with a database, we use **SQL** (Structured Query Language, often said "sequel"): a language for asking a database questions and changing its data. Over the next few lessons, we'll ask the same questions about Steam games that we asked with Polars, but this time in SQL. Because it's the same data, we can check our SQL answers against the Polars answers from our data story.

## What is a database?

The database we'll use is a **relational database**: a database that stores its data in tables, which can be linked to each other. Here's how it compares with the CSV file and DataFrame we've been using:

| | CSV file and DataFrame | Relational database |
| :-- | :-- | :-- |
| tables | one table per file | many tables in one file, which can be linked |
| data types | worked out when we load the file, and can be wrong (like our dates stored as text) | set for each column when the table is made, and kept every time |
| changing data | change the DataFrame, then save the whole file again | change just the rows we need, and the change is saved straight away |
| many users at once | no: if two people save the same file, one loses their changes | yes: the database handles changes from many users safely |
| asking questions | Python code with Polars | SQL, which works with almost every database |

There are lots of database programs. We'll use **SQLite**, a small database program that keeps a whole database in a single file. It's built into Python, so we don't need to install anything. It's also the database we'll use next year.

## Tables, records and fields

A relational database stores its data in **tables**. Just like a DataFrame, a table has rows and columns:

- each row of a table is a **record**: all the data about one thing, such as one game
- each column of a table is a **field**: one piece of data that every record has, such as a game's price

Our database is called ***steam.db***, and it has two tables:

- `games` → the same 10,250 games from our data story, already cleaned. We'll only ever read this table.
- `wishlist` → a small table of games someone wants to buy. We'll use it to practise changing data, so the `games` table never changes.

Each table has a **primary key**: a field whose value is different for every record, so it can pick out exactly one record. Remember from [Fixing Our Data](../cleaning/06_fixing_data.md#repeated-names) that two games can share a name, but never an AppID. So in the `games` table, the primary key is `app_id`.

These are the fields in the `games` table:

| Field | What it holds | Data type |
| :-- | :-- | :-- |
| `app_id` | the game's Steam AppID (the primary key) | `INTEGER` |
| `name` | the game's name | `TEXT` |
| `release_date` | the date the game came out, written like `2017-02-24` | `TEXT` |
| `price` | the price in US dollars | `REAL` |
| `positive` | the number of positive reviews | `INTEGER` |
| `negative` | the number of negative reviews | `INTEGER` |
| `review_score` | positive reviews as a percentage of all reviews | `REAL` |
| `metacritic` | the game's Metacritic score, or `NULL` if it doesn't have one | `INTEGER` |
| `indie` | `1` if the game is Indie, `0` if it isn't | `INTEGER` |
| `developers` | who made the game | `TEXT` |
| `genres` | the game's genres | `TEXT` |

The fields have short, lower-case names with no spaces, like `review_score`. That's the usual way to name fields in a database, because names with spaces are awkward to type in SQL.

## Data types

Every field has a data type, just like every column in a DataFrame. SQLite uses these data types:

| SQLite data type | What it holds | Polars data type |
| :-- | :-- | :-- |
| `INTEGER` | whole numbers, like `1025` | `Int64` |
| `REAL` | numbers with a decimal point, like `14.99` | `Float64` |
| `TEXT` | text, like `Hollow Knight` | `String` |

`NULL` isn't a data type. It's the value a field has when it has no value: the same idea as a null in Polars. Remember from [Fixing Our Data](../cleaning/06_fixing_data.md#values-that-mean-missing) that a Metacritic score of 0 really meant "no score", so we turned the 0s into nulls. ***steam.db*** was made from our cleaned data, so those games have `NULL` in the `metacritic` field.

Two more of our cleaning decisions are built into ***steam.db***:

- SQLite has no date data type, so `release_date` is `TEXT`. Every date is written year first, like `2017-02-24`, so the dates sort in time order. We'll see why that matters when we combine conditions.
- `indie` holds `1` for Indie games and `0` for the rest. It's the same as our `Group` column from [Making New Columns](../insights/07_new_columns.md), stored as a number.

## Getting the database

1. Download [steam.db](../downloads/steam.db){ download="steam.db" }. It's about 1.2 MB.
2. Move ***steam.db*** into the ***data*** folder of our ***steam_data_stories*** project folder, next to ***steam_games.csv***. When we're done, the folder should look like this:

    ```text
    steam_data_stories/
        .venv/
        data/
            clean_games.parquet
            README.txt
            steam.db
            steam_games.csv
        clean_steam.py
        my_data_story.md
        steam_story.py
    ```

    We might have other files and folders too. That's fine.

!!! tip "Starting again"
    If we ever make a mess of ***steam.db***, we can download it again and replace our copy. We'll need this when we practise changing data.

## Connecting to the database

We'll write our SQL in a new marimo notebook. Open the ***steam_data_stories*** folder in VS Code, open the terminal, check the prompt starts with `(.venv)`, then type the command below and press ++enter++.

```text
marimo edit sql_intro.py
```

Before marimo can send SQL to our database, it needs a **connection**: a link between our notebook and a database file, which carries our SQL to the database and brings the answers back. We make the connection with Python, using the `sqlite3` library that comes with Python. Type the code below into the first cell and run it.

```python linenums="1" title="sql_intro.py — first cell"
--8<-- "examples/sql/01_why_databases/sql01.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports marimo, so we can use `mo.notebook_dir()` and, later, marimo's SQL cells.
    - **line 2** → imports the `sqlite3` library, which comes with Python and lets Python work with SQLite databases.
    - **line 4** → connects to ***steam.db*** in our ***data*** folder, and stores the connection in `conn`. `mo.notebook_dir()` finds the folder our notebook is in, just like in [Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server).

The cell shows nothing, because storing a connection doesn't show anything. That's fine: `conn` is ready to use.

!!! warning "Check the file name"
    If ***steam.db*** isn't in our ***data*** folder, `sqlite3.connect` doesn't give an error. It quietly makes a new, empty database called ***steam.db*** instead, and every query after that says there's no `games` table. If that happens, delete the empty file and check where our download went.

## Our first query

A **query** is a question we ask a database, written in SQL. In marimo, we write SQL in an **SQL cell**. Every SQL cell in this notebook needs to use our connection, `conn`:

1. Hover under our connection cell and click the **SQL** button to add a new SQL cell.

    <!-- SCREENSHOT: assets/s01_sql_button.png — the buttons under a marimo cell, with the SQL button labelled -->

2. At the top of the new cell, open the connection dropdown and choose `conn`.

    <!-- SCREENSHOT: assets/s01_connection.png — the top of an SQL cell with the connection dropdown open and conn selected, with the output variable name _df beside it -->

!!! warning "Always choose conn"
    marimo's SQL cells start with a different database program, called DuckDB, which can't see ***steam.db***. If we forget to choose `conn`, our query gives an error or tries to install DuckDB. Check the dropdown says `conn` in every SQL cell we add.

Our first query asks for the first five records of the `games` table, so we can see what the table looks like. Type the query below into the SQL cell and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/01_why_databases/q01.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change `5` to `10`. What changes?

??? note "Code explanation"
    - `SELECT *` → chooses which fields to show. `*` means every field.
    - `FROM games` → says which table to get the records from.
    - `LIMIT 5` → shows only the first 5 records.

marimo shows the answer in the same table viewer we used for our DataFrames. The first record is Counter-Strike, with an `app_id` of 10. Look at the `metacritic` field: some games show `NULL`.

<!-- SCREENSHOT: assets/s01_first_query.png — the SQL cell with SELECT * FROM games LIMIT 5 and its result in the table viewer, five rows starting with Counter-Strike -->

The answer to a query is always a table, even when it's only one record or one number. marimo also stores the answer as a Polars DataFrame, in the variable named at the top of the cell (`_df` to start with). We'll use that when we chart a query's answer.

!!! tip "Capital letters"
    SQL doesn't mind whether we write `SELECT` or `select`. But SQL **keywords**, like `SELECT`, `FROM` and `LIMIT`, are usually written in capitals, and table and field names in lower case. Then we can tell at a glance which words are SQL and which are our data. We'll write all our SQL this way.

## Looking at a table's structure

When we explored our CSV file, we used `schema` to see each column's data type. In SQLite, `PRAGMA table_info` shows the same thing for a table. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/01_why_databases/q02.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change `games` to `wishlist`. How many fields does the `wishlist` table have, and which one is its primary key?

??? note "Code explanation"
    - `PRAGMA table_info(games)` → shows one row for each field in the `games` table, with its name and data type.

<!-- SCREENSHOT: assets/s01_table_info.png — the result of PRAGMA table_info(games): 11 rows from app_id to genres, with the name, type and pk columns visible -->

There's one row for each of the 11 fields. The columns we need are:

- `name` → the field's name
- `type` → the field's data type: `INTEGER`, `TEXT` or `REAL`
- `pk` → `1` if the field is the primary key, otherwise `0`. Only `app_id` has a `1`.

## Check your SQL

Answer these questions with new SQL cells in ***sql_intro.py***. Remember to choose `conn` in each one.

1. Write a query that shows the first 20 records of the `games` table.
2. Write a query that shows every record in the `wishlist` table. How many records does it have?
3. Use `PRAGMA table_info` to find the data type of the `price` field in the `wishlist` table.
4. Which data type would you use for each of these: the number of achievements in a game, a game's publisher, and a game's file size in gigabytes, like `4.5`?
5. In the `games` table, what does `NULL` in the `metacritic` field mean? Why is it better than storing `0`?
