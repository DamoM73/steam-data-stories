# 4. Sorting and Summarising

!!! learn "In this lesson we will learn"
    - how to sort records with `ORDER BY` and `DESC`
    - how to sort by two fields to break ties
    - how to answer "top 10" questions with `LIMIT`
    - how to name a field in our answer with `AS`
    - how to summarise a whole table with `COUNT`, `MIN`, `MAX`, `AVG` and `ROUND`

!!! terms "Terminology"
    - **descending** – sorted from the biggest value to the smallest.
    - **ascending** – sorted from the smallest value to the biggest.
    - **alias** – a new name for a column or field in an answer, given with AS in SQL or alias in Polars.
    - **aggregate function** – a function, like COUNT or AVG, that turns the values in many records into one value.

## Introduction

So far, our answers have come back in the order the records are stored in the table. That's fine for checking a few records, but lots of questions are about order: which games are the best reviewed, the cheapest, or the newest? Other questions need a single number, like how many games there are or what they cost on average. In this lesson we'll do both.

Start marimo with `marimo edit sql_intro.py`, and run the connection cell so `conn` is ready.

## Sorting records

`ORDER BY` sorts the records by a field. Let's find the best-reviewed games. The highest score should come first, so we sort in **descending** order, from biggest to smallest, with `DESC`. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/04_sorting_summarising/q16.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Remove `DESC`. Which games come first now?

??? note "Code explanation"
    - `SELECT name, review_score` → chooses the name and review score fields.
    - `FROM games` → gets the records from the `games` table.
    - `ORDER BY review_score DESC` → sorts the records by review score, biggest first.
    - `LIMIT 10` → keeps only the first 10 records after sorting.

The best-reviewed game is Kabuto Park, with **99.9%** positive reviews. Without `DESC`, `ORDER BY` sorts in **ascending** order, from smallest to biggest, and the worst-reviewed games come first.

`ORDER BY` and `LIMIT` together answer "top 10" questions: sort so the records we want come first, then keep only as many as we need. The order matters: SQLite sorts first, then cuts the list down.

## Breaking ties

Look at the top of our list. Seal World, Beastieball and Aokana - Four Rhythms Across the Blue - EXTRA2 all have a score of 99.6, so which should come first? A score from thousands of reviews is more convincing than one from a few hundred. So when two games have the same score, let's put the one with more positive reviews first. We do that by sorting by a second field. Change the cell to match the query below and run it.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/04_sorting_summarising/q17.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Which of the three 99.6 games will come first?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `SELECT name, review_score, positive` → chooses the name, review score and positive reviews fields.
    - `FROM games` → gets the records from the `games` table.
    - `ORDER BY review_score DESC, positive DESC` → sorts by review score, biggest first. Records with the same review score are then sorted by their number of positive reviews, biggest first.
    - `LIMIT 10` → keeps only the first 10 records.

Now the three games with 99.6 are in order of positive reviews: Aokana (1,774), Beastieball (1,163), then Seal World (895). The second field only matters when the first field is a tie.

## Naming our answers

The fields we `SELECT` don't have to be fields in the table. We can also calculate a new value for each record, like we did with `with_columns` in Polars. The total number of reviews a game has is its positive reviews plus its negative reviews. Let's find the 10 games with the most reviews. We give our calculation a name with `AS`, so we can use the name in `ORDER BY`, and so the answer has a clear field name. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/04_sorting_summarising/q18.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Which game do you think has the most reviews?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Remove `AS reviews`, and change `ORDER BY reviews DESC` to `ORDER BY positive + negative DESC`. What is the field called now?

??? note "Code explanation"
    - `SELECT name, positive + negative AS reviews` → chooses the name field, and adds the positive and negative reviews of each game, naming the answer `reviews`.
    - `FROM games` → gets the records from the `games` table.
    - `ORDER BY reviews DESC` → sorts by the new `reviews` field, biggest first.
    - `LIMIT 10` → keeps only the first 10 records.

