# 15. Publishing Our Data Story

!!! learn "In this lesson we will learn"
    - how to write the words of our story with `mo.md`
    - how to put numbers from our data into our text
    - how to be honest about the limitations of our story
    - how to tidy our notebook and check it in app view
    - how to hand in our story for the class server

!!! terms "Terminology"
    - **app view** – a way of showing a marimo notebook with the code hidden, so only the outputs and controls appear.
    - **class server** – a computer at school that runs everyone's notebooks so anyone on the school network can open them in a web browser.

## Introduction

Welcome to the **Resolution**, the last stage of our data story. The Resolution answers our question, says what the answer means, and is honest about what our data can't tell us.

So far our notebook is full of code, tables and charts that only make sense to us. Our audience needs something different: the story told in words, with only the charts that matter. marimo can show our notebook as an **app view**, which hides all the code and shows only the outputs. In this lesson we'll write the words of our story, tidy our notebook for the app view, then hand it in so it can run on the **class server**: a computer at school that runs everyone's notebooks so anyone on the school network can open them in a web browser.

## Writing with mo.md

In Lesson 1 we started writing ***my_data_story.md*** in **Markdown**, using `#` for headings, `**` for bold text and `-` for lists. marimo can turn Markdown into formatted text in our notebook, using `mo.md`.

Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/resolution/15_publishing/story23.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Rewrite the introduction so it hooks our audience in a different way, for example by starting with a surprising number.

??? note "Code explanation"
    - **line 1** → shows the text inside the brackets as formatted Markdown, using `mo.md`.
    - **line 2** → starts a string with three quotation marks, which lets the string go over many lines.
    - **line 3** → a level 1 heading, which is the title of our story.
    - **lines 5–7** → a paragraph that hooks our audience with the question.
    - **line 9** → a sentence that tells our audience what data we used.
    - **line 10** → ends the string.
    - **line 11** → closes the brackets.

The cell shows a large title and two paragraphs, with no code in sight. This is the **Hook** of our story, so it needs to go at the top of our notebook. Hover over the cell, then drag the dots on its left edge up to the very top of the notebook.

<!-- SCREENSHOT: assets/l15_drag_cell.png — marimo cell with the drag handle (dots) on its left edge highlighted -->

!!! tip "Cell order doesn't change our code"
    In marimo, the order of our cells doesn't change how our code runs. marimo works out which cells need which variables, and runs them in the right order. That means we can put our cells in whatever order tells our story best.

## Putting numbers in our text

Our story should use the numbers we found, such as the median review scores from Lesson 8. We could type them into our text, but if we fixed a mistake in our data or got a newer copy of it, the numbers in our text would be wrong. Instead, we'll take them straight from our data using an **f-string**. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/resolution/15_publishing/story24.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Add a sentence that uses the median prices from the `prices` table in Lesson 8.

??? note "Code explanation"
    - **line 1** → gets the first value in the `Median review score` column of `per_group`, which is the Indie group's score, and stores it in `indie_score`.
    - **line 2** → gets the second value, which is the other group's score, and stores it in `other_score`.
    - **line 3** → shows the text as formatted Markdown.
    - **line 4** → starts an f-string over many lines, so we can put variables inside `{ }`.
    - **line 5** → a level 2 heading that states this insight.
    - **lines 7–8** → a sentence that puts the values of `indie_score` and `other_score` into the text, in bold.
    - **line 9** → ends the string.
    - **line 10** → closes the brackets.

The text says **86.5%** and **83.2%**, the same numbers as our `per_group` table. If our data changes, the text changes with it.

Drag this cell so it sits just above the chart that shows the same finding. Each insight in our story gets its own `mo.md` cell like this one: a heading that states the insight, then a sentence or two with the numbers, then the chart.

!!! tip "Why [0] and [1]?"
    In Lesson 8 we sorted `per_group` by `Group`, so Indie is always the first row, `[0]`, and Not Indie is always the second, `[1]`. If we didn't sort it, the rows could come out in a different order each time, and our text could swap the two numbers.

## Being honest about limitations

A good Resolution answers our question, then tells our audience what our data **can't** tell them. These are the **limitations** we've been recording in ***my_data_story.md*** since Lesson 3. Being honest about them makes our story more trustworthy, not less. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/resolution/15_publishing/story25.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → shows the text as formatted Markdown.
    - **line 2** → starts a string over many lines.
    - **line 3** → a level 2 heading for our answer.
    - **lines 5–7** → a paragraph that answers our question in plain words.
    - **line 9** → a level 3 heading for our limitations.
    - **lines 11–12** → a list item about how we chose our groups.
    - **lines 13–14** → a list item about which games are in our data.
    - **line 15** → a list item about when our data was collected.
    - **lines 16–17** → a list item that reminds our audience a relationship isn't a cause.
    - **line 18** → ends the string.
    - **line 19** → closes the brackets.

