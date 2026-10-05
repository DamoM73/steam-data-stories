# 3. Asking a Question Data Can Answer

!!! learn "In this lesson we will learn"
    - what makes a question investigable
    - how to define the words in our question
    - how to use `describe` and `value_counts` to check a question against the data
    - how to refine a question that's too broad or can't be answered

## Introduction

In Lesson 1 we wrote a question for our own data story, and in Lesson 2 we explored the columns that might answer it. Now we need to check that our question is one the data can actually answer. A great question that the data can't answer leads to a story with no evidence, and a story with no evidence isn't a data story.

## Investigable questions

An **investigable question** is a question we can answer by collecting and analysing data. Good investigable questions are:

- **specific:** it's clear exactly what we're looking at
- **measurable:** the answer comes from columns we actually have
- **open:** the answer isn't obvious before we look

Let's compare some questions about Steam games:

| Question | Investigable? | Why |
| :-- | :-- | :-- |
| What's the best game on Steam? | no | "best" isn't measurable; best for who? |
| Are games getting more expensive? | almost | which games, and since when? |
| Has the median price of Steam games changed between 2015 and 2025? | yes | specific, measurable with `Price` and `Release date`, and the answer isn't obvious |
| Do people like indie games? | no | "like" isn't measurable as it stands |
| Do games tagged Indie get a higher share of positive reviews than other games? | yes | uses `Tags`, `Positive` and `Negative` |

### Example questions

Here are some investigable questions about the Steam data:

- Has the number of games released on Steam each year kept growing?
- Do free games get more recommendations than paid games?
- Do games that support more languages get more recommendations?
- Which genres have the longest median playtime?
- Are games released on Mac and Linux as well as Windows becoming more common?
- Do games with achievements get more recommendations than games without them?

!!! primm "PRIMM"
    Time to **modify** some questions. Can you write two more investigable questions about the Steam data? For each one, write down which columns would answer it.

## Defining our terms

Even a specific question can hide a word that means different things to different people. Our example question is:

> **Was ARC Raiders' drop in players unusual?**

To answer it, we need to decide exactly what our words mean:

1. **"drop in players"** → how far the number of people playing at the same time falls from its highest point, month by month after launch
2. **"unusual"** → different from games like it: other **extraction shooters**, where players fight their way into an area, grab loot and try to get out alive
3. **"games that let us play without fighting other players"** → games with a **PvE** option. **PvE** means **player versus environment**: we only fight computer-controlled enemies. ARC Raiders is **PvPvE**: we fight computer enemies *and* other players.

Steam doesn't have a column that says whether a game has a PvE option, so we'll record it ourselves, from what each game's makers have said. Writing down our sources means anyone can check our decisions:

