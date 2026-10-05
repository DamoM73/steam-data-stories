# 6. Fixing Data Types

!!! learn "In this lesson we will learn"
    - why the data type of a column matters
    - how to turn text into dates with `str.to_date`
    - how to read a date format code like `%b %d, %Y`
    - how to split text and turn the parts into numbers with `cast`
    - how to make new columns with `with_columns` and `alias`

## Introduction

In Lesson 2 we found that two important columns hold the wrong kind of data. `Release date` holds dates, and `Estimated owners` holds numbers, but Polars stored both of them as **String**: text.

Text can't be used for dates or maths. Sorted as text, `Apr 30, 2024` comes before `Oct 30, 2025` and `Mar 5, 2026`, because the sorting goes letter by letter: April before March before October. We can't ask "which games came out after 2020?" or "how many more owners?" until we fix the data types.

## Text into dates

Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_data_types/cell17a.py"
```

??? note "Code explanation"
    - **line 1** → starts making a new version of `selected` with changed columns, using `with_columns`, and will store it in `typed`.
    - **line 2** → tries to turn the text in `Release date` into dates, using `str.to_date`.
    - **line 3** → closes the `with_columns` brackets.
    - **line 4** → shows `typed` as the cell's output.

We get an error:

``` { .text .error linenums="1" }
ComputeError: could not find an appropriate format to parse dates, please define a format
```

- **line 1** → `ComputeError` means Polars couldn't finish a calculation. The message says it couldn't work out how our dates are written, so we need to tell it.

Polars recognises dates written like `2025-10-30`, but ours are written like `Oct 30, 2025`. We describe that pattern with a **format code**:

| Part of the date | Format code | Example |
| :-- | :-- | :-- |
| short month name | `%b` | `Oct` |
| day of the month | `%d` | `30` |
| four-digit year | `%Y` | `2025` |

Everything that isn't a format code, like the space and the comma, has to match the text exactly. So `Oct 30, 2025` has the format `%b %d, %Y`.

Change the cell to match the code below and run it again.

```python linenums="1" title="clean_steam.py" hl_lines="2"
--8<-- "examples/cleaning/06_data_types/cell17b.py"
```

??? note "Code explanation"
    - **line 2** → turns the text in `Release date` into dates, using the format `%b %d, %Y`. Because the new column has the same name as the old one, it replaces it.

<!-- SCREENSHOT: assets/l06_dates.png — the typed table with Release date shown as dates (2023-08-01 style) -->

The `Release date` column now shows dates like `2023-08-01`, and its data type is **date**. Every one of the 138,270 dates converted, so no row was left empty.

!!! tip "One format for every row"
    `str.to_date` uses the same format for every row. If even one row were written differently, like `30 Oct 2025`, Polars would stop with an error. That's a useful check: it proves every date in our data is written the same way.

## Text into numbers

`Estimated owners` holds text like `0 - 20000`. Let's see what happens if we ask Polars to turn it straight into a whole number. Change the cell to match the code below and run it.

```python linenums="1" title="clean_steam.py" hl_lines="3"
--8<-- "examples/cleaning/06_data_types/cell17c.py"
```

??? note "Code explanation"
    - **line 3** → tries to **cast** the `Estimated owners` column, which means change its data type, to `pl.Int64`: whole numbers.

Another error:

``` { .text .error linenums="1" }
InvalidOperationError: conversion from `str` to `i64` failed in column 'Estimated owners' for 233 out of 233 values: ["0 - 0", "0 - 20000", … "0 - 20000"]
```

- **line 1** → `InvalidOperationError` means we asked for something that can't be done with these values. Polars can't turn `0 - 20000` into a single whole number, because it isn't one: it's two numbers with a dash between them. The numbers in the message might be different on our computer, because Polars stops as soon as it finds a batch of values that fail.

The fix is to split the text into its two numbers first. `0 - 20000` means "somewhere between 0 and 20,000 owners", so we'll make two new columns: `Owners min` and `Owners max`.

Change the cell to match the code below and run it.

```python linenums="1" title="clean_steam.py" hl_lines="3-12"
--8<-- "examples/cleaning/06_data_types/cell17.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 3** → starts with the `Estimated owners` column.
    - **line 4** → splits each value wherever it finds `" - "`, which turns `0 - 20000` into a **list** of two pieces of text: `["0", "20000"]`.
    - **line 5** → keeps the first item of each list: `"0"`.
    - **line 6** → casts that text to a whole number, which works now because `"0"` is a number on its own.
    - **line 7** → names the new column `Owners min`, using `alias`. Without a new name it would replace `Estimated owners`.
    - **lines 8–12** → do the same again, but keep the **last** item of each list and name the column `Owners max`.

The cell shows `typed`, which now has 15 columns. Let's look at just the ones we changed. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/cleaning/06_data_types/cell18.py"
```

??? note "Code explanation"
    - **line 1** → shows only the `Release date`, `Estimated owners`, `Owners min` and `Owners max` columns of `typed`.

<!-- SCREENSHOT: assets/l06_owners.png — Release date, Estimated owners, Owners min and Owners max side by side -->

`Owners min` and `Owners max` are **i64** columns: whole numbers we can sort, compare and do maths with. We kept `Estimated owners` too, so we can always check our new columns against the original.

!!! tip "Method chains"
    Lines 3 to 7 are one long instruction split over several lines. Each line starting with `.` does one step to the result of the line above. This is called a **method chain**. Reading it from top to bottom tells us the steps in order: take the column, split it, keep the first part, make it a number, name it.

!!! primm "PRIMM"
    Time to **modify** the code. Add a third new column called `Owners middle`, halfway between `Owners min` and `Owners max`. Hint: we can't use `Owners min` inside the same `with_columns` that makes it, so add it in a new cell with a new variable name.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 6: Data types` and record our answers under it.

1. List the columns our question needs, with the data type of each one in `typed`.
2. Are any of them stored as the wrong type? Write down what type each should be and how we fixed it, or how we could fix it.
3. Write one sentence explaining why the right data type matters for our question.
