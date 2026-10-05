# 16. Publishing Our Data Story

!!! learn "In this lesson we will learn"
    - what the Resolution stage of our story does
    - how to write the words of our story with `mo.md`
    - how to put live numbers into our writing with f-strings
    - how to be honest about the limits of our data
    - how to turn our notebook into a finished story with app view and HTML export

## Introduction

Welcome to the **Resolution**, the final stage of our story arc. We've found our answer. Now we explain what it means, admit what our data can't tell us, and share the finished story with an audience who has never seen our notebook.

A notebook full of code isn't a story. In this lesson we'll add the words, hide the code, and publish the result.

## Writing with Markdown

marimo can show formatted text in a cell, using **Markdown**, the same format as ***my_data_story.md***. Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/resolution/16_publishing/story27.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → starts a Markdown output, using `mo.md`.
    - **lines 2–9** → hold the Markdown text in a **triple-quoted string**, which can go over several lines. The `#` line becomes a heading, and the rest becomes a paragraph. marimo removes the spaces at the start of each line for us.
    - **line 10** → closes the brackets.

<!-- SCREENSHOT: assets/l16_md_hook.png — the rendered Markdown hook with heading and paragraph -->

The cell shows a heading and a paragraph, with no code in sight. This is our **Hook**: it opens our story with the question, and gives our audience a reason to care.

## Putting numbers in our words

Numbers we type into our writing can go out of date. If we change a cleaning step, a number in our text might no longer match our charts. An **f-string** fixes this: it puts the value of a variable straight into the text.

Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/resolution/16_publishing/story28.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Add a sentence that uses Escape from Tarkov's month 6 percent of peak, from a new variable.

??? note "Code explanation"
    - **lines 1–3** → keep the row of `monthly` for ARC Raiders in month 6, pick its `Percent of peak` column, take the first value with `[0]`, and store it in `arc_month_6`.
    - **line 4** → starts a Markdown output.
    - **lines 5–12** → hold the text in an **f-string**, which starts with `f`. Anything inside curly brackets, like `{arc_month_6}`, is replaced by its value. The `**` on each side makes the number bold.
    - **line 13** → closes the brackets.

The output says ARC Raiders still had **28.4%** of its peak players after six months. If our data ever changes, this number changes with it.

## Writing the Resolution

The Resolution answers three questions for our audience:

1. **What did we find?** Our answer to the question, in plain words.
2. **How sure are we?** What our data can't tell us.
3. **So what?** What it means, and what someone should do or investigate next.

For our example story, the Resolution might say:

> ARC Raiders' drop wasn't unusual for an extraction shooter. Almost every game in our comparison lost most of its players, and ARC Raiders held on to them longer than most before it fell. A PvE option didn't decide which games kept their players: Escape from Tarkov kept the most, but Gray Zone Warfare, which also has PvE, lost the most.
>
> We only compared six games, and the two with PvE had very different stories, so we can't say whether PvE helps. Both Escape from Tarkov and Gray Zone Warfare had big jumps in players that look like updates. Next, we'd look at when each game released big updates, to see whether updates matter more than PvE.

### Being honest about limits

Every data story has **limitations**: things our data can't tell us, or decisions that might have changed our answer. Stating them doesn't weaken our story. It shows our audience we've thought carefully, which makes them trust the rest of it. Common limitations are:

- a **small sample**, like our six games
- **missing data**, like the 86% of games with no `Peak CCU`
- **cleaning decisions**, like turning 0s into nulls
- **relationships aren't causes**, as we saw in Lesson 12
- **time**: our data stops on 5 October 2026

Our notes in ***my_data_story.md*** from every lesson are where we'll find our limitations. That's why we wrote down every decision.

## Tidying the notebook

Our notebook is full of experiments: error demonstrations, test cells and charts we replaced. A finished story only keeps the cells that tell it.

1. Delete the cells we don't need, including the three cells from Lesson 13 that send requests to the API. Keep the cell that loads the saved history.
    - **Why:** our audience doesn't need our experiments, and the API cells would send new requests every time the notebook runs.
    - **Expected result:** every remaining cell runs without errors.
2. Add a Markdown cell before each chart, explaining what it shows and why it matters. Follow the story arc: Hook, Behind the Scenes, Rising Insights, Aha Moment, Resolution.
    - **Why:** each chart needs words to turn it into evidence.
3. Drag cells into story order using the handle (⋮⋮) on the left of each cell. Put the Hook cell at the top.
    - **Why:** marimo runs cells in the order their variables need, not the order they're shown, so we can arrange them in the order our audience should read them.
    - **Expected result:** reading from top to bottom tells the story.

!!! tip "Behind the Scenes in a few lines"
    Our audience doesn't need to see the cleaning, but they should know it happened. One short Markdown cell, with the summary we wrote in Lesson 8, covers our whole Behind the Scenes stage. Don't forget the attribution from Lesson 4.

## App view

Press ++ctrl+period++ (++cmd+period++ on a Mac) to switch to **app view**. marimo hides all the code and shows only the outputs: our words, tables, charts and controls, in order. Press it again to go back to the code.

<!-- SCREENSHOT: assets/l16_app_view.png — the finished story in app view, code hidden -->

Read our whole story in app view, as if we'd never seen it before. Does every chart have words explaining it? Does the Aha chart stand out? Is anything still confusing?

## Publishing

There are two ways to share our finished story.

### Presenting it live

To present our story to the class with the interactive controls working, stop marimo, then type the command below in the terminal and press ++enter++.

```text
marimo run steam_story.py
```

- **Why:** `marimo run` opens the notebook as an **app**: outputs only, with no code, and nothing can be edited.
- **Expected result:** a browser tab opens showing our story. The menu and slider still update the chart.

Stop it with ++ctrl+c++ when we're finished.

### Sharing a file

To give someone a file they can open in any web browser, type the command below in the terminal and press ++enter++.

```text
marimo export html steam_story.py -o my_data_story.html --no-include-code
```

- **Why:** this runs every cell, then saves all the outputs into one HTML file, ***my_data_story.html***. `--no-include-code` leaves our code out.
- **Expected result:** after a few seconds the terminal prompt comes back, and ***my_data_story.html*** appears in VS Code's Explorer panel. Double-click it in File Explorer (or Finder on a Mac) to open it in a web browser.

!!! warning "Controls don't work in the HTML file"
    The HTML file is a snapshot. The charts can still be hovered and zoomed, but the menu and slider won't change anything, because there's no Python running behind them. Make sure our story makes sense without them.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 16: Resolution` and record our answers under it.

1. Write our Resolution: what we found, how sure we are, and so what.
2. List at least three limitations of our story.
3. Turn our ***steam_story.py*** notebook into our finished data story, following every stage of the story arc, and export it as ***my_data_story.html***.
4. Read our story in app view and check it against this list:
    - the Hook asks a clear question
    - Behind the Scenes explains where the data came from, how we cleaned it, and its attribution
    - each Rising Insight has a chart with a headline title and words that explain it
    - the Aha chart makes the answer impossible to miss
    - the Resolution answers the question, states the limitations, and says what's next