Counter-Strike 2 has the most reviews by far: **8,815,087**. The new name is an **alias**, just like `alias` in Polars. Without one, the field is named after the calculation, `positive + negative`, which is hard to read and awkward to use.

## Summarising the whole table

Sometimes we want one number about all the records, not a list of records. SQL has **aggregate functions** for this: functions that turn the values in many records into one value, just like the summaries we made in Polars with `agg`.

| Function | What it gives | Polars |
| :-- | :-- | :-- |
| `COUNT(*)` | the number of records | `pl.len()` |
| `MIN(price)` | the smallest value | `pl.col("Price").min()` |
| `MAX(price)` | the biggest value | `pl.col("Price").max()` |
| `AVG(price)` | the mean | `pl.col("Price").mean()` |
| `ROUND(AVG(price), 2)` | a value rounded to 2 decimal places | `.round(2)` |

Let's find out how many games there are, the lowest and highest prices, and the mean price. We round the mean to 2 decimal places, because prices are in dollars and cents. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/04_sorting_summarising/q19.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. How many records will the answer have?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `SELECT COUNT(*) AS games` → counts the records, and names the answer `games`.
    - `MIN(price) AS lowest` → finds the smallest price, and names it `lowest`.
    - `MAX(price) AS highest` → finds the biggest price, and names it `highest`.
    - `ROUND(AVG(price), 2) AS mean_price` → finds the mean price, rounds it to 2 decimal places and names it `mean_price`.
    - `FROM games` → gets the records from the `games` table.

The answer is one record: **10,250** games, from **$0** to **$69.99**, with a mean price of **$6.65**. Notice how the functions fit inside each other: `AVG(price)` works out the mean first, then `ROUND` rounds it.

## Counting missing values

`COUNT(*)` counts records. `COUNT` with a field name inside the brackets does something different. Let's compare them. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/04_sorting_summarising/q20.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Will the two numbers be the same?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `SELECT COUNT(*) AS games` → counts every record, and names the answer `games`.
    - `COUNT(metacritic) AS with_metacritic` → counts only the records that have a value in the `metacritic` field, and names the answer `with_metacritic`.
    - `FROM games` → gets the records from the `games` table.

We get **10,250** and **2,933**. `COUNT(metacritic)` skips the `NULL` values. So do `AVG`, `MIN` and `MAX`, so the mean Metacritic score only uses the games that really have one. If the missing scores were still stored as 0, every one of them would drag the mean down, which is exactly why we turned them into nulls.

## Summarising some records

We can use `WHERE` with an aggregate function to summarise only some of the records. Let's find how well the games released in 2024 were reviewed. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/04_sorting_summarising/q21.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change it to summarise the games released in 2015. Were they reviewed better or worse?

??? note "Code explanation"
    - `SELECT COUNT(*) AS games` → counts the records, and names the answer `games`.
    - `ROUND(AVG(review_score), 1) AS mean_score` → finds the mean review score, rounded to 1 decimal place, and names it `mean_score`.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE release_date BETWEEN '2024-01-01' AND '2024-12-31'` → keeps only the games released in 2024, before anything is counted.

The **929** games from 2024 have a mean review score of **83.8%**. SQLite picks out the records with `WHERE` first, then summarises only those records.

!!! tip "The order of the clauses"
    The clauses we've used so far always go in this order: `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`. If we write them in a different order, SQLite gives an error. The [SQL](../reference/sql.md#the-order-of-the-clauses) reference page shows the full list.

## Check your SQL

Answer these questions with new SQL cells in ***sql_intro.py***. Remember to choose `conn` in each one.

1. What are the 10 most expensive games? Show their name and price.
2. Which 5 games were released first?
3. What's the mean review score of all Indie games, rounded to 1 decimal place?
4. How many games have a Metacritic score of 90 or more, and what's their mean price?
5. Show the 10 games with the most negative reviews, with a field called `percent_negative` that works out `100 - review_score`, rounded to 1 decimal place.
