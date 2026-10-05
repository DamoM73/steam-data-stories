# marimo

!!! learn "On this page we will learn"
    - the marimo commands and shortcuts used in this course
    - the rules marimo notebooks follow
    - marimo's interactive controls

**marimo** is a notebook for Python. We write code in small blocks called **cells**, and each cell's result appears straight away. marimo notebooks are saved as ordinary Python files.

## Terminal commands

Type these in the VS Code terminal, with `(.venv)` at the start of the prompt.

| Command | What it does | Lesson |
| :-- | :-- | :-- |
| `marimo edit clean_steam.py` | opens a notebook to edit, creating it if it doesn't exist | [Setting Up](../start/setup.md#open-our-first-notebook) |
| `marimo run steam_story.py` | opens a notebook as an app: outputs only, no code | [16](../resolution/16_publishing.md#presenting-it-live) |
| `marimo export html steam_story.py -o my_data_story.html --no-include-code` | runs a notebook and saves its outputs as a web page | [16](../resolution/16_publishing.md#sharing-a-file) |
| ++ctrl+c++, then `y` | stops marimo (++ctrl+c++ on a Mac too) | [Setting Up](../start/setup.md#open-our-first-notebook) |

!!! warning "Keep the terminal open"
    The notebook in our browser only works while marimo is running in the terminal.

## Keyboard shortcuts

| Windows | macOS | What it does |
| :-- | :-- | :-- |
| ++ctrl+enter++ | ++cmd+enter++ | runs the cell |
| ++shift+enter++ | ++shift+enter++ | runs the cell and adds a new cell below |
| ++ctrl+shift+r++ | ++cmd+shift+r++ | runs all stale cells: every cell that hasn't run yet |
| ++ctrl+period++ | ++cmd+period++ | switches between the code and app view |

## The rules

- **The output appears above the cell.** marimo shows the value of the last line of a cell.
- **Each variable can only be created in one cell.** Creating it in a second cell gives a `MultipleDefinitionError`. To change a variable, make a new one with a new name, like `typed = selected.with_columns(…)`. See [Lesson 2](../hook/02_exploring_data.md#one-variable-one-cell).
- **Cells are reactive.** When a cell runs, every cell that uses its variables runs again too. See [Lesson 2](../hook/02_exploring_data.md#reactive-cells).
- **Cell order doesn't matter.** marimo works out the order to run cells from the variables they use, so we can arrange cells in any order. See [Lesson 16](../resolution/16_publishing.md#tidying-the-notebook).
- **Reopened notebooks don't run by themselves.** Press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run them.
- **marimo saves automatically.**

## The table viewer

When a cell's output is a DataFrame, marimo shows it as an interactive table. We can scroll through rows and columns, sort by clicking a column heading, search with the search box, and see a summary at the top of each column. See [Lesson 2](../hook/02_exploring_data.md#exploring-with-the-table-viewer).

## Markdown

`mo.md` shows formatted text. Use an f-string to put variables into the text.

```python title="steam_story.py"
mo.md(
    f"""
    ## What we found

    ARC Raiders still had **{arc_month_6}%** of its peak players.
    """
)
```

See [Lesson 16](../resolution/16_publishing.md#writing-with-markdown).

## Interactive controls

Interactive controls live in `mo.ui`. Store each control in a variable, show it as a cell's output, and use its `value` in another cell. When someone changes the control, every cell that uses it runs again.

| Code | Control | `value` is |
| :-- | :-- | :-- |
| `mo.ui.slider(1, 11, value=11, label="Months")` | a slider | the chosen number |
| `mo.ui.multiselect(options=["A", "B"], label="Games")` | a menu where we can choose several options | a list of the chosen options |
| `mo.ui.dropdown(options=["A", "B"], label="Game")` | a menu where we choose one option | the chosen option |
| `mo.ui.checkbox(label="Only PvE")` | a tick box | `True` or `False` |
| `mo.hstack([control_1, control_2])` | shows controls side by side | |

See [Lesson 15](../aha/15_aha_moment.md#letting-our-audience-explore).

!!! tip "The official documentation"
    The [marimo documentation](https://docs.marimo.io/) explains every feature, with examples.