Each limitation came from an earlier lesson: our groups from Lesson 7, the 500-review rule from Lesson 12, and relationship versus cause from Lesson 11. This cell is the end of our story, so leave it at the bottom of our notebook.

!!! warning "Limitations aren't excuses"
    A limitation explains what our audience should keep in mind, not why our story might be wrong. Write it as a fact ("we only used games with at least 500 reviews"), then say what it means ("which leaves out most small games").

## Tidying for our audience

In the app view, every cell that shows an output appears on the page. Right now that includes every working table we made along the way, like the `scored.select(...)` table from Lesson 7. Our audience doesn't need those.

Work through our notebook from top to bottom, and put our cells in story order:

| Story stage | What our audience sees |
| :-- | :-- |
| Hook | our title and question, in a `mo.md` cell |
| Behind the Scenes | one sentence about our data, in the Hook's `mo.md` cell |
| Rising Insights | for each insight, a `mo.md` cell with a heading and the numbers, then its chart |
| Aha Moment | our Aha chart, then our UI elements and explore chart |
| Resolution | what we found and our limitations, in a `mo.md` cell |

For every other cell, ask: **does our audience need to see this?** If not, delete the last line of the cell, the one that shows the output. For example, change the cell that makes `per_group` so it ends at the closing bracket, without the `per_group` line underneath. The variable is still made, so every cell that uses it still works. It just isn't shown.

!!! warning "Delete the line, not the cell"
    Only delete the line that **shows** a table. If we delete the whole cell, its variable disappears, and every cell that uses it stops with an error.

## Checking the app view

Let's see our story the way our audience will.

1. Click in the VS Code terminal, press ++ctrl+c++, type `y` and press ++enter++.
    - **Why:** we need to stop editing before we run the notebook as an app.
    - **Expected result:** the terminal shows the `(.venv)` prompt again.
2. In the terminal, type the command below and press ++enter++.

    ```text
    marimo run steam_story.py
    ```

    - **Why:** `marimo run` opens our notebook in app view, with the code hidden.
    - **Expected result:** a new browser tab opens with our story: our title, text, charts and controls, and no code.

![marimo app view showing the title "Do Indie games review better?", two paragraphs, the heading "Players like Indie games more" with the sentence "The typical Indie game gets 86.5% positive reviews, compared with 83.2% for other games.", and the box plot from Lesson 10 below it](../assets/l15_app_view.png)

Read our story from top to bottom as if we've never seen it before. Try the slider and the dropdown. If anything is out of order, confusing or still showing a working table, stop `marimo run` with ++ctrl+c++, go back to `marimo edit steam_story.py`, fix it, and check again.

## Getting ready for the class server

There's one more change to make before our notebook can run on the class server. In Lesson 7 we loaded our data with the path `"data/clean_games.parquet"`. Python looks for that path starting from the folder marimo was **started** in. On our computer, that's our project folder, so it works. But the class server starts marimo in a different folder, so it can't find our data, and our story would show a blank page.

`mo.notebook_dir()` gives the folder our notebook is saved in, wherever that is. Go to the cell that loads `clean_games.parquet` and change it to match the code below. Then run it.

```python linenums="1" title="steam_story.py" hl_lines="1"
--8<-- "examples/resolution/15_publishing/story02.py"
```

??? note "Code explanation"
    - **line 1** → loads ***clean_games.parquet*** from the ***data*** folder next to our notebook, using `mo.notebook_dir()`, so it works on any computer.
    - **line 2** → shows `games` as the cell's output.

Nothing seems to change: `games` still has **10250** rows and **10** columns. The difference only shows up when our notebook runs somewhere else. While we're here, delete the `games` line too, because our audience doesn't need to see the raw table.

## Handing in our story

The class server needs two files, in the same folders as on our computer:

```text
steam_data_stories/
    steam_story.py
    data/
        clean_games.parquet
```

Our teacher will tell us how to hand them in. Once our story is on the class server, our teacher will give us its address, such as `http://192.168.1.50:2718`. Open it in a web browser and we'll see a card for each person's story, labelled with their name. Click ours to open it in app view.

![marimo home page listing the stories on the class server, with a card for each student's folder, each labelled with the student's name and Steam Story](../assets/class_server_home.png)

!!! warning "Check before handing in"
    Before we hand in, check that our story opens with `marimo run steam_story.py` and shows no errors, that the notebook is still called ***steam_story.py***, and that ***clean_games.parquet*** is inside the ***data*** folder. If the class server can't find our data, our story shows an empty page.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 15: Publishing` and record our answers under it.

1. Write the `mo.md` cells for our story: a Hook, a heading and sentence for each insight, and a Resolution with our limitations. Use an f-string for at least two numbers.
2. Check our story with `marimo run`, then ask someone else to read it in app view. Could they follow our story without us explaining it? Record what they said, and what we changed.
3. Change the cell that loads our data to use `mo.notebook_dir()`, then hand in our story. Record the address of our story on the class server.
