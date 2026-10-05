# 5. Choosing Columns and Rows

!!! learn "In this lesson we will learn"
    - why cleaning is the Behind the Scenes stage of our story
    - how to keep only the columns we need with `select`
    - how to keep only the rows we need with `filter`
    - how to combine conditions with `&` and `|`
    - how to find our story's games with `is_in`

## Introduction

Welcome to **Behind the Scenes**. Our audience will never see the next four lessons, but this is where we earn their trust. If our data is wrong, every chart and every claim in our story is wrong too.

The first job is to cut our data down to size. We have 37 columns and 138,270 rows, but our question only needs some of them. Working with less data makes our notebook faster and our tables easier to read.

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
    - **lines 1–15** → use `select` to make a new DataFrame from `public_games` that holds only the 13 columns we list, in the order we list them, and store it in a variable called `selected`.
    - **line 16** → shows `selected` as the cell's output.

The table now has **13** columns instead of 37, and still has all 138,270 rows. `select` never changes the number of rows: it only chooses columns.

!!! tip "Building on the last variable"
    Notice that we started from `public_games`, the version without contact details from Lesson 4. Each cleaning step starts from the variable the previous step made, and gives its result a new name. That way we can always look back at any earlier version.

## Choosing rows

To keep only some rows, we use `filter` with a **condition**: a test that is `true` or `false` for each row. Rows where the condition is `true` are kept.

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

The output is **109764**: that's how many games cost money.

`pl.col("Price")` means "the `Price` column". It's called an **expression**: a description of what to do with a column that Polars works out for every row at once. We'll use `pl.col` in almost every cell from now on.

Conditions use the comparison operators we already know from Python:

| Operator | Meaning |
| :-- | :-- |
| `==` | equal to |
| `!=` | not equal to |
| `>` and `>=` | greater than, and greater than or equal to |
| `<` and `<=` | less than, and less than or equal to |

## Combining conditions

What if we want paid games that are also popular? We need two conditions at once. Add a new cell and type the code below, exactly as it is, then run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/05_select_filter/cell15a.py"
```

??? note "Code explanation"
    - **lines 1–3** → try to keep the rows of `selected` that cost more than 0 and have more than 1,000 recommendations.
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
    - **line 2** → puts each condition in its own brackets and joins them with `&`, so a row is kept only if **both** conditions are `true`.

The output is **6077**: only 6,077 paid games have more than 1,000 recommendations.

There are three ways to combine conditions:

| Operator | Meaning | A row is kept when |
| :-- | :-- | :-- |
| `&` | and | both conditions are `true` |
| `|` | or | at least one condition is `true` |
| `~` | not | the condition is `false` |

!!! warning "Use & and |, not and and or"
    In normal Python we write `and` and `or`. Polars expressions need `&` and `|` instead, and each condition needs its own brackets.

!!! primm "PRIMM"
    Time to **modify** the code. Change it to find games that are free **or** have more than 10,000 recommendations. How many are there?

## Finding our story's games

Our example story only needs six games. Their AppIDs are in the `story_games` DataFrame we made in Lesson 3. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/05_select_filter/cell16.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → starts filtering `selected` and will store the result in `story_rows`.
    - **line 2** → gets the `AppID` column from `story_games`, turns it into a Python list with `to_list`, then keeps only the rows whose `AppID` is in that list, using `is_in`.
    - **line 3** → closes the `filter` brackets.
    - **line 4** → shows `story_rows` as the cell's output.

<!-- SCREENSHOT: assets/l05_story_rows.png — the six story_rows in marimo's table viewer -->

All six of our games are there. Scroll across and look closely at their columns:

1. Five of the six have `Peak CCU` of 0 and `Metacritic score` of 0.
2. Arena Breakout: Infinite has `0 - 0` owners and 0 recommendations, even though tens of thousands of people play it.
3. `Release date` is still text, like `Oct 30, 2025`.

Some of these values must be wrong, or really mean "no data". We'll deal with them over the next two lessons.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 5: Columns and rows` and record our answers under it.

1. List the columns our own question needs. If any of them isn't in `selected`, add it to the `select` cell. Don't remove any columns, because the next lessons use them.
2. Write a `filter` that finds the rows our question is about, such as games from one genre, one year or one price range. Record the condition and how many rows it keeps.
3. If our question compares two groups, write one `filter` for each group, and record how many rows are in each.
