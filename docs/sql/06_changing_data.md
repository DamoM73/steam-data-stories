# 6. Changing Data

!!! learn "In this lesson we will learn"
    - how to add records with `INSERT INTO`
    - how to change records with `UPDATE`
    - how to remove records with `DELETE FROM`
    - why we check which records will change before we change them
    - what happens when we leave out `WHERE`

!!! terms "Terminology"
    - **CRUD** – create, read, update and delete: the four jobs a program does with the data in a database.

## Introduction

So far, every query has only read data. But think back to the Steam website at the start of this section: people are adding games to their wishlists, changing them and removing them all the time. A database has to do four jobs, often called **CRUD**:

- **create** → add new records, with `INSERT INTO`
- **read** → find records, with `SELECT`, which we've been doing
- **update** → change records, with `UPDATE`
- **delete** → remove records, with `DELETE FROM`

Next year, our website will do all four. In this lesson we'll practise the last three jobs on the `wishlist` table. We won't change the `games` table, so all our earlier queries keep giving the same answers.

Start marimo with `marimo edit sql_intro.py`, and run the connection cell so `conn` is ready.

!!! warning "Changes are saved straight away"
    In our data story, changing a DataFrame never changed ***steam_games.csv***. A database is different: `INSERT INTO`, `UPDATE` and `DELETE FROM` change ***steam.db*** as soon as the cell runs, and there's no undo. If we make a mess, we can download a fresh copy of ***steam.db***, as shown at the end of this lesson.

## Looking at the wishlist

Before we change a table, we need to see what's in it. We'll keep a check cell that shows the whole `wishlist` table, and run it again after every change. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/06_changing_data/q25a.sql"
```

??? note "Code explanation"
    - `SELECT *` → chooses every field.
    - `FROM wishlist` → gets the records from the `wishlist` table.

| id | name | price | priority |
| --: | :-- | --: | --: |
| 1 | Hollow Knight | 14.99 | 1 |
| 2 | Stardew Valley | 14.99 | 2 |
| 3 | Celeste | 19.99 | 3 |
| 4 | Terraria | 9.99 | 4 |
| 5 | Hades | 24.99 | 5 |

Each record is a game someone wants to buy, with its full price in US dollars and a priority, where 1 is the game they want most. The primary key is `id`.

!!! warning "One cell for changes"
    marimo runs a cell again whenever we run all our cells, such as when we press ++ctrl+shift+r++ after opening the notebook. If a cell adds a record, running it again adds the record again. So we'll use **one** SQL cell for all our changes, and replace its query each time. When we finish this lesson, we'll delete that cell.

## Adding records

`INSERT INTO` adds a new record to a table. We list the fields we're giving values for, then the values, in the same order. Let's add Dead Cells to the wishlist. Add a new SQL cell (our change cell), choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/06_changing_data/q26.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. What `id` will the new record get?
    2. **Run** the cell, then run the check cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `INSERT INTO wishlist (name, price, priority)` → adds a new record to the `wishlist` table, giving values for the `name`, `price` and `priority` fields.
    - `VALUES ('Dead Cells', 24.99, 2)` → gives the values, in the same order as the fields: text in single quotes, numbers without.

The change cell shows no table, because `INSERT INTO` doesn't ask for any records. The check cell doesn't run again by itself, because marimo doesn't know that the table has changed, so we run it ourselves. Now the wishlist has 6 records, and Dead Cells has an `id` of **6**. We didn't give a value for `id`, so SQLite numbered the new record itself: an `INTEGER PRIMARY KEY` gets the next number automatically.

We can add several records with one `INSERT INTO`, by listing several sets of values, separated by commas. Change the change cell to match the query below and run it, then run the check cell.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/06_changing_data/q27.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell, then run the check cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `INSERT INTO wishlist (name, price, priority)` → adds new records to the `wishlist` table, giving values for the `name`, `price` and `priority` fields.
    - `VALUES ('Slay the Spire', 24.99, 3), ('Katana ZERO', 14.99, 4)` → gives the values for two records, each in its own brackets.

Slay the Spire gets an `id` of **7** and Katana ZERO gets **8**.

## Changing records

Celeste has gone on sale for $4.99. `UPDATE` changes the values in records that already exist, and `WHERE` says **which** records to change. Before we change anything, we check that our `WHERE` clause picks out exactly the records we mean, by using it in a `SELECT` first. Change the change cell to match the query below and run it.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/06_changing_data/q28.sql"
```

??? note "Code explanation"
    - `SELECT *` → chooses every field.
    - `FROM wishlist` → gets the records from the `wishlist` table.
    - `WHERE name = 'Celeste'` → keeps only the record whose name is `Celeste`.

