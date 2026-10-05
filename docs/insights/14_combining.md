# 14. Combining Datasets

!!! learn "In this lesson we will learn"
    - how to join two DataFrames with `join`
    - why join keys must have the same data type
    - why we join on IDs rather than names
    - how to turn text into date-times and change time zones
    - how to remove duplicate rows with `unique`
    - how to calculate within each group with `over`

## Introduction

We now have two datasets: `story_games`, which tells us each game's name and whether it has a PvE option, and `history`, which tells us how many people played each game every hour. Neither one can answer our question alone. We need to **combine** them, so every hour of history knows its game's name and PvE option.

Before we combine them, the history needs some Behind the Scenes work of its own. Real stories often loop back like this: new data means new cleaning.

## Joining DataFrames

A **join** combines two DataFrames by matching the values in a **key** column that both of them have. For every row in the first DataFrame, Polars finds the row in the second with the same key, and puts their columns side by side.

Both of our DataFrames have an `AppID` column, so it should be our key. Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/14_combining/story18a.py"
```

??? note "Code explanation"
    - **line 1** → tries to join `history` and `story_games`, matching rows where `AppID` is the same, using `join`.

We get an error:

``` { .text .error linenums="1" }
SchemaError: datatypes of join keys don't match - `AppID`: str on left does not match `AppID`: i64 on right (and no other type was available to cast to)
```

- **line 1** → `SchemaError` means there's a problem with the columns' data types. In `history`, `AppID` is text (`str`), but in `story_games` it's a whole number (`i64`). The text `"1808500"` and the number `1808500` aren't equal, so Polars won't try to match them.

We'll fix the type in a moment. Delete this cell before moving on.

### Why not join on names?

What if we joined on `Name` instead? Let's try it with `games`, our big table, to add each game's release date to `story_games`. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/14_combining/story18b.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → joins `story_games` with the `Name` and `Release date` columns of `games`, matching rows where `Name` is the same. `how="left"` keeps every row of `story_games`, even ones with no match.

| AppID | Name | PvE | Release date |
| :-- | :-- | :-- | :-- |
| 1808500 | ARC Raiders | No | 2025-10-30 |
| 3065800 | Marathon | No | 2026-03-05 |
| 3932890 | Escape from Tarkov | Yes | 2025-11-15 |
| 2479810 | Gray Zone Warfare | Yes | 2024-04-30 |
| 2073620 | Arena Breakout: Infinite | Added later | 2025-09-15 |
| 3167020 | Escape from Duckov | Single-player | null |

Escape from Duckov gets a null, because its name in the data is `Escape From Duckov`, with a capital **F**, as we found in Lesson 8. And if two games shared a name, like the two games called `2048`, the join would match both. AppIDs don't have either problem: each one belongs to exactly one game. **Always join on an ID when there is one.**

There are four kinds of join:

| `how=` | Keeps |
| :-- | :-- |
| `"inner"` | only rows that match in both DataFrames (the default) |
| `"left"` | every row of the first DataFrame, with nulls where there's no match |
| `"right"` | every row of the second DataFrame |
| `"full"` | every row of both |

## Cleaning the history

Our history has three more problems to fix before we can join it:

1. `AppID` is text
2. `added` is text, not a date and time
3. some hours might appear twice

Let's check the third one first. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/14_combining/story18.py"
```

??? note "Code explanation"
    - **line 1** → bundles `AppID` and `added` together for each row, using `pl.struct`, keeps the rows where that pair appears more than once, and counts them.

The output is **251**. Some hours were recorded twice for the same game, so if we didn't remove them, those hours would count twice.

Now let's fix all three problems in one cell. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/14_combining/story19.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → opens a bracket for our method chain, and will store the result in `clean_history`.
    - **line 2** → starts changing columns of `history`.
    - **line 3** → casts `AppID` to a whole number, so it matches `story_games`.
    - **line 4** → starts with the `added` column.
    - **line 5** → turns its text into a **datetime**: a date and a time together.
    - **line 6** → tells Polars the times are in **UTC**, the world's standard time zone, which is what the API uses.
    - **line 7** → converts the times to Brisbane time, so they match our clocks in Queensland.
    - **line 8** → names the new column `Time`.
    - **line 9** → closes the `with_columns` brackets.
    - **line 10** → removes rows with the same `AppID` and `Time` as an earlier row, using `unique`.
    - **line 11** → sorts the rows by game, then by time.
    - **line 12** → closes the bracket we opened on line 1.
    - **line 13** → shows `clean_history` as the cell's output.

