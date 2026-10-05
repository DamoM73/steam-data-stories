# Common Errors

!!! learn "On this page we will learn"
    - how to read an error message
    - the errors we're most likely to see in this course
    - how to fix each one

## Reading an error message

When a cell has a problem, marimo shows the error in red above the cell, instead of the output. Don't panic: the error message is trying to help. Read it in three parts:

1. **the error type**, like `ColumnNotFoundError`, tells us what kind of problem it is
2. **the message** after the colon tells us exactly what went wrong
3. **the expression** at the end, if there is one, shows which part of our code caused it

Most errors in this course come from a small typing mistake. Check spelling, capital letters, brackets and quotation marks first.

## Setting up

### ModuleNotFoundError

``` { .text .error }
ModuleNotFoundError: No module named 'polars'
```

- **What it means:** Python can't find the library we're importing.
- **Usual cause:** the library was installed without `(.venv)` at the start of the terminal prompt, so it went into a different Python. Or marimo was started without `(.venv)`.
- **Fix:** stop marimo, check the prompt starts with `(.venv)`, then run the install command from [Setting Up](../start/setup.md#install-the-libraries) again.

### ImportError: Plotly Express requires numpy

``` { .text .error }
ImportError: Plotly Express requires numpy to be installed.
```

- **What it means:** Plotly Express needs the NumPy library to draw charts from Polars data.
- **Fix:** stop marimo and run `pip install numpy` in the terminal, with `(.venv)` at the start of the prompt.

### FileNotFoundError

``` { .text .error }
FileNotFoundError: No such file or directory (os error 2): steam_games.csv
```

- **What it means:** Polars can't find the file at that path.
- **Usual causes:**
    - the path is missing the folder, like `steam_games.csv` instead of `data/steam_games.csv`
    - the data wasn't unzipped into a folder called ***data***
    - marimo was started from a different folder, so the path starts in the wrong place
- **Fix:** check the path matches the file in VS Code's Explorer panel, and that the terminal is in our ***steam_data_stories*** folder when we start marimo. In Lesson 9, if ***clean_games.parquet*** is missing, go back and run the saving cell from [Lesson 8](../cleaning/08_text_lists.md#saving-our-clean-data).

## marimo

### MultipleDefinitionError

``` { .text .error }
MultipleDefinitionError: The variable 'sample_size' was defined by another cell
```

- **What it means:** the same variable is created in two cells. marimo won't run either of them.
- **Fix:** give the new version a new name, like `typed` instead of `selected`, or delete one of the cells. See [Lesson 2](../hook/02_exploring_data.md#one-variable-one-cell).

### NameError

``` { .text .error }
NameError: name 'scored' is not defined
```

- **What it means:** the cell uses a variable that doesn't exist yet.
- **Usual causes:** a spelling mistake in the variable's name, or the cell that creates it has an error, or it was created in our other notebook.
- **Fix:** check the spelling, then fix any errors in earlier cells. Remember that ***clean_steam.py*** and ***steam_story.py*** have separate variables.

## Polars

### ColumnNotFoundError

``` { .text .error }
ColumnNotFoundError: unable to find column "Prices"; valid columns: ["AppID", "Name", "Release date", …]
```

- **What it means:** there's no column with that name.
- **Fix:** compare our spelling with the list of valid columns in the message. Column names are case sensitive and include spaces: `"Peak CCU"`, not `"peak_ccu"`.

### TypeError: the truth value of an Expr is ambiguous

``` { .text .error }
TypeError: the truth value of an Expr is ambiguous
```

- **What it means:** Python tried to treat a Polars expression as a single `True` or `False`.
- **Usual causes:** using `and` or `or` instead of `&` or `|`, or leaving out the brackets around each condition.
- **Fix:** write `(pl.col("Price") > 0) & (pl.col("Recommendations") > 1000)`. See [Lesson 5](../cleaning/05_select_filter.md#combining-conditions).

### ComputeError: could not find an appropriate format

``` { .text .error }
ComputeError: could not find an appropriate format to parse dates, please define a format
```

- **What it means:** Polars can't work out how our dates are written.
- **Fix:** give `str.to_date` a format code, like `str.to_date("%b %d, %Y")`. See [Lesson 6](../cleaning/06_data_types.md#text-into-dates).

### InvalidOperationError: casting from string to date

``` { .text .error }
InvalidOperationError: casting from string to date is not supported.
It was removed in Polars 2.0. Use `str.to_date()` instead.
```

- **What it means:** we used `cast(pl.Date)` on a text column. Older versions of Polars allowed this, so we'll see it in older examples online.
- **Fix:** use `str.to_date` with a format code instead.

### InvalidOperationError: conversion failed

``` { .text .error }
InvalidOperationError: conversion from `str` to `i64` failed in column 'Estimated owners' for 233 out of 233 values: ["0 - 0", "0 - 20000", … "0 - 20000"]
```

- **What it means:** some text can't be turned into the data type we asked for. The message shows some of the values that failed.
- **Fix:** look at the failed values. Remove or split out the parts that aren't numbers first, like we did with `str.split` in [Lesson 6](../cleaning/06_data_types.md#text-into-numbers).

### SchemaError: datatypes of join keys don't match

``` { .text .error }
SchemaError: datatypes of join keys don't match - `AppID`: str on left does not match `AppID`: i64 on right
```

- **What it means:** the key column has a different data type in each DataFrame.
- **Fix:** `cast` one of them so they match, like `pl.col("AppID").cast(pl.Int64)`. See [Lesson 14](../insights/14_combining.md#joining-dataframes).

## Results that look wrong

Some problems don't cause an error, but give us the wrong answer.

| What we see | Likely cause | Fix |
| :-- | :-- | :-- |
| a filter or join finds nothing, or gives nulls | text that doesn't match exactly, like a capital letter | compare in lowercase with `str.to_lowercase`, or use an ID instead of a name ([Lesson 8](../cleaning/08_text_lists.md#matching-text)) |
| `NaN` in a calculation | dividing 0 by 0 | use `fill_nan(None)` ([Lesson 9](../insights/09_new_columns.md#nan-is-not-null)) |
| a mean that seems far too small | 0s that really mean "missing" | `replace(0, None)` ([Lesson 7](../cleaning/07_missing_values.md#hidden-missing-values)) |
| groups or bars in a strange order | `group_by` doesn't keep any order | add `sort`, or `category_orders` in a chart ([Lesson 11](../insights/11_charts_compare.md#box-plots)) |
| a chart squashed to one side | an outlier stretching the axis | filter out the extreme values and say so ([Lesson 11](../insights/11_charts_compare.md#histograms)) |
| the API returns status code 429 | too many requests | wait, and use the saved files ([Lesson 13](../insights/13_api.md#sending-a-request)) |
| a notebook shows no outputs | it hasn't been run since it was opened | press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) |