There's one record, Celeste, so this `WHERE` clause is safe to use. Now change the change cell to match the query below and run it, then run the check cell.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/06_changing_data/q29.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell, then run the check cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Hollow Knight is now your top priority, and Celeste is second. Write one `UPDATE` for each change. Check each `WHERE` with a `SELECT` first.

??? note "Code explanation"
    - `UPDATE wishlist` → changes records in the `wishlist` table.
    - `SET price = 4.99` → sets the `price` field to 4.99. Here `=` stores a value, instead of comparing.
    - `WHERE name = 'Celeste'` → changes only the record whose name is `Celeste`.

Celeste now costs **$4.99**. Its other fields haven't changed.

!!! tip "Use the primary key"
    `WHERE name = 'Celeste'` is safe in our small wishlist, but remember that two games can share a name. In a real database, the safest way to change one record is with its primary key: `WHERE id = 3`. That can only ever match one record.

## Removing records

`DELETE FROM` removes whole records, and `WHERE` says which ones. Let's remove every game with a priority of 4 or more: the games we want least. First, check which records our `WHERE` clause picks out. Change the change cell to match the query below and run it.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/06_changing_data/q30.sql"
```

??? note "Code explanation"
    - `SELECT *` → chooses every field.
    - `FROM wishlist` → gets the records from the `wishlist` table.
    - `WHERE priority >= 4` → keeps only the records with a priority of 4 or more.

There are three records: Terraria, Hades and Katana ZERO. That's what we want to remove, so change the change cell to match the query below and run it, then run the check cell.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/06_changing_data/q31.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. How many records will be left?
    2. **Run** the cell, then run the check cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `DELETE FROM wishlist` → removes records from the `wishlist` table.
    - `WHERE priority >= 4` → removes only the records with a priority of 4 or more.

Five records are left: Hollow Knight, Stardew Valley, Celeste, Dead Cells and Slay the Spire. Notice that the `id` values didn't change. The `id` of a record stays the same for as long as the record exists, which is what makes it a good primary key.

## Forgetting WHERE

The `WHERE` clause is what stops `UPDATE` and `DELETE FROM` changing **every** record. Let's see what happens without one, so we never do it by accident in a real database. We want to make Stardew Valley our top priority, but we'll forget the `WHERE` clause. Change the change cell to match the query below and run it, then run the check cell.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/06_changing_data/q32.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell, then run the check cell.
    3. Time to **investigate** the query. Why did it change so much?

??? note "Code explanation"
    - `UPDATE wishlist` → changes records in the `wishlist` table.
    - `SET priority = 1` → sets the `priority` field to 1. With no `WHERE` clause, it does this to every record.

<!-- SCREENSHOT: assets/s06_update_all.png — the check cell after UPDATE wishlist SET priority = 1, with all five records showing a priority of 1 -->

Every game now has a priority of 1, and there's no error and no warning. SQLite did exactly what we asked. Without `WHERE`, `DELETE FROM wishlist` would be even worse: it would remove every record in the table.

!!! warning "Check before we change"
    Before every `UPDATE` or `DELETE FROM`:

    1. write the `WHERE` clause first
    2. run it in a `SELECT`, and check it picks out only the records we mean
    3. then change `SELECT *` to `UPDATE … SET …` or `DELETE`, keeping the same `WHERE` clause

## Starting again

Our wishlist's priorities are now wrong, and there's no undo. To start again, we replace our copy of ***steam.db***:

1. Delete the change cell, so it doesn't run again.
2. Stop marimo: click in the VS Code terminal, press ++ctrl+c++, type `y` and press ++enter++. While marimo has ***steam.db*** open, Windows may not let us replace it.
3. Download [steam.db](../downloads/steam.db){ download="steam.db" } again, and move it into the ***data*** folder, replacing the old copy.
4. Start marimo with `marimo edit sql_intro.py`, and press ++ctrl+shift+r++ to run all the cells. The check cell shows the five original records again.

## Check your SQL

Answer these questions with your change cell in ***sql_intro.py***, and run the check cell after each change. Check every `WHERE` clause with a `SELECT` first.

1. Add three games you'd like to buy to the wishlist, with one `INSERT INTO`. Use their prices from the `games` table.
2. One of your games has gone on sale. Change its price, using its `id` in the `WHERE` clause.
3. Change the priority of every game that costs less than $10 to 1.
4. Remove every game that costs more than $20.
5. What would `DELETE FROM wishlist` do? Explain why, without running it.

When you've finished, delete the change cell.
