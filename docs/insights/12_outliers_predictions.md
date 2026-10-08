# 12. Outliers and Predictions

!!! learn "In this lesson we will learn"
    - how to find outliers with the interquartile range
    - how to decide whether to keep an outlier
    - how to make a simple prediction from a trend
    - how to check a prediction, and what to do when it's wrong

!!! terms "Terminology"
    - **interquartile range** – the distance between the 25% value and the 75% value, also called the IQR.
    - **upper fence** – the 75% value plus 1.5 times the interquartile range; values above it count as outliers.

## Introduction

In Lesson 10 our box plots showed dots beyond the whiskers: **outliers**. In this lesson we'll work out where those dots come from, and decide what to do about them. Then we'll use a trend to make a **prediction**, and find out how far we can trust it.

## Finding outliers

An **outlier** is a value far away from most of the others. One common way to find them uses the **interquartile range**, or **IQR**:

1. find the 25% value, **Q1**, and the 75% value, **Q3**
2. the IQR is the distance between them: **Q3 − Q1**
3. any value more than **1.5 × IQR** above Q3 is an outlier. This limit is called the **upper fence**

This is the same rule Plotly used to draw the dots on our box plots. Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/12_outliers_predictions/story15.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Add a new cell that shows `price_outliers` sorted by `Price`, most expensive first. What kinds of games are they?

??? note "Code explanation"
    - **line 1** → finds the 25% value of `Price`, using `quantile(0.25)`, and stores it in `q1`.
    - **line 2** → finds the 75% value and stores it in `q3`.
    - **line 3** → works out the upper fence: Q3 plus 1.5 times the IQR.
    - **line 4** → keeps only the games that cost more than the upper fence, and stores them in `price_outliers`.
    - **line 5** → shows the upper fence and the number of outliers.

The output is **(21.74, 438)**. Q1 is $1.49 and Q3 is $9.59, so any game over $21.74 counts as an outlier: 438 games.

Now let's see which group they belong to. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/12_outliers_predictions/story16.py"
```

??? note "Code explanation"
    - **line 1** → splits `price_outliers` into its two groups, counts the games in each, and sorts the result by `Group`.

| Group | Games |
| :-- | --: |
| Indie | 119 |
| Not Indie | 319 |

Most of the expensive outliers aren't Indie games. That explains what we saw in Lesson 8: these 319 games pull the mean price of the other games up much more than the median.

### Keep or remove?

Finding an outlier doesn't mean we should delete it. Let's think about this:

1. Is it a **mistake**, like a price of $9,999 typed by accident? Then we fix it or remove it.
2. Is it **real but unusual**, like a $69.99 sports game? Then it's part of the story, and we keep it.

Our 438 price outliers are real games at real prices, so we keep them. The IQR rule tells us which values to **look at**, not which ones to delete. And because we're using medians, a few expensive games can't distort our main finding.

## Making a prediction

In Lesson 8 we made `per_year`, which counts the games in our data from each year. From 2019 to 2024, the number of games went up and down but mostly grew. Can we use that to predict how many 2025 games our data should have? Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
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

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 12: Outliers and predictions` and record our answers under it.

1. Find the outliers in one number column our question uses. Record how many there are, and decide whether to keep them. Write down why.
2. If our question is about change over time, make a prediction and write down what it's based on.
3. Add any new limitations we've found to our list from Lesson 6.
