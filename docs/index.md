# Steam Data Stories

![Steam Data Stories](assets/logo.png){ width="160" }

Tell data stories about Steam games with Python, Polars, Plotly and marimo.

## How to use this site

- Work through the **Start** pages first. They explain what a data story is, introduce the Steam dataset and set up Python, VS Code and marimo.
- The lessons are grouped by the stages of a data story: **Hook**, **Behind the Scenes**, **Rising Insights**, **Aha Moment** and **Resolution**. Each lesson continues from the one before, so we do them in order.
- Each lesson works through one example question about Steam games. At the end of each lesson we apply what we've learnt to our own question about the same data, so our own data story grows as we go.
- **Reference** has a summary of the data story arc, Polars, Plotly Express and marimo, plus the errors we're most likely to see.

## Callouts

Coloured boxes called **callouts** highlight different kinds of information. Each type of callout has its own colour and icon, so we can tell at a glance what it's for.

!!! learn "Learning intentions"
    This callout is at the top of every lesson page. It lists what we will learn on that page.

!!! terms "Terminology"
    This callout comes straight after the learning intentions. It lists the new technical terms on the page, with a short definition of each. Every term is also on the [Glossary](reference/glossary.md) page.

!!! primm "PRIMM"
    This callout comes after each example. It asks us to **predict** what the code will do, **run** it, and **investigate** how it works. Sometimes it asks us to **modify** the code.

!!! note "Code explanation"
    This callout comes after each piece of code and gives a line-by-line explanation. On the lesson pages it starts closed, so we can make our own prediction first. Click its title to open it.

!!! tip "Tip"
    This callout gives extra information, such as definitions, background facts, comparisons and hints.

!!! warning "Warning"
    This callout warns us about mistakes that are easy to make, or things that will stop our notebook working.

## Code blocks

We write our code in **marimo notebooks**. A notebook is made of **cells**, and each code block on a lesson page is one cell:

```python linenums="1" hl_lines="2" title="steam_story.py — change existing cell"
games = pl.read_parquet(mo.notebook_dir() / "data" / "clean_games.parquet")
games.head()
```

- the **notebook name** above the code tells us which notebook the cell belongs to. We use two notebooks: ***clean_steam.py*** for exploring and cleaning the data, and ***steam_story.py*** for telling our story
- the words after the notebook name tell us **where the code goes**:
    - **new cell** → add a new cell at the bottom of the notebook, and type the code into it
    - **change existing cell** → don't add a cell. Find the cell we already made, and change it to match the code
    - **first cell** → type the code into the empty cell a new notebook starts with
    - **change first cell** → change the cell at the top of the notebook, the one with our imports
- **line numbers** match the line numbers in the Code explanation
- **highlighted lines** are new or changed since the last time we saw the cell, so they're the lines we need to add or change
- the **copy** button in the top-right corner copies the code to paste into a marimo cell

Code blocks without colours show commands to type in the terminal, or what appears when we run a cell.

## Error messages

When a cell has an error, marimo shows the error message in red under the cell, and the lesson pages show a screenshot of it. Errors that appear in the terminal, outside marimo, are shown in red code blocks like this one:

``` { .text .error linenums="1" }
Activate.ps1 cannot be loaded because running scripts is disabled
```

Under each error message, the lesson breaks it down part by part, so we learn how to read the error and fix our code. The [Common Errors](reference/common_errors.md) page collects the errors we're most likely to see.

## Tutorial files

The tutorial files are our classroom copy of the Steam data: the 10,250 Steam games with at least 500 reviews. Everyone uses the same copy, so our results match the lessons. Download [steam_games.csv](downloads/steam_games.csv){ download="steam_games.csv" } and [README.txt](downloads/README.txt){ download="README.txt" }, and follow [Setting Up](start/setup.md#download-the-data) to put them in the right place.
