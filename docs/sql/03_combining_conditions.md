# 3. Combining Conditions

!!! learn "In this lesson we will learn"
    - how to combine conditions with `AND` and `OR`
    - why brackets matter when we mix `AND` and `OR`
    - how to match a list of values with `IN` and a range with `BETWEEN`
    - how to search text with `LIKE`
    - how to compare dates stored as text

!!! terms "Terminology"
    - **logical operator** – a word, like AND or OR, that joins conditions together into one bigger condition.
    - **wildcard** – a symbol that stands for any characters when we search text, like % in LIKE.

## Introduction

Most questions need more than one condition. When we cleaned our data, we combined conditions with `&` and `|` in [Choosing Columns and Rows](../cleaning/05_select_filter.md#combining-conditions). SQL uses the words `AND` and `OR` instead. These are **logical operators**: words that join conditions together into one bigger condition.

Start marimo with `marimo edit sql_intro.py`, and run the connection cell so `conn` is ready.

## AND

`AND` keeps a record only when **both** conditions are true. Let's find the best-reviewed Indie games: the ones where `indie` is 1 **and** at least 98% of reviews are positive. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q08.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Will there be more or fewer records than when we only asked for Indie games?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Add a third condition, `AND price < 5`. How many games are left?

??? note "Code explanation"
    - `SELECT name, price, review_score` → chooses the name, price and review score fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE indie = 1 AND review_score >= 98` → keeps only the records where both conditions are true: the game is Indie, and its review score is 98 or more.

**141** Indie games have a review score of 98 or more, including Stardew Valley (98.4) and TY the Tasmanian Tiger (98.0), from Brisbane's Krome Studios. Each extra condition joined with `AND` can only keep the same records or fewer.

## OR

`OR` keeps a record when **either** condition is true, or both. Let's find every game made by Valve or by Team Cherry. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q09.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `SELECT name, developers, price` → chooses the name, developers and price fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE developers = 'Valve' OR developers = 'Team Cherry'` → keeps the records where the developer is Valve, or the developer is Team Cherry.

There are **33** records: Valve's 32 games and Team Cherry's Hollow Knight. Notice that we have to write `developers =` twice. `WHERE developers = 'Valve' OR 'Team Cherry'` doesn't work, because each side of `OR` must be a whole condition.

## Brackets

Now let's narrow that down to the games from Valve or Team Cherry that cost more than $10. That needs `OR` and `AND` in the same condition. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q10.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. How many games do you think will cost more than $10?
    2. **Run** the cell.
    3. Time to **investigate** the query. Look at the prices. Do they all cost more than $10?

??? note "Code explanation"
    - `SELECT name, developers, price` → chooses the name, developers and price fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE developers = 'Valve' OR developers = 'Team Cherry' AND price > 10` → SQLite works out `AND` before `OR`, so this keeps every Valve game, plus any Team Cherry game that costs more than $10.

We get **32** records, and most of them cost much less than $10. Some are even free. Something has gone wrong.

Just like multiplication comes before addition in maths, SQL works out `AND` before `OR`. So SQLite read our condition as "Valve, **or** (Team Cherry **and** more than $10)". That kept all 32 Valve games, whatever their price, and Hollow Knight costs less than $10, so it was left out.

To make SQLite work out the `OR` first, we put it in brackets, just like we did in Polars. Change the cell to match the query below and run it.

```sql title="sql_intro.py — change existing cell"
--8<-- "examples/sql/03_combining_conditions/q11.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What do the brackets change?

??? note "Code explanation"
    - `SELECT name, developers, price` → chooses the name, developers and price fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE (developers = 'Valve' OR developers = 'Team Cherry') AND price > 10` → works out the brackets first, so a record is kept only if it's from Valve or Team Cherry, **and** it costs more than $10.

Now there's just **1** record: Half-Life: Alyx, at $17.99.

!!! tip "Use brackets whenever we mix AND and OR"
    The wrong answer didn't cause an error. It just quietly gave us the wrong records. Whenever a condition has both `AND` and `OR`, put brackets around the part that should be worked out first, and check the answer makes sense.

## IN

Checking for lots of values with `OR` gets long. `IN` checks whether a value is in a list, which we write in brackets with commas between the values. Let's find the games from three famous Indie studios. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q12.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Rewrite the `WHERE` clause using `OR` instead of `IN`. Do you get the same records?

??? note "Code explanation"
    - `SELECT name, developers` → chooses the name and developers fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE developers IN ('Team Cherry', 'ConcernedApe', 'Supergiant Games')` → keeps the records whose developer is any of the three values in the list.

There are **7** games: Hollow Knight, Stardew Valley, and five games from Supergiant Games, including Hades and Hades II.

## BETWEEN

`BETWEEN` checks whether a value is in a range. Let's find the games that cost from $10 to $20. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q13.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Will a game that costs exactly $20 be included?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?

??? note "Code explanation"
    - `SELECT name, price` → chooses the name and price fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE price BETWEEN 10 AND 20` → keeps the records whose price is from 10 to 20. The `AND` here is part of `BETWEEN`, not a logical operator.

**1,528** games cost from $10 to $20. `BETWEEN` includes both ends of the range, so it's the same as `price >= 10 AND price <= 20`.

## LIKE

Sometimes we want text that **contains** a word, not text that's exactly the same. For that, SQL has `LIKE`, with a **wildcard**: a symbol that stands for any characters. In `LIKE`, the wildcard `%` stands for any number of characters, even none. Let's find every game with "zombie" in its name. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q14.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Will it find "Plants vs. Zombies", which has a capital Z?
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change `'%zombie%'` to `'The %'`. Which games does it find now?

??? note "Code explanation"
    - `SELECT name` → chooses the name field.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE name LIKE '%zombie%'` → keeps the records whose name has "zombie" anywhere in it: `%` before it means any characters can come first, and `%` after it means any characters can come after.

**39** games have "zombie" in their name, including Plants vs. Zombies GOTY Edition. In SQLite, `LIKE` ignores capital letters, so `'%zombie%'` matches "Zombie" too.

Where we put the `%` changes what we find:

| Pattern | Finds names that… | Example |
| :-- | :-- | :-- |
| `'%zombie%'` | contain "zombie" anywhere | Plants vs. Zombies GOTY Edition |
| `'The %'` | start with "The " | The Witcher 3: Wild Hunt |
| `'%2'` | end with "2" | Portal 2 |

`LIKE` is the SQL version of `str.contains`, which we used to find the Indie games in [Asking a Question Data Can Answer](../hook/03_asking_questions.md#defining-our-terms). In fact, `WHERE genres LIKE '%Indie%'` finds **6,243** games: exactly the same games as `WHERE indie = 1`.

## Comparing dates

Our dates are stored as text, like `2017-02-24`. SQLite compares text one character at a time, from the left, just like sorting words in a dictionary. Because each date starts with the year, then the month, then the day, comparing the text gives the same answer as comparing the dates. Let's find the games released in 2024. Add a new SQL cell, choose `conn`, type the query below and run it.

```sql title="sql_intro.py — new SQL cell"
--8<-- "examples/sql/03_combining_conditions/q15.sql"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the query. What does each part do?
    4. Time to **modify** the query. Change it to find the games released since 1 July 2025.

??? note "Code explanation"
    - `SELECT name, release_date` → chooses the name and release date fields.
    - `FROM games` → gets the records from the `games` table.
    - `WHERE release_date BETWEEN '2024-01-01' AND '2024-12-31'` → keeps the records whose date is from 1 January to 31 December 2024. The dates are text, so they go in single quotes.

There are **929** games: the same number we found for 2024 when we counted [games per year](../insights/08_summarising_groups.md#games-per-year) in Polars.

!!! warning "Dates must be written year first"
    This only works because our dates are written year first. In our original CSV file, dates were written like `Feb 24, 2017`. As text, `Apr 1, 2025` comes before `Feb 24, 2017`, because "A" comes before "F". That's why we turned the dates into real dates in [Fixing Our Data](../cleaning/06_fixing_data.md#text-into-dates), and why ***steam.db*** stores them as `2017-02-24`.

## Check your SQL

Answer these questions with new SQL cells in ***sql_intro.py***. Remember to choose `conn` in each one.

1. Which Indie games cost more than $30? Show their name, developers and price.
2. Which games have "Portal" in their name?
3. How many games were released in 2020?
4. Which games cost from $1 to $2 and have a review score of at least 97?
5. Which games were made by Valve or Team Cherry and were released before 2005? Check your brackets.