<!-- SCREENSHOT: assets/l14_clean_history.png — clean_history showing the Time column in AEST -->

`clean_history` has **59700** rows: 128 fewer than before. That's less than 251, because `is_duplicated` counts every copy of a repeated row, including the first one, and `unique` keeps the first one. The first row is ARC Raiders' first hour: **11 pm on 30 October 2025**, Brisbane time, with 159,981 players.

!!! tip "Why Brisbane time?"
    Queensland doesn't use daylight saving, so Brisbane time is always 10 hours ahead of UTC. Other states would need a time zone like `Australia/Sydney`, which changes by an hour in summer.

## Checking for gaps

The history should have one row every hour. If the API missed some hours, our story could miss a busy moment. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/14_combining/story20.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change `hours=3` to `hours=24`. How many gaps are longer than a day?

??? note "Code explanation"
    - **lines 1–2** → add a column called `Gap` that holds the time since the previous row, using `diff`. `over("AppID")` does this separately for each game, so the first row of one game isn't compared with the last row of another.
    - **line 3** → keeps only the rows where the gap is longer than 3 hours, and stores them in `gaps`.
    - **line 4** → shows the `AppID`, `Time` and `Gap` columns of `gaps`.

<!-- SCREENSHOT: assets/l14_gaps.png — the gaps table -->

There are **61** gaps longer than 3 hours. The longest is about two and a half days, in September 2026. Look at the times: the same gaps appear for several games at once. That tells us the API stopped collecting for a while, rather than the games disappearing from Steam.

Our question is about months, and the biggest gap is less than three days, so we'll keep going. This is one more decision for our data story notes.

## Players per month

Hourly data is too detailed for our story. Players go up and down every day, as people wake up and go to sleep around the world. To see the long-term drop, we'll find each game's **busiest hour in each month** since launch, and compare it to the game's busiest month.

Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/14_combining/story21.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → opens a bracket for our method chain, and will store the result in `monthly`.
    - **line 2** → starts adding a column to `clean_history`.
    - **lines 3–6** → for each row, work out how many days have passed since that game's first hour, divide by 30 and throw away the remainder with `//`, then name the result `Month`. Month 0 is a game's first 30 days, month 1 is the next 30, and so on.
    - **line 7** → closes the `with_columns` brackets.
    - **line 8** → splits the rows into one group for each game and month.
    - **line 9** → finds the most players in any hour of each group, and names it `Peak players`.
    - **lines 10–14** → divide each month's peak by that game's highest monthly peak, multiply by 100 and round, then name the result `Percent of peak`.
    - **line 15** → joins the game's `Name` and `PvE` columns from `story_games`, matching on `AppID`, which works now that both are whole numbers.
    - **line 16** → sorts by game, then by month.
    - **line 17** → closes the bracket we opened on line 1.
    - **line 18** → shows `monthly` as the cell's output.

<!-- SCREENSHOT: assets/l14_monthly.png — the monthly table for ARC Raiders -->

`monthly` has **86** rows, one for each month of each game. Here's ARC Raiders:

| Month | Peak players | Percent of peak |
| --: | --: | --: |
| 0 | 477399 | 100.0 |
| 1 | 438255 | 91.8 |
| 2 | 466031 | 97.6 |
| 3 | 374932 | 78.5 |
| 4 | 248222 | 52.0 |
| 5 | 157405 | 33.0 |
| 6 | 135443 | 28.4 |

!!! tip "group_by or over?"
    Both work with groups, but they give back different shapes. `group_by` and `agg` **shrink** each group to one row. `over` does a calculation for each group but **keeps every row**, so we can compare each row with its own group, like each month with its game's best month.

!!! tip "Why percent of peak?"
    ARC Raiders peaked at 477,399 players, and Gray Zone Warfare at about 71,000. Comparing raw player numbers would just tell us ARC Raiders is bigger. Turning every game's numbers into a percentage of its own peak lets us compare how quickly each one **dropped**, whatever its size.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 14: Combining data` and record our answers under it.

1. If our question uses two datasets, write down the key we'll join them on and check it has the same data type in both.
2. Write down the extra cleaning decisions from this lesson: duplicates, gaps and time zones. Did any of them affect our question?
3. Record the summary table our question needs, like `monthly`, and the most important numbers in it.
