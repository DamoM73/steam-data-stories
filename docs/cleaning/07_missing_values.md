# 7. Missing and Impossible Values

!!! learn "In this lesson we will learn"
    - what a null is, and how to count them with `null_count`
    - how to spot values that really mean "missing"
    - how to replace them with nulls using `replace`
    - how to find duplicates
    - how to write checks that prove our data makes sense

## Introduction

Real data always has gaps. Sometimes a value is missing and the data says so. Sometimes it's missing and the data **doesn't** say so: someone typed 0, or a date that can't be right. The second kind is more dangerous, because it quietly changes our results. A 0 for `Peak CCU` drags down the average number of players, even though it really means "we don't know".

In this lesson we'll find both kinds, decide what to do with each, and write down our decisions.

## Counting nulls

A **null** is Polars' way of saying "no value here". Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/07_missing_values/cell19.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → counts the nulls in every column of `typed`, and shows the counts as a table with one row.

<!-- SCREENSHOT: assets/l07_null_count.png — the null_count output for typed -->

Scroll across the output. Most columns have no nulls, but:

- `Name` has **1**: one game has no name at all
- `Genres` has **8407**, `Categories` **8966** and `Tags` **56052**: lots of games have no labels

But we know there are more gaps than this. In Lesson 3 we saw that the median `Peak CCU` and `Metacritic score` were both 0, and that 38,991 games had `0 - 0` owners. None of those show up here, because 0 isn't a null.

## Hidden missing values

We need to decide, column by column, whether 0 is a real value or means "missing":

| Column | Is 0 real? | Why |
| :-- | :-- | :-- |
| `Price` | yes | free games really do cost $0 |
| `Recommendations` | yes | a new or unknown game can really have none |
| `Peak CCU` | no | most 0s are games SteamSpy has no data for, including ARC Raiders |
| `Metacritic score` | no | scores go from 1 to 100, so 0 means the game wasn't reviewed |
| `Owners max` | no | a game on sale with a maximum of 0 owners means SteamSpy had no estimate |

Now let's replace the 0s that mean "missing" with nulls. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/07_missing_values/cell20.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → starts making a new version of `typed` with changed columns, and will store it in `missing`.
    - **line 2** → replaces every 0 in `Peak CCU` with `None`, which Polars stores as a null.
    - **line 3** → does the same for `Metacritic score`.
    - **line 4** → does the same for `Owners max`.
    - **line 5** → closes the `with_columns` brackets.
    - **line 6** → counts the nulls in every column of `missing`.

Now the hidden gaps show up: **119316** nulls in `Peak CCU`, **134010** in `Metacritic score` and **38991** in `Owners max`.

That's a big result for our story. `Peak CCU` is missing for 86% of games, and `Metacritic score` for 97%. Any question built on those columns would be built on very little data.

!!! tip "Why nulls are better than 0s"
    Polars skips nulls when it calculates things like `mean` and `median`. So once the fake 0s are nulls, the average `Peak CCU` is the average of the games we actually know about, instead of being dragged down by more than 100,000 made-up zeros.

!!! warning "Cleaning is a judgement call"
    Some games really did have 0 players at their busiest time. By turning every 0 into a null, we've decided that's rare enough to ignore. Good data scientists write down decisions like this, so others can see them and disagree. That's what the **Our data story** section is for.

## Duplicates

A **duplicate** is a row, or a value, that appears more than once when it shouldn't. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/07_missing_values/cell21.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → keeps only the rows of `typed` whose `Name` appears more than once, using `is_duplicated`, then sorts them by `Name` so games with the same name sit together.

<!-- SCREENSHOT: assets/l07_duplicates.png — duplicated names sorted, showing the two 2048 rows -->

**2527** rows share a name with another row. Look at the two games called `2048`: they have different AppIDs, different release dates and different owners. They're different games that happen to have the same name.

So duplicate names aren't a mistake. This is why we use `AppID`, not `Name`, to identify a game. Lesson 1 told us that every game has its own AppID; next, we'll check that it's true.

## Writing checks

A **check** is a test that should always be `true` if our data makes sense. Writing checks down means we prove things about our data, instead of hoping. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/07_missing_values/cell22.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → imports `date` from Python's `datetime` library, so we can make a date in our code.
    - **line 3** → stores the date our data was collected in `DATA_DATE`. The capital letters show it's a **constant**: a value we set once and never change.
    - **line 5** → starts a dictionary called `checks`. Each key describes a check, and each value is its result.
    - **line 6** → checks that every value in `AppID` is unique, then uses `all` to give one `True` only if every row passed.
    - **line 7** → checks that no `Price` is below 0.
    - **line 8** → checks that `Name` has no nulls.
    - **lines 9–11** → check that no `Release date` is later than `DATA_DATE`. A game can't have been released after our data was collected.
    - **line 12** → closes the dictionary.
    - **line 13** → shows `checks` as the cell's output.

marimo shows the dictionary with each check and its result:

| Check | Result |
| :-- | :-- |
| every AppID is different | `True` |
| no negative prices | `True` |
| every game has a name | `False` |
| no release dates after the data date | `False` |

<!-- SCREENSHOT: assets/l07_checks.png — marimo output of the checks dictionary -->

Two checks pass and two fail. Use the table viewer on the `typed` cell to find the problem rows:

1. Search for `396420`. It's a game from 2016 with no name.
2. Sort by `Release date`, newest first. One game, `Roten`, says it was released on 1 December 2026. That's an **upcoming** release date: the game wasn't out yet when our data was collected.

Neither row can help our story, so we'll remove them. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/07_missing_values/cell23.py"
```

??? note "Code explanation"
    - **line 1** → starts filtering `missing` and will store the result in `checked`.
    - **line 2** → keeps only rows where `Name` is not null.
    - **line 3** → keeps only rows where `Release date` is on or before `DATA_DATE`. When we give `filter` more than one condition separated by commas, a row must pass all of them, just like using `&`.
    - **line 4** → closes the `filter` brackets.
    - **line 5** → shows the number of rows in `checked`.

The output is **138268**: two fewer rows than before.

!!! primm "PRIMM"
    Time to **modify** the code. Add a fifth check to the `checks` dictionary: no game has more `Owners min` than `Owners max`. Does it pass?

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 7: Missing values` and record our answers under it.

1. For each column our question needs, write down how many nulls it has in `missing`. Is there enough real data left to answer our question?
2. Write down every cleaning decision we made in this lesson, and why. Start each one with "We decided…".
3. Write one check of our own that our data should pass for our question. Add it to the `checks` dictionary and record whether it passes.
