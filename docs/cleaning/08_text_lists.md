# 8. Cleaning Text and Lists

!!! learn "In this lesson we will learn"
    - how to write our own function to reuse code
    - how to turn comma-separated text into lists
    - how to count the items in lists with `explode`
    - how to search lists with `list.contains`
    - how to match text that uses different capital letters
    - how to save our clean data as a Parquet file

## Introduction

This is our last Behind the Scenes lesson. Three of our columns, `Genres`, `Tags` and `Categories`, each pack several labels into one piece of text, like `Action,Adventure,Indie`. That makes simple questions surprisingly hard. How many games are Indie games? Searching the text for `Indie` would also match a tag like `Indie Horror`, so we'd get the wrong answer.

The fix is to turn each piece of text into a **list** of labels. Then we'll save our clean data, ready for the Rising Insights lessons.

## Writing a function

We need to do the same thing to three columns. Instead of typing it three times, we'll write a **function**. Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/08_text_lists/cell24.py"
```

??? note "Code explanation"
    - **line 1** → defines a function called `to_list` that takes the name of a column.
    - **line 2** → returns an expression that splits that column's text wherever there's a comma, turning each value into a list.

Nothing appears above the cell. Defining a function doesn't run it; it just makes it ready to use, in this cell or any other.

## Text into lists

Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/08_text_lists/cell25.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → starts making a new version of `checked` with changed columns, and will store it in `clean_games`.
    - **lines 2–4** → use our `to_list` function to turn the `Genres`, `Tags` and `Categories` columns into lists.
    - **line 5** → closes the `with_columns` brackets.
    - **line 6** → shows just the `Name`, `Genres` and `Tags` columns of `clean_games`.

<!-- SCREENSHOT: assets/l08_lists.png — Name, Genres and Tags shown as lists in marimo -->

Each value is now a list, like `["Adventure"]` or `["Casual", "Indie", "Simulation"]`, and the data type is **list[str]**: a list of strings. Games with no labels still have a null.

## Counting labels

Now let's count how many games have each genre. To do that, we **explode** the lists: we make one row for every item in every list. A game with three genres becomes three rows, one for each genre.

Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/08_text_lists/cell26.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change it to count `Categories` instead of `Genres`. What's the most common category?

??? note "Code explanation"
    - **line 1** → explodes the `Genres` lists of `clean_games` so each genre gets its own row, picks the `Genres` column, counts how many times each genre appears, sorted from most to least common, and stores the counts in `genre_counts`.
    - **line 2** → shows `genre_counts` as the cell's output.

The top three are **Indie** with 92,088 games, **Casual** with 57,008 and **Action** with 52,271. The counts add up to far more than 138,268, because most games have more than one genre.

## Searching lists

Our example story is about extraction shooters. Steam has a tag for them, so let's find every game with it. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/08_text_lists/cell27.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change `"Extraction Shooter"` to `"PvE"`. How many games have that tag?

??? note "Code explanation"
    - **lines 1–3** → keep only the games whose `Tags` list contains the tag `Extraction Shooter` exactly, using `list.contains`, and store them in `extraction_shooters`.
    - **line 4** → shows the `AppID`, `Name` and `Release date` of those games.

**38** games have the tag, but none of them are our six games. Why not? Look back at `story_rows` from Lesson 5: `Tags` is null for five of our six games. Tags come from SteamSpy, and SteamSpy hasn't labelled most recent games.

This is why we chose our story's games ourselves in Lesson 3, using what we know about them, instead of trusting a column that's mostly empty for new games.

## Matching text

When we make our own list of games, the names have to match the data exactly. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/08_text_lists/cell28.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Remove `.str.to_lowercase()` and change the name to `"Escape from Duckov"`, as we wrote it in `story_games`. What happens?

??? note "Code explanation"
    - **lines 1–2** → change every `Name` to lowercase letters, using `str.to_lowercase`, and keep only the rows that match `escape from duckov`.
    - **line 3** → shows only the `AppID` and `Name` of the matching rows.

The game is found, and its real name in the data is `Escape From Duckov`, with a capital **F**. In `story_games` we wrote `Escape from Duckov`. Text matching is **case sensitive**, so without `to_lowercase` Polars wouldn't find a match. Changing everything to lowercase before comparing means the capital letters can't trip us up.

We'll meet this problem again in Lesson 14, and it's one more reason to match games by `AppID` instead of by name.

## Saving our clean data

Our cleaning is done. Rather than run every cleaning cell again in the next notebook, we'll save the result. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/08_text_lists/cell29.py"
```

??? note "Code explanation"
    - **line 1** → saves `clean_games` as a **Parquet** file called ***clean_games.parquet*** in our ***data*** folder.
    - **line 2** → saves `story_games` as ***story_games.parquet*** in the same folder.

Check VS Code's Explorer panel: the two new files are in our ***data*** folder.

!!! tip "Why Parquet and not CSV?"
    A **Parquet** file stores each column's data type along with the data. When we load it again, our dates are still dates and our lists are still lists, so we don't have to fix them a second time. It's also much smaller: ***clean_games.parquet*** is about 7 MB, compared with about 400 MB for ***steam_games.csv***.

!!! warning "Re-run the saving cell after changes"
    If we change any cleaning cell later, the Parquet files won't update by themselves. Run the saving cell again so our second notebook gets the new version.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 8: Clean data` and record our answers under it.

1. If our question uses genres, tags or categories, write a `list.contains` filter for the label we need, and record how many games have it. Are many of them missing labels?
2. Write a short summary of everything we did Behind the Scenes, in the order we did it, in five to eight dot points. This becomes the "How we got our data" part of our finished story.
3. Write down one thing about our data that our audience should know, because it limits what we can claim.
