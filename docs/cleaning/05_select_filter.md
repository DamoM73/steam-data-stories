# 5. Choosing Columns and Rows

!!! learn "In this lesson we will learn"
    - why cleaning is the Behind the Scenes stage of our story
    - how to keep only the columns we need with `select`
    - how to keep only the rows we need with `filter`
    - how to combine conditions with `&` and `|`
    - how to find the Indie games

!!! terms "Terminology"
    - **data cleaning** – finding and fixing problems in data so we can trust the results.
    - **expression** – a description of what to do with a column, such as `pl.col("Price") > 0`, which Polars works out for every row at once.

## Introduction

Welcome to **Behind the Scenes**. Our audience will never see the next two lessons, but this is where we earn their trust. If our data is wrong, every chart and every claim in our story is wrong too.

Finding and fixing problems in data so we can trust it is called **data cleaning**. The first job is to cut our data down to what we need. We have 12 columns and 10,250 rows, but our question only needs some of them. Smaller tables are easier to read and easier to check.

## Choosing columns

Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Then add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/05_select_filter/cell13.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–12** → use `select` to make a new DataFrame from `public_games` that holds only the 10 columns we list, in the order we list them, and store it in a variable called `selected`.
    - **line 13** → shows `selected` as the cell's output.

The table now has **10** columns instead of 12, and still has all 10,250 rows. `select` never changes the number of rows: it only chooses columns. We left out `Achievements` and `Publishers`, because our example question doesn't need them.

!!! tip "Building on the last variable"
    We started from `public_games`, the version without support emails from Lesson 4. Each cleaning step starts from the variable the step before made, and gives its result a new name. That way we can always look back at any earlier version.

## Choosing rows

To keep only some rows, we use `filter` with a condition. Rows where the condition is `True` are kept.

Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/05_select_filter/cell14.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change `> 0` to `== 0` to find the free games instead. How many are there?

??? note "Code explanation"
    - **line 1** → keeps only the rows of `selected` where the `Price` is greater than 0, and stores them in `paid_games`.
    - **line 2** → shows the number of rows in `paid_games`, using `height`.

The output is **8839**: that's how many games cost money. The other 1,411 are free.

`pl.col("Price")` means "the `Price` column". It's called an **expression**: a description of what to do with a column, which Polars works out for every row at once. We'll use `pl.col` in almost every cell from now on.

## Combining conditions

What if we want paid games that are also very popular? We need two conditions at once. Add a new cell and type the code below, exactly as it is, then run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/05_select_filter/cell15a.py"
```

??? note "Code explanation"
    - **lines 1–3** → try to keep the rows of `selected` that cost more than 0 and have more than 10,000 recommendations.
    - **line 4** → shows the number of rows in `popular_paid`.

Instead of a number, we get an error:

``` { .text .error linenums="1" }
TypeError: the truth value of an Expr is ambiguous
```

- **line 1** → `TypeError` means Python tried to use a value in a way its type doesn't allow. Here, it tried to treat an expression as a single `True` or `False`.

The problem is the order Python works things out. Python does `&` **before** `>`, so it tried to work out `0 & pl.col("Recommendations")` first, which makes no sense. We fix it by putting each condition in its own brackets, so each comparison happens first.

Change the cell to match the code below and run it again.

```python linenums="1" title="clean_steam.py" hl_lines="2"
--8<-- "examples/cleaning/05_select_filter/cell15.py"
```

??? note "Code explanation"
    - **line 2** → puts each condition in its own brackets and joins them with `&`, so a row is kept only if **both** conditions are `True`.

The output is **1315**: only 1,315 paid games have more than 10,000 recommendations.

There are three ways to combine conditions:

| Operator | Meaning | A row is kept when |
| :-- | :-- | :-- |
| `&` | and | both conditions are `True` |
| `|` | or | at least one condition is `True` |
| `~` | not | the condition is `False` |

!!! warning "Use & and |, not and and or"
    In normal Python we write `and` and `or`. Polars expressions need `&` and `|` instead, and each condition needs its own brackets.

!!! primm "PRIMM"
    Time to **modify** the code. Change it to find games that are free **or** have more than 100,000 recommendations. How many are there?

## Finding the Indie games

Our example question compares Indie games with all the other games. In Lesson 3 we counted the Indie games with `str.contains`. Now let's keep them as their own DataFrame. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/05_select_filter/cell16.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Put `~` in front of `pl.col` to find the games that **aren't** Indie. How many are there?

??? note "Code explanation"
    - **line 1** → keeps only the rows of `selected` whose `Genres` text contains `Indie`, and stores them in `indie_games`.
    - **line 2** → shows `indie_games` as the cell's output.

<!-- SCREENSHOT: assets/l05_indie_games.png — the indie_games table in marimo, 6,243 rows -->

The table has **6243** rows, which matches our count from Lesson 3. Scroll across to the `Genres` column: every row has `Indie` somewhere in its list of genres.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 5: Columns and rows` and record our answers under it.

1. List the columns our own question needs. If any of them isn't in `selected`, add it to the `select` cell. Don't remove any columns, because the next lessons use them.
2. Write a `filter` that finds the rows our question is about, such as games from one genre or one price range. Record the condition and how many rows it keeps.
3. If our question compares two groups, write one `filter` for each group, and record how many rows are in each.
