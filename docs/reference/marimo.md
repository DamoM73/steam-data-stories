# marimo

!!! learn "On this page we will learn"
    - the marimo commands and shortcuts used in this course
    - the rules marimo notebooks follow
    - how to write text and add UI elements

**marimo** is a notebook for Python. We write code in small blocks called **cells**, and each cell's result appears straight away. marimo notebooks are saved as ordinary Python files. We import it with `import marimo as mo`.

## Terminal commands

Type these in the VS Code terminal, with `(.venv)` at the start of the prompt.

| Command | What it does | Where we learned it |
| :-- | :-- | :-- |
| `marimo edit clean_steam.py` | opens a notebook to edit, creating it if it doesn't exist | [Setting Up](../start/setup.md#open-our-first-notebook) |
| `marimo edit steam_story.py` | opens our second notebook | [Making New Columns](../insights/07_new_columns.md#a-new-notebook) |
| `marimo run steam_story.py` | opens a notebook in app view: outputs only, no code | [Publishing Our Data Story](../resolution/15_publishing.md#checking-the-app-view) |
| ++ctrl+c++, then `y` | stops marimo (++ctrl+c++ on a Mac too) | [Setting Up](../start/setup.md#open-our-first-notebook) |

!!! warning "Keep the terminal open"
    The notebook in our browser only works while marimo is running in the terminal.

## Keyboard shortcuts

| Windows | macOS | What it does |
| :-- | :-- | :-- |
| ++ctrl+enter++ | ++cmd+enter++ | runs the cell |
| ++shift+enter++ | ++shift+enter++ | runs the cell and adds a new cell below |
| ++ctrl+shift+r++ | ++cmd+shift+r++ | runs all stale cells: every cell that hasn't run yet |

## The rules

- **The output appears above the cell.** marimo shows the value of the last line of a cell. See [Exploring Our Data](../hook/02_exploring_data.md#notebooks-and-cells).
- **Each variable can only be created in one cell.** Creating it in a second cell gives a `MultipleDefinitionError`. To change a variable, make a new one with a new name, like `dated = selected.with_columns(…)`. See [Exploring Our Data](../hook/02_exploring_data.md#one-variable-one-cell).
- **Cells are reactive.** When a cell changes, every cell that uses its variables runs again too. See [Exploring Our Data](../hook/02_exploring_data.md#reactive-cells).
- **Cell order doesn't matter.** marimo works out the order to run cells from the variables they use, so we can put cells in any order. Drag the dots on a cell's left edge to move it. See [Publishing Our Data Story](../resolution/15_publishing.md#writing-with-momd).
- **Each notebook has its own variables.** `games` in ***clean_steam.py*** and `games` in ***steam_story.py*** are different. See [Making New Columns](../insights/07_new_columns.md#a-new-notebook).
- **Reopened notebooks don't run by themselves.** Press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run them.
- **marimo saves automatically.**

## The table viewer

When a cell's output is a DataFrame, marimo shows it in an interactive table. We can scroll through rows and columns, sort by clicking a column heading, search with the search box, and see a summary at the top of each column. See [Exploring Our Data](../hook/02_exploring_data.md#exploring-with-the-table-viewer).

## Writing text with mo.md

`mo.md` shows Markdown as formatted text. Put the text in triple quotes so it can go over many lines, and use an f-string to put variables into it.

```python title="steam_story.py"
mo.md(
    f"""
    ## Players like Indie games more

    The typical Indie game gets **{indie_score}%** positive reviews.
    """
)
```

See [Publishing Our Data Story](../resolution/15_publishing.md#writing-with-momd).

## UI elements

UI elements live in `mo.ui`. Store each one in a variable, then use its `value` in **another** cell: a cell can't use the value of a UI element it creates. We can show a UI element in any cell, so show it in the cell that uses it, next to the table or chart it changes. When someone changes it, every cell that uses it runs again.

| Code | UI element | `value` is | Where we learned it |
| :-- | :-- | :-- | :-- |
| `mo.ui.range_slider(start=2010, stop=2024, value=[2010, 2024], label="Years")` | a slider with two handles | a list of the start and end values | [The Aha Moment](../aha/14_aha_moment.md#creating-the-controls) |
| `mo.ui.dropdown(options=["Review score", "Price"], value="Review score", label="Measure")` | a menu where we choose one option | the chosen option | [The Aha Moment](../aha/14_aha_moment.md#creating-the-controls) |
| `mo.ui.slider(start=0, stop=60, value=20, label="Price")` | a slider with one handle | the chosen number | |
| `mo.ui.checkbox(label="Paid games only")` | a tick box | `True` or `False` | |
| `mo.hstack([years, measure])` | shows things side by side | | [The Aha Moment](../aha/14_aha_moment.md#connecting-the-controls) |
| `mo.vstack([mo.hstack([years, measure]), explore_chart])` | shows things one under the other | | [The Aha Moment](../aha/14_aha_moment.md#connecting-the-controls) |

!!! tip "Not covered in the lessons"
    `mo.ui.slider` and `mo.ui.checkbox` aren't used in our example story, but they work the same way as the UI elements in [The Aha Moment](../aha/14_aha_moment.md#creating-the-controls). They're here in case our own story needs them.

## Notebook files and folders

| Code | What it does | Where we learned it |
| :-- | :-- | :-- |
| `mo.notebook_dir()` | the folder our notebook is saved in | [Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server) |
| `mo.notebook_dir() / "data" / "clean_games.parquet"` | the path to a file in the ***data*** folder next to our notebook | [Publishing Our Data Story](../resolution/15_publishing.md#getting-ready-for-the-class-server) |

!!! tip "The official documentation"
    The [marimo documentation](https://docs.marimo.io/){ target="_blank" rel="noopener" } explains every feature, with examples.