| Game | PvE option | Source |
| :-- | :-- | :-- |
| ARC Raiders | No | [PC Gamer](https://www.pcgamer.com/games/third-person-shooter/arc-raiders-is-finally-testing-a-pve-only-mode-we-cant-ignore-what-the-data-is-telling-us/) |
| Marathon | No | [Wikipedia](https://en.wikipedia.org/wiki/Marathon_(2026_video_game)) |
| Escape from Tarkov | Yes | [Wikipedia](https://en.wikipedia.org/wiki/Escape_from_Tarkov) |
| Gray Zone Warfare | Yes | [Steam Community](https://steamcommunity.com/app/2479810/discussions/0/4355620303679362648/) |
| Arena Breakout: Infinite | Added later | [Willy B Gamer](https://www.willybgamer.com/intel/arena-breakout-infinite-permanent-pve-mode/) |
| Escape from Duckov | Single-player | [Wikipedia](https://en.wikipedia.org/wiki/Escape_from_Duckov) |

Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our cells from Lesson 2. Then add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/hook/03_asking_questions/cell07.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **lines 1–2** → start creating a new DataFrame called `story_games` from a dictionary, where each key is a column name and each value is a list holding that column's values.
    - **line 3** → creates the `AppID` column, holding the Steam AppID of each of our six games.
    - **lines 4–11** → create the `Name` column, holding the name of each game in the same order as the AppIDs.
    - **line 12** → creates the `PvE` column, holding the PvE option we decided on for each game.
    - **lines 13–14** → close the dictionary and finish creating the DataFrame.
    - **line 15** → shows `story_games` as the cell's output.

<!-- SCREENSHOT: assets/l03_story_games.png — the story_games DataFrame in marimo -->

!!! warning "Keep the lists in order"
    Each list must have the same number of values, in the same order. The fourth AppID belongs with the fourth name and the fourth PvE value. If one list is a different length, Polars stops with an error.

## Checking our question against the data

Now let's check that the columns we need hold useful values. Polars gives us two quick ways to do this.

### Summary statistics

Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/hook/03_asking_questions/cell08.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → calculates **summary statistics** for every column of `games` and shows them as a table.

<!-- SCREENSHOT: assets/l03_describe.png — the output of games.describe() -->

Each row of the output is one statistic:

| Statistic | What it tells us |
| :-- | :-- |
| **count** | how many values the column has |
| **null_count** | how many values are missing |
| **mean** | the average |
| **std** | the standard deviation: how spread out the values are |
| **min** and **max** | the smallest and largest values |
| **25%**, **50%**, **75%** | the values a quarter, half and three-quarters of the way through, when the values are sorted. The **50%** value is the **median**: the middle value. |

Let's think about what the numbers tell us:

1. The median `Price` is 2.72, but the maximum is 999.99. A few very expensive items pull the mean up to about 5.01. When the mean and median are this far apart, the median gives a fairer picture of a "typical" game.
2. The median, and even the 75% value, of `Peak CCU` is 0. Three-quarters of games had nobody playing at their busiest time? That's very unlikely. It's a clue that this column has values that really mean "missing", which we'll investigate in Lesson 7.
3. `Metacritic score` has a median of 0 too. Metacritic only reviews some games, so a 0 here probably means "no score", not a terrible score.

### Counting values

`describe` is great for number columns, but many of our columns hold text. For those, we count how often each value appears. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/hook/03_asking_questions/cell09.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change `"Estimated owners"` to `"Required age"` and run it again. What do you notice?

??? note "Code explanation"
    - **line 1** → picks the `Estimated owners` column from `games`, counts how many times each different value appears, and sorts the results from most common to least common.

<!-- SCREENSHOT: assets/l03_value_counts.png — the output of value_counts for Estimated owners -->

The most common value is `0 - 20000`, with 74,121 games, and the next is `0 - 0`, with 38,991 games. Let's think about this:

1. `Estimated owners` isn't a number at all. It's a range, stored as text.
2. `0 - 0` means a game with no owners at all, which is very unlikely for a game on sale. Like `Peak CCU`, it suggests missing data.
3. ARC Raiders is in the `0 - 20000` group, even though hundreds of thousands of people played it at once.

So `Estimated owners` and `Peak CCU` can't tell us how popular recent games are. That's why our example story will need a second source of data: the player history we'll get in Lesson 13.

!!! tip "Square brackets pick one column"
    `games["Estimated owners"]` picks a single column from a DataFrame. A single column is called a **Series**. Many methods, like `value_counts`, work on a Series rather than a whole DataFrame.

## Refining our question

If the data can't answer our question, we don't give up on it: we **refine** it. Common fixes are:

- **narrow it down:** "Are games getting more expensive?" → "Has the median price of Steam games changed between 2015 and 2025?"
- **swap in a column that works:** if `Peak CCU` is missing for the games we care about, use `Recommendations` or `Positive` and `Negative` instead
- **define the fuzzy words:** "popular" → "has more than 1,000 recommendations"
- **add another source:** like our example story, which adds player history

Our refined example question is:

> **Did ARC Raiders lose a bigger share of its peak players, month by month after launch, than other extraction shooters, and do extraction shooters with a PvE option keep a bigger share of their players?**

It's longer, but every part of it can be measured.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 3: Our question` and record our answers under it.

1. Check our own question against the three features of an investigable question. Rewrite it if it isn't specific, measurable and open.
2. Write down what each fuzzy word in our question means, like we did for "unusual" and "PvE".
3. Use `describe` and `value_counts` on the columns our question needs. Do they have enough real values to answer it?
4. If they don't, refine our question using one of the fixes above.
5. Finish with our final question on its own line, so it's easy to find later.
