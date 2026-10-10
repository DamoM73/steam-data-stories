# 12. Outliers and Predictions

!!! learn "In this lesson we will learn"
    - how to find outliers with the interquartile range
    - how to decide whether to keep an outlier
    - how to make a simple prediction from a trend
    - how to check a prediction, and what to do when it's wrong

!!! terms "Terminology"
    - **quartile** – one of the three values that split sorted data into four equal parts: Q1 (25%), the median (50%) and Q3 (75%).
    - **interquartile range** – the distance between the first quartile (Q1) and the third quartile (Q3), also called the IQR.
    - **upper fence** – Q3 plus 1.5 times the interquartile range; values above it count as outliers.

## Introduction

When we drew box plots, they showed dots beyond the whiskers: **outliers**. In this lesson we'll work out where those dots come from, and decide what to do about them. Then we'll use a trend to make a **prediction**, and find out how far we can trust it.

## Finding outliers

An **outlier** is a value far away from most of the others. We'll look for outliers in `Price`, because when we compared the mean and median prices, the big gap between them hinted that a few very expensive games were pulling the mean up.

### Quartiles

To decide what counts as "far away", we first need to know where most of the values are. Imagine lining up all 10,250 games from cheapest to most expensive, then cutting the line into four equal parts. The prices at the cuts are called **quartiles**:

- **Q1**, the first quartile, is the price a quarter of the way along the line. 25% of games cost this much or less.
- the median is halfway along. 50% of games cost this much or less.
- **Q3**, the third quartile, is three quarters of the way along. 75% of games cost this much or less.

The middle half of the games, the "normal" prices, sit between Q1 and Q3. That's exactly the box we saw in our box plots: the bottom of the box is Q1, and the top is Q3.

### The interquartile range

The **interquartile range**, or **IQR**, is the distance between Q3 and Q1: **IQR = Q3 − Q1**. It tells us how spread out the middle half of the values are. If most games cost about the same, the IQR is small. If prices vary a lot, it's big.

### The upper fence

A value counts as an outlier if it's more than **1.5 × IQR** above Q3. That limit is called the **upper fence**:

**upper fence = Q3 + 1.5 × IQR**

Why this formula?

- **we start at Q3**, the top of the normal range, because we're looking for values that are unusually **high**. (There's also a lower fence, Q1 − 1.5 × IQR, for unusually low values. No game costs less than $0, so we don't need it for prices.)
- **we measure the distance in IQRs** rather than in dollars, so the fence suits the data. If prices were tightly bunched, the fence would be close to Q3; because they're spread out, it's further away. The same rule works for prices, review scores or anything else.
- **we use 1.5** because the statistician John Tukey chose it when he invented the box plot. It's far enough out that ordinary variation stays inside the fence, so only values well beyond the usual spread get flagged. For data shaped like a bell curve, fewer than 1 in 100 values land outside the fences.

This is the same rule Plotly used to draw the dots on our box plots.

In our code, we'll work out Q1 and Q3 with `quantile`, which finds the value a given fraction of the way along the sorted column: `0.25` for a quarter and `0.75` for three quarters. Then line 3 turns the formula above into Python: `q3 - q1` is the IQR, so `q3 + 1.5 * (q3 - q1)` is the upper fence. Finally we keep the games above the fence and count them. Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="steam_story.py — new cell"
--8<-- "examples/insights/12_outliers_predictions/story15.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change `"Price"` to `"Review score"` on lines 1, 2 and 4. What is the upper fence for review scores? How many games are above it, and why?

??? note "Code explanation"
    - **line 1** → finds the 25% value of `Price`, using `quantile(0.25)`, and stores it in `q1`.
    - **line 2** → finds the 75% value and stores it in `q3`.
    - **line 3** → works out the IQR with `q3 - q1`, multiplies it by 1.5, and adds it to Q3 to get the upper fence.
    - **line 4** → keeps only the games that cost more than the upper fence, and stores them in `price_outliers`.
    - **line 5** → shows the upper fence and the number of outliers.

The output is **(21.74, 438)**. Q1 is $1.49 and Q3 is $9.59, so the IQR is $8.10, and the upper fence is $9.59 + 1.5 × $8.10 = $21.74. Any game over $21.74 counts as an outlier: 438 games.

### Checking the outliers

