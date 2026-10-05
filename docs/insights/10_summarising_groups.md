# 10. Summarising Groups

!!! learn "In this lesson we will learn"
    - how to split data into groups with `group_by`
    - how to summarise each group with `agg`
    - how to count rows with `pl.len`
    - when to use the mean and when to use the median
    - how to group by the items in a list

## Introduction

A table of 138,268 games can't tell a story by itself. Our audience needs a few clear numbers: how many games came out each year, or how the cheap games compare with the expensive ones. To get those numbers, we **summarise** groups of rows.

Every summary in this lesson follows the same three steps, often called **split, apply, combine**:

1. **split** the rows into groups, like one group for each release year
2. **apply** a calculation to each group, like counting its games
3. **combine** the answers into a new, much smaller table, with one row per group

## Games per year

Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/10_summarising_groups/story04.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → opens a bracket so our method chain can go over several lines, and will store the result in `per_year`.
    - **line 2** → **splits** the rows of `scored` into groups, one for each different `Release year`.
    - **line 3** → starts `agg`, short for **aggregate**, which **applies** calculations to each group.
    - **line 4** → counts the rows in each group with `pl.len`, and names the answer `Games`.
    - **line 5** → finds the median `Price` of each group, and names it `Median price`.
    - **line 6** → closes the `agg` brackets, which **combines** the answers into one table.
    - **line 7** → sorts the table by `Release year`, because `group_by` doesn't keep the groups in any order.
    - **line 8** → closes the bracket we opened on line 1.
    - **line 9** → shows `per_year` as the cell's output.

<!-- SCREENSHOT: assets/l10_per_year.png — per_year table, scrolled to show 2020 to 2026 -->

There's one row per year: 30 rows, from 1997 to 2026. Scroll down to the end:

- **24,007** games came out in 2025, more than in any other year
- 2026 shows **19,705**, but our data was collected in October, so 2026 isn't finished yet
- the median price has been **$1.99** for most recent years, but rose to $2.99 in 2025

!!! warning "Watch out for part years"
    It would be easy to say "fewer games came out in 2026 than in 2025". But 2026 only has nine months of data. Comparing a part year with full years is a common mistake in data stories, so we'll leave 2026 out when we look at trends in Lesson 12.

## Mean or median?

Let's compare the four price bands from Lesson 9. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/10_summarising_groups/story05.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → opens a bracket for our method chain, and will store the result in `per_band`.
    - **line 2** → splits the rows of `scored` into one group for each `Price band`.
    - **line 3** → starts `agg`.
    - **line 4** → counts the games in each band.
    - **line 5** → finds the median `Recommendations` of each band.
    - **line 6** → finds the mean `Recommendations` of each band, rounded to a whole number.
    - **line 7** → closes the `agg` brackets.
    - **line 8** → sorts the bands from most games to fewest.
    - **line 9** → closes the bracket we opened on line 1.
    - **line 10** → shows `per_band` as the cell's output.

| Price band | Games | Median recommendations | Mean recommendations |
| :-- | --: | --: | --: |
| Under $10 | 95302 | 0.0 | 651.0 |
| Free | 28504 | 0.0 | 674.0 |
| $10 to $30 | 13150 | 0.0 | 2085.0 |
| $30 and over | 1312 | 0.0 | 6332.0 |

The **median** is 0 for every band, but the **mean** is in the hundreds or thousands. How can both be right?

About 85% of all games have no recommendations at all, so the middle value of each band is 0. A small number of hit games have hundreds of thousands of recommendations, or even millions, and they pull the mean up. When the data is **skewed** like this, with a few huge values, the mean and median tell very different stories:

- the **median** describes a **typical** game: it gets no recommendations
- the **mean** is pulled towards the **hits**: expensive bands have more big hits

Neither is wrong, but we need to choose the one that matches what we want to say, and tell our audience which one we used.

!!! tip "Other ways to summarise"
    Inside `agg` we can use `mean`, `median`, `min`, `max`, `sum`, `std` and `count` on any column, and `pl.len()` to count rows. We can use as many as we like, each with its own `alias`.

## Grouping by genre

A game can have several genres, so first we explode the `Genres` lists, like we did in Lesson 8. Then each genre becomes a group. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/10_summarising_groups/story06.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. There's a `null` genre in the top 10, for games with no genre. Add `.drop_nulls("Genres")` after the explode, so it's left out. Which genre takes its place?

??? note "Code explanation"
    - **line 1** → opens a bracket for our method chain, and will store the result in `per_genre`.
    - **line 2** → explodes the `Genres` lists of `scored`, so a game with three genres becomes three rows.
    - **line 3** → splits the rows into one group for each genre.
    - **line 4** → starts `agg`.
    - **line 5** → counts the games in each genre.
    - **line 6** → finds the median review score of each genre.
    - **line 7** → closes the `agg` brackets.
    - **line 8** → sorts the genres from most games to fewest.
    - **line 9** → keeps only the first 10 rows, using `head`.
    - **line 10** → closes the bracket we opened on line 1.
    - **line 11** → shows `per_genre` as the cell's output.

<!-- SCREENSHOT: assets/l10_per_genre.png — per_genre top 10 table -->

Indie is the biggest genre by far, with 92,088 games. The median review scores are close together: from **75.6** to **83.3**. Casual games have the highest median score in the top 10.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 10: Summaries` and record our answers under it.

1. Write a `group_by` that summarises the groups our question is about. Record the table it makes, or the most important rows.
2. Decide whether the mean or the median suits our question better, and write down why.
3. Write one sentence that states a finding, using a number from our summary. For example: "In 2025, 24,007 games came out on Steam, more than in any year before."
