# 9. Making New Columns

!!! learn "In this lesson we will learn"
    - what the Rising Insights stage of our story does
    - how to start a second notebook and load our clean data
    - how to calculate a new column from other columns
    - the difference between NaN and null
    - how to sort values into groups with `pl.when`

## Introduction

Welcome to **Rising Insights**. Our data is clean, so now we can start finding things out. Each Rising Insights lesson adds one more piece of evidence to our story, building up to the Aha Moment.

Often the column we need isn't in the data yet. Steam gives us the number of positive and negative reviews, but not a review **score**. It gives us a full release date, but our question might be about years. In this lesson we'll make the columns we need from the ones we have.

## A new notebook

We'll do Lessons 9 to 16 in a second notebook, ***steam_story.py***, that starts from the clean data we saved in Lesson 8. Keeping cleaning and storytelling in separate notebooks means each one stays short enough to follow.

1. If marimo is still running, click in the VS Code terminal, press ++ctrl+c++, type `y` and press ++enter++.
    - **Why:** marimo can only edit one notebook at a time from one terminal.
    - **Expected result:** the terminal shows the `(.venv)` prompt again.
2. In the terminal, type the command below and press ++enter++.

    ```text
    marimo edit steam_story.py
    ```

    - **Why:** this creates and opens our second notebook.
    - **Expected result:** a new browser tab opens with an empty notebook, and ***steam_story.py*** appears in VS Code's Explorer panel.

In the empty cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/09_new_columns/story01.py"
```

??? note "Code explanation"
    - **line 1** → imports Polars with the short name `pl`.

Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/09_new_columns/story02.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → loads ***clean_games.parquet*** into a DataFrame called `games`.
    - **line 2** → loads ***story_games.parquet*** into a DataFrame called `story_games`.
    - **line 3** → shows `games` as the cell's output.

`games` has **138268** rows and **15** columns, and it loaded almost instantly. Check the column types in the table: `Release date` is still a date, and `Genres` is still a list. Parquet kept all our cleaning work.

!!! tip "games in two notebooks"
    `games` in this notebook is our clean data, but `games` in ***clean_steam.py*** is the raw data. That's fine: each notebook has its own variables, so the two can't clash.

## Calculating a review score

A game with 900 positive and 100 negative reviews, and a game with 9 positive and 1 negative, are both liked by 90% of reviewers. A **review score**, the percentage of reviews that are positive, lets us compare games of any size.

Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/09_new_columns/story03a.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → starts making a new version of `games` with an extra column, and will store it in `scored`.
    - **line 2** → divides `Positive` by the total number of reviews, `Positive` plus `Negative`, and multiplies by 100 to make a percentage.
    - **line 3** → rounds the result to 1 decimal place.
    - **line 4** → names the new column `Review score`.
    - **line 5** → closes the `with_columns` brackets.
    - **line 6** → shows the `Name`, `Positive`, `Negative` and `Review score` columns of `scored`.

<!-- SCREENSHOT: assets/l09_nan.png — Review score column showing NaN for a game with 0 positive and 0 negative -->

Most rows have a sensible score, like **98.8**. But look at `Black Dragon Mage Playtest`: it has 0 positive and 0 negative reviews, and its score is **NaN**.

### NaN is not null

**NaN** stands for **not a number**. It's what we get when a calculation has no sensible answer, like 0 divided by 0. It looks like a missing value, but Polars treats it differently from a null:

| | null | NaN |
| :-- | :-- | :-- |
| means | there's no value | the calculation has no answer |
| skipped by `mean` and `median`? | yes | no: the answer becomes NaN too |
| counted by `null_count`? | yes | no |

56,438 games have no reviews at all, so we'd get a lot of NaNs. A game with no reviews doesn't have a score of NaN; it just doesn't have a score. So we'll turn the NaNs into nulls. Change the cell to match the code below and run it.

```python linenums="1" title="steam_story.py" hl_lines="4"
--8<-- "examples/insights/09_new_columns/story03b.py"
```

??? note "Code explanation"
    - **line 4** → replaces every NaN in the new column with `None`, which Polars stores as a null, using `fill_nan`.

`Black Dragon Mage Playtest` now has a null review score.

## Years and price bands

Two more columns will be useful for comparing groups of games in the next lesson: the release **year**, and a **price band** that sorts every game into one of four groups. Change the cell to match the code below and run it.

```python linenums="1" title="steam_story.py" hl_lines="6-14 16-18"
--8<-- "examples/insights/09_new_columns/story03.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Add a fifth band, `$60 and over`, for the most expensive games. Where does the new `when` need to go?

??? note "Code explanation"
    - **line 6** → gets the year from each `Release date`, using `dt.year`, and names the new column `Release year`.
    - **line 7** → starts a `pl.when` chain, which works like `if` and `elif` in Python, and tests whether `Price` is 0.
    - **line 8** → if it is, the value is the text `Free`. `pl.lit` means a **literal** value: the same text for every matching row, rather than a column name.
    - **lines 9–10** → otherwise, if `Price` is under 10, the value is `Under $10`.
    - **lines 11–12** → otherwise, if `Price` is under 30, the value is `$10 to $30`.
    - **line 13** → for every other price, the value is `$30 and over`, like `else` in Python.
    - **line 14** → names the new column `Price band`.
    - **lines 16–18** → show the `Name`, `Review score`, `Release date`, `Release year`, `Price` and `Price band` columns of `scored`.

<!-- SCREENSHOT: assets/l09_scored.png — scored with Review score, Release year and Price band columns -->

Every game now has a `Release year` and a `Price band`. A $5.24 game is `Under $10`, and a $13.99 game is `$10 to $30`.

!!! tip "Order matters in pl.when"
    Polars checks each `when` from top to bottom and stops at the first one that's true, just like `if` and `elif`. A $5 game passes both `< 10` and `< 30`, but it gets `Under $10` because that test comes first.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 9: New columns` and record our answers under it.

1. Write down one new column our question needs that isn't in the data, and how we could calculate it from the columns we have.
2. Add it to the `scored` cell (or make a new cell with a new variable), run it, and check a few rows by hand to make sure the values are right.
3. Write down any NaNs or nulls our new column has, and what they mean.