Before we decide anything about these 438 games, we need to know whether their prices are **real**. A price of $9,999 would be a typing mistake, not an expensive game. The quickest check is to look at the most expensive ones: if the biggest prices are believable, the rest must be too. So we'll sort `price_outliers` from most expensive to cheapest, and show just the columns we need to recognise each game. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py — new cell"
--8<-- "examples/insights/12_outliers_predictions/story15b.py"
```

??? note "Code explanation"
    - **line 1** → sorts `price_outliers` by `Price`, most expensive first, using `descending=True`, then shows only the `AppID`, `Name`, `Price` and `Group` columns.

The most expensive games in our data cost **$69.99**, and they're games like Microsoft Flight Simulator 2024, EA SPORTS FC™ 25 and NBA 2K25. That's the normal full price for a new game from a big studio, so these prices are real. Scroll to the end of the table: the cheapest outliers cost about $22. There are no impossible prices, like a negative price or thousands of dollars.

!!! tip "Look at the extremes"
    When checking outliers, always look at the most extreme values first. If the most extreme value is believable, the less extreme ones almost certainly are too. If it isn't, we've found a mistake to fix in ***clean_steam.py***.

Now let's see which group the outliers belong to. We'll group them by `Group` and count them, just like we did for all our games. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py — new cell"
--8<-- "examples/insights/12_outliers_predictions/story16.py"
```

??? note "Code explanation"
    - **line 1** → splits `price_outliers` into its two groups, counts the games in each, and sorts the result by `Group`.

| Group | Games |
| :-- | --: |
| Indie | 119 |
| Not Indie | 319 |

Most of the expensive outliers aren't Indie games. That explains what we saw when we compared the mean and median prices: these 319 games pull the mean price of the other games up much more than the median.

### Keep or remove?

Finding an outlier doesn't mean we should delete it. Let's think about this:

1. Is it a **mistake**, like a price of $9,999 typed by accident? Then we fix it or remove it.
2. Is it **real but unusual**, like a $69.99 sports game? Then it's part of the story, and we keep it.

We checked our 438 price outliers: they're real games at real prices, so we keep them. The IQR rule tells us which values to **look at**, not which ones to delete. And because we're using medians, a few expensive games can't distort our main finding.

## Making a prediction

When we summarised groups, we made `per_year`, which counts the games in our data from each year. From 2019 to 2024, the number of games went up and down but mostly grew. Can we use that to predict how many 2025 games our data should have?

A simple way to predict is to assume the next year changes by the same amount as an average year did. So we'll take the years from 2019 to 2024, work out how much the count changed from each year to the next with `diff`, and find the average of those changes. Then we add the average change to the 2024 count. We use only recent years because the way people make and review games has changed a lot since 2010, and recent years are more like 2025. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py — new cell"
--8<-- "examples/insights/12_outliers_predictions/story17.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → keeps only the years from 2019 to 2024 in `per_year`, and stores them in `recent`.
    - **line 2** → works out how much the number of games changed from each year to the next, using `diff`, then finds the average change.
    - **line 3** → adds the average change to the last year's count, using `[-1]` to get the last value, to predict 2025.
    - **line 4** → shows the average growth and the prediction.

The output is **(30.0, 959.0)**. From 2019 to 2024, there were on average 30 more games each year than the year before, so we predict about **959** games from 2025.

### Checking our prediction

Now look back at `per_year`. Our data has only **424** games from 2025, less than half our prediction. Our prediction was way off. Why?

Remember that our data only includes games with at least 500 reviews. A game released in December 2025 has had far less time to collect reviews than a game from 2019, so many 2025 games haven't reached 500 yet. They exist, but they aren't in our data yet. So the low number probably isn't because fewer games came out in 2025. It's because of how our data was chosen.

That's a **limitation** worth telling our audience about: our data has fewer recent games, and the recent games it has are the ones that got popular quickly.

!!! warning "Predictions are guesses with reasons"
    A prediction assumes the future will behave like the past. When it doesn't, that's not a failure: finding out **why** often teaches us something important about our data. When we put a prediction in our story, we say what it's based on, and we check it if we can.

## Your data story

Open ***my_data_story.md***, add a new heading `## Outliers and predictions` and record your answers under it.

1. Find the outliers in one number column your question uses. Record how many there are.
2. Sort the outliers so the most extreme come first, and check that their values are real. Decide whether to keep them, and write down why.
3. If your question is about change over time, make a prediction and write down what it's based on.
4. Add any new limitations you've found to your list under `## Clean data`.
