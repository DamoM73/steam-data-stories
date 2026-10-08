# 6. Fixing Our Data

!!! learn "In this lesson we will learn"
    - how to turn text into dates with `str.to_date`
    - how to turn values that mean "missing" into nulls
    - why we identify games by AppID, not name
    - how to save our clean data

!!! terms "Terminology"
    - **format code** – a pattern such as `%b %d, %Y` that tells Polars how dates are written in text.
    - **Parquet** – a file format for tables that saves each column's data type along with the data.

## Introduction

In Lesson 3 we found two problems in our data. `Release date` holds dates stored as text, so they sort in alphabetical order instead of by date. And most `Metacritic score` values are 0, which really means "no score". In this lesson we'll fix both, check for repeated games, and save our clean data so our story notebook can use it.

## Text into dates

Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_fixing_data/cell17a.py"
```

??? note "Code explanation"
    - **line 1** → starts making a new version of `selected` with changed columns, using `with_columns`, and will store it in `dated`.
    - **line 2** → tries to turn the text in `Release date` into dates, using `str.to_date`.
    - **line 3** → closes the `with_columns` brackets.
    - **line 4** → shows `dated` as the cell's output.

We get an error:

``` { .text .error linenums="1" }
ComputeError: could not find an appropriate format to parse dates, please define a format
```

- **line 1** → `ComputeError` means Polars couldn't finish a calculation. The message says it couldn't work out how our dates are written, so we need to tell it.

Polars recognises dates written like `2017-02-24`, but ours are written like `Feb 24, 2017`. We describe that pattern with a **format code**:

| Part of the date | Format code | Example |
| :-- | :-- | :-- |
| short month name | `%b` | `Feb` |
| day of the month | `%d` | `24` |
| four-digit year | `%Y` | `2017` |

Everything that isn't a format code, like the space and the comma, has to match the text exactly. So `Feb 24, 2017` has the format `%b %d, %Y`.

Change the cell to match the code below and run it again.

```python linenums="1" title="clean_steam.py" hl_lines="2"
--8<-- "examples/cleaning/06_fixing_data/cell17.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 2** → turns the text in `Release date` into dates, using the format `%b %d, %Y`. Because the new column has the same name as the old one, it replaces it.

<!-- SCREENSHOT: assets/l06_dates.png — the dated table with Release date shown as dates (2019-09-05 style) -->

The `Release date` column now shows dates like `2019-09-05`, and its data type is **date**. Every one of the 10,250 dates converted.

!!! tip "One format for every row"
    `str.to_date` uses the same format for every row. If even one row were written differently, like `24 Feb 2017`, Polars would stop with an error. That's a useful check: it proves every date in our data is written the same way.

Now let's check that the dates sort properly. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_fixing_data/cell18.py"
```

??? note "Code explanation"
    - **line 1** → shows the earliest and the latest `Release date` in `dated`, using `min` and `max`.

The output shows **30 June 1997** and **18 December 2025**. In Lesson 3, when the dates were text, the "smallest" was `Apr 1, 1999` and the "largest" was `Sep 9, 2024`. Now they really are the oldest and newest games.

## Values that mean "missing"

Remember from Lesson 4 that a **null** means a value is missing. In Lesson 3 we found that 7,317 games have a `Metacritic score` of 0. Metacritic scores go from 1 to 100, so a 0 means the game wasn't reviewed. If we left those 0s in, they'd drag down every average we work out.

Before we change anything, let's think about the other number columns too:

| Column | Is 0 real? | Why |
| :-- | :-- | :-- |
| `Price` | yes | free games really do cost $0 |
| `Recommendations` | yes | a game can really have no recommendations |
| `Metacritic score` | no | scores go from 1 to 100, so 0 means "no score" |

So we only need to fix `Metacritic score`. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_fixing_data/cell19.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → starts making a new version of `dated` with a changed column, and will store it in `clean_games`.
    - **line 2** → replaces every 0 in `Metacritic score` with `None`, which Polars stores as a null.
    - **line 3** → closes the `with_columns` brackets.
    - **line 4** → counts the nulls in every column of `clean_games`.

<!-- SCREENSHOT: assets/l06_null_count.png — null_count output showing 7317 in Metacritic score -->

Every column has 0 nulls, except `Metacritic score`, which now has **7317**. The hidden gaps are now real gaps that Polars knows about.

!!! tip "Why nulls are better than 0s"
    Polars skips nulls when it works out things like `mean` and `median`. So the average `Metacritic score` is now the average of the games that were actually reviewed, instead of being dragged down by thousands of made-up zeros.

!!! warning "Cleaning is a judgement call"
    We decided that 0 means "missing" for `Metacritic score` but not for `Price`. Decisions like this change our results, so good data scientists write them down where others can see them. That's what the **Our data story** section is for.

## Repeated names

In Lesson 1 we said two games can share a name but never an AppID. Let's check. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_fixing_data/cell20.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → keeps only the rows of `clean_games` whose `Name` appears more than once, using `is_duplicated`, then sorts them by `Name` so games with the same name sit together.

<!-- SCREENSHOT: assets/l06_repeated_names.png — repeated names sorted, showing the two Alpha Protocol rows -->

**115** rows share their name with another row. Look at the two rows for `Alpha Protocol™`: they have the same release date and developer, but different AppIDs and different numbers of reviews. Some games have more than one page on the Steam store, such as a separate page for a special edition or for players in another region, and each page collects its own reviews.

So these rows aren't mistakes we need to delete. But they show why we must never use `Name` to identify a game. Let's check that every AppID really is different. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_fixing_data/cell21.py"
```

??? note "Code explanation"
    - **line 1** → checks whether each value in the `AppID` column appears only once, using `is_unique`, then uses `all` to give back one `True` only if every row passed.

The output is **True**. Every game has its own AppID.

## Saving our clean data

Our cleaning is done. Rather than run every cleaning cell again in our next notebook, we'll save the result. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_fixing_data/cell22.py"
```

??? note "Code explanation"
    - **line 1** → saves `clean_games` as a **Parquet** file called ***clean_games.parquet*** in our ***data*** folder.

Check VS Code's Explorer panel: the new file is in our ***data*** folder.

!!! tip "Why Parquet and not CSV?"
    A **Parquet** file stores each column's data type along with the data. When we load it again, our dates are still dates and our nulls are still nulls, so we don't have to fix them a second time.

!!! warning "Re-run the saving cell after changes"
    If we change any cleaning cell later, the Parquet file won't update by itself. Run the saving cell again so our story notebook gets the new version.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 6: Clean data` and record our answers under it.

1. For each column our question needs, write down whether 0 is a real value or means "missing", and why.
2. Write down every cleaning decision we made in Lessons 4 to 6, and why. Start each one with "We decided…". This becomes the "How we got our data" part of our finished story.
3. Write down one thing about our data that our audience should know, because it limits what we can claim.
