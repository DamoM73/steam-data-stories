# Common Errors

!!! learn "On this page we will learn"
    - how to read an error message
    - the errors we're most likely to see in this course
    - how to fix each one

## Reading an error message

When a cell has a problem, marimo shows the error in red where the cell's output would be. The error message is trying to help us, so read it in three parts:

1. **the error type**, like `ColumnNotFoundError`, tells us what kind of problem it is
2. **the message** after the colon tells us exactly what went wrong
3. **the expression**, if there is one, shows which part of our code caused it

Most errors in this course come from a small typing mistake. Check spelling, capital letters, brackets and quotation marks first.

## Setting up

### ModuleNotFoundError

``` { .text .error linenums="1" }
ModuleNotFoundError: No module named 'polars'
```

- **line 1** → Python can't find the library we're importing, here Polars.

The library was probably installed without `(.venv)` at the start of the terminal prompt, so it went into a different Python, or marimo was started without `(.venv)`. To fix it, stop marimo, check the prompt starts with `(.venv)`, then run the install command from [Setting Up](../start/setup.md#install-the-libraries) again.

### ImportError: Plotly Express requires numpy

``` { .text .error linenums="1" }
ImportError: Plotly Express requires numpy to be installed. You can install numpy using pip with:

$ pip install numpy
```

- **line 1** → Plotly Express needs the NumPy library to draw charts from Polars data, and it isn't installed.
- **line 3** → the command that installs it.

To fix it, stop marimo and run `pip install numpy` in the terminal, with `(.venv)` at the start of the prompt.

### Running scripts is disabled (Windows)

``` { .text .error linenums="1" }
Activate.ps1 cannot be loaded because running scripts is disabled
```

- **line 1** → Windows won't let PowerShell switch on our virtual environment.

To fix it, follow [Running scripts is disabled](../start/setup.md#running-scripts-is-disabled-windows) in Setting Up.

### FileNotFoundError

``` { .text .error linenums="1" }
FileNotFoundError: No such file or directory (os error 2): steam_games.csv
```

- **line 1** → Polars can't find a file at the path we gave it, here `steam_games.csv`.

Check that:

1. the path includes the folder, like `"data/steam_games.csv"`, not `"steam_games.csv"`
2. the data was unzipped into a folder called ***data*** inside our project folder
3. the terminal was in our ***steam_data_stories*** folder when we started marimo
4. in ***steam_story.py***, ***clean_games.parquet*** exists. If it doesn't, run the saving cell in ***clean_steam.py*** from [Fixing Our Data](../cleaning/06_fixing_data.md#saving-our-clean-data)

On the class server, this error means our notebook still uses `"data/clean_games.parquet"` instead of `mo.notebook_dir()`. See [Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server).

## marimo

### MultipleDefinitionError

![marimo showing CELL NOT RUN under the cell sample_size = 10, with the message This cell redefines variables from other cells, 'sample_size' was also defined by cell-4, and a Fix: Wrap in a function button](../assets/102_multiple_definition_error.png)

- **CELL NOT RUN** → marimo has refused to run this cell.
- **This cell redefines variables from other cells.** → the same variable, here `sample_size`, is created in two cells.
- **'sample_size' was also defined by: cell-4** → names the variable, and the cell that created it first. Click the cell's name to jump to it.

Don't use the **Fix: Wrap in a function** button: it hides the problem rather than fixing it. To fix it, give the new version a new name, like `dated` instead of `selected`, or delete one of the cells. This often happens when we copy a pattern from a lesson for our own story. See [Exploring Our Data](../hook/02_exploring_data.md#one-variable-one-cell).

### NameError

``` { .text .error linenums="1" }
NameError: name 'mo' is not defined
```

- **line 1** → the cell uses a name, here `mo`, that doesn't exist in this notebook.

Check that:

1. the name is spelt correctly, including capital letters
2. for `mo`, the first cell has `import marimo as mo`. See [The Aha Moment](../aha/14_aha_moment.md#letting-our-audience-explore)
3. for `pl` or `px`, the first cell imports Polars and Plotly Express
4. for a variable, the cell that creates it doesn't have an error of its own
5. the variable was made in **this** notebook: ***clean_steam.py*** and ***steam_story.py*** have separate variables

### RuntimeError: Accessing the value of a UIElement

``` { .text .error linenums="1" }
RuntimeError: Accessing the value of a UIElement in the cell that created it is not allowed. Fix: move the value access to another cell.
```

- **line 1** → we created a UI element and used its `value` in the same cell.

To fix it, create and show the UI element in one cell, then use its `value` in a different cell, just like `years` and `explore` in [The Aha Moment](../aha/14_aha_moment.md#connecting-the-controls).

## Polars

### ColumnNotFoundError

``` { .text .error linenums="1" }
ColumnNotFoundError: unable to find column "price"; valid columns: ["AppID", "Name", "Release date", "Price", "Positive", "Negative", "Recommendations", "Metacritic score", "Developers", "Genres"]

Did you mean "Price"?
```

- **line 1** → there's no column called `price`, and the message lists every column the DataFrame does have.
- **line 3** → Polars suggests the column we probably meant.

To fix it, compare our spelling with the list of valid columns. Column names are case sensitive and can include spaces: `"Price"`, not `"price"`, and `"Review score"`, not `"Review Score"`. If the column we want isn't in the list at all, check that we're using the right DataFrame: `Review score` is in `scored`, not `games`.

### TypeError: the truth value of an Expr is ambiguous

``` { .text .error linenums="1" }
TypeError: the truth value of an Expr is ambiguous
```

- **line 1** → Python tried to treat a Polars expression as a single `True` or `False`.

This usually means we used `and` or `or` instead of `&` or `|`, or left out the brackets around each condition. Write each condition in its own brackets: `(pl.col("Price") > 0) & (pl.col("Recommendations") > 10000)`. See [Choosing Columns and Rows](../cleaning/05_select_filter.md#combining-conditions).

### ComputeError: could not find an appropriate format

``` { .text .error linenums="1" }
ComputeError: could not find an appropriate format to parse dates, please define a format
```

- **line 1** → Polars can't work out how our dates are written.

To fix it, give `str.to_date` a format code, like `str.to_date("%b %d, %Y")`. See [Fixing Our Data](../cleaning/06_fixing_data.md#text-into-dates) and the [date format codes](polars.md#text-and-dates).

### ComputeError: cannot compare string with numeric type

``` { .text .error linenums="1" }
ComputeError: cannot compare string with numeric type (i32)

This error occurred in the following expression:
    [(col("Name")) > (dyn int: 5)]
```

- **line 1** → we compared a text column with a number.
- **line 4** → the expression that caused it: `Name` is text, but we checked whether it was greater than `5`.

Check that we've used the right column. If a column of numbers is stored as text, check its data type with `schema`.

### InvalidOperationError: operation not supported for dtype str

``` { .text .error linenums="1" }
InvalidOperationError: `year` operation not supported for dtype `str`

This error occurred in the following expression:
    col("Release date").dt.year()
```

- **line 1** → we used a date method, `year`, on a column of text (`str`).
- **line 4** → the expression that caused it.

The release dates are only real dates after we convert them in [Fixing Our Data](../cleaning/06_fixing_data.md#text-into-dates). In ***steam_story.py***, check that we loaded ***clean_games.parquet***, not ***steam_games.csv***.

### InvalidOperationError: expected String type

``` { .text .error linenums="1" }
InvalidOperationError: expected String type, got: f64
```

- **line 1** → we used a text method, such as `str.contains`, on a column of numbers. `f64` is short for `Float64`.

Text methods only work on text columns. To compare numbers, use `>`, `<` or `==` instead.

### DuplicateError

``` { .text .error linenums="1" }
DuplicateError: column with name 'Price' has more than one occurrence
```

- **line 1** → our result would have two columns with the same name, here `Price`.

This usually happens inside `agg`, when we summarise the same column twice, like `pl.col("Price").median()` and `pl.col("Price").mean()`. To fix it, give each summary its own name with `alias`, like `.alias("Median price")`. See [Summarising Groups](../insights/08_summarising_groups.md#mean-or-median).

## Plotly Express

### ValueError: not the name of a column

``` { .text .error linenums="1" }
ValueError: Value of 'x' is not the name of a column in 'data_frame'. Expected one of ['AppID', 'Name', 'Release date', 'Price', 'Positive', 'Negative', 'Recommendations', 'Metacritic score', 'Developers', 'Genres', 'Review score', 'Release year', 'Group'] but received: group
```

- **line 1** → the column we gave for `x`, here `group`, isn't in the DataFrame. The message lists the columns that are.

To fix it, check the spelling and capital letters: `"Group"`, not `"group"`. If the column isn't in the list, check that we're charting the right DataFrame.

## Results that look wrong

Some problems don't cause an error, but give us the wrong result.

| What we see | Likely cause | Fix |
| :-- | :-- | :-- |
| a notebook shows no outputs | it hasn't run since we opened it | press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) |
| a mean that seems far too small | 0s that really mean "missing" | `replace(0, None)` ([Fixing Our Data](../cleaning/06_fixing_data.md#values-that-mean-missing)) |
| groups in a different order each time | `group_by` doesn't keep any order | add `sort`, or `category_orders` in a chart ([Summarising Groups](../insights/08_summarising_groups.md#comparing-our-two-groups)) |
| a group's bars look taller just because it's bigger | comparing counts of groups with different sizes | use `histnorm="percent"` ([Bar Charts and Histograms](../insights/09_bar_histogram.md#comparing-two-groups)) |
| `{indie_score}` appears in our text instead of a number | the `f` before the quotes is missing | write `f"""` ([Publishing Our Data Story](../resolution/15_publishing.md#putting-numbers-in-our-text)) |
| a working table appears in app view | the cell still ends with a line that shows it | delete that last line ([Publishing Our Data Story](../resolution/15_publishing.md#tidying-for-our-audience)) |
| a slider or dropdown does nothing | no other cell uses its `value` yet | use `.value` in another cell ([The Aha Moment](../aha/14_aha_moment.md#connecting-the-controls)) |
| our story is an empty page on the class server | the notebook can't find its data | use `mo.notebook_dir()` ([Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server)) |
