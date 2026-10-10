# 13. Our Own Insights

!!! learn "In this lesson we will learn"
    - how to plan the insights for our own data story
    - how to reuse the patterns we've learned for finding insights
    - how to check that each insight is ready for our audience

## Introduction

Since we made our story notebook, we've built up the evidence for our example story one piece at a time. Along the way, the **Your data story** tasks asked you to try each step on your own question. This lesson is different: there's no new code. Instead, we'll pull our own work together into a set of Rising Insights that lead up to our Aha Moment.

## Our example story so far

Let's look back at the insights we found for our example question, **Do Indie games review as well as games from big studios, and do they cost less?**

| Insight | Evidence | Where we found it |
| :-- | :-- | :-- |
| the typical Indie game gets more positive reviews | median review score 86.5 vs 83.2 | [Summarising Groups](08_summarising_groups.md) |
| Indie games cost less | median price US$3.84 vs US$4.99 | [Summarising Groups](08_summarising_groups.md) |
| a bigger share of Indie games get very high scores | histogram by group, as percentages | [Bar Charts and Histograms](09_bar_histogram.md) |
| the whole spread of Indie scores sits higher | box plot | [Box Plots and Better Charts](10_better_charts.md) |
| the gap has lasted every year since 2017 | line chart by year | [Trends and Relationships](11_trends_relationships.md) |
| price isn't related to review score | scatter plot | [Trends and Relationships](11_trends_relationships.md) |
| our data has fewer recent games | 2025 prediction check | [Outliers and Predictions](12_outliers_predictions.md) |

Notice how each insight builds on the one before. The first is a single number, the next few show the same finding in more detail, and the line chart shows it's not a one-off. The last row is a limitation, which we'll need in our Resolution.

## Planning our insights

Open ***my_data_story.md*** and read back through your notes, from `## Choosing a question` onwards. Then add a new heading `## My insights` and plan **three to five** insights in a table like this one:

```text title="my_data_story.md"
| Insight | Summary or chart | Columns | Done? |
| :-- | :-- | :-- | :-- |
| ... | ... | ... | ... |
```

For each insight, write:

1. **Insight:** what you expect to find, in one sentence
2. **Summary or chart:** which pattern from the table below you'll use
3. **Columns:** which columns it needs
4. **Done?:** leave this empty until the insight is finished

!!! tip "Start with a number, end with a chart"
    A good order is: one summary table that gives the headline number, then one or two charts that show the same finding in more detail, then a trend or relationship that makes it stronger.

## Patterns we can reuse

Every insight in our example came from one of these patterns. Copy the pattern from the page where we learned it, then change the column names and variable names for your own question.

| Name | To find… | Pattern | Where we learned it |
| :-- | :-- | :-- | :-- |
| new column | a new column from other columns | `with_columns(... .alias("New name"))` | [Calculating a review score](07_new_columns.md#calculating-a-review-score) |
| group label | a label for each group | `pl.when(...).then(...).otherwise(...)` | [Years and groups](07_new_columns.md#years-and-groups) |
| group summary | a summary of each group | `group_by("Group").agg(...)` | [Comparing our two groups](08_summarising_groups.md#comparing-our-two-groups) |
| bar chart | a comparison of one number | `px.bar` | [Bar charts](09_bar_histogram.md#bar-charts) |
| histogram | how values are spread out | `px.histogram`, with `histnorm="percent"` for groups | [Comparing two groups](09_bar_histogram.md#comparing-two-groups) |
| box plot | how spread compares between groups | `px.box` | [Box plots](10_better_charts.md#box-plots) |
| line chart | a change over time | `group_by("Release year", ...)` then `px.line` | [Trends over time](11_trends_relationships.md#trends-over-time) |
| scatter plot | a relationship between two numbers | `px.scatter` | [Looking for a relationship](11_trends_relationships.md#looking-for-a-relationship) |
| outliers | unusual values | the IQR upper fence | [Finding outliers](12_outliers_predictions.md#finding-outliers) |

!!! warning "One variable, one cell"
    When we copy a pattern, give every new variable a new name, like `per_genre` instead of `per_group`. Remember from when we explored our data: if two cells create the same variable, marimo stops both of them with a `MultipleDefinitionError`.

## Building our insights

Work through our plan one insight at a time:

1. Add a Markdown heading to ***my_data_story.md*** for the insight.
2. Build the summary or chart in ***steam_story.py***.
3. Check it against the list below, and fix anything that doesn't pass.
4. Record the finding in one sentence, with a number, in ***my_data_story.md***, and tick it off in our table.

!!! primm "PRIMM"
    For each insight, **predict** what we'll find before we build it, and write the prediction down. When we **run** it, compare the result with our prediction. A result that surprises us is often the most interesting part of our story.

## Checking each insight

Before an insight goes into our story, it should pass every check:

1. **Enough data:** every group has plenty of rows. Check the counts, and leave out tiny groups.
2. **Right average:** we chose the mean or the median on purpose, and can say why.
3. **Right chart:** the chart type matches the question, using the table in [Choosing a chart](10_better_charts.md#choosing-a-chart).
4. **Headline title:** the title states the finding, and the finding is true.
5. **Clear labels:** the axes and legend use words our audience understands.
6. **Honest claim:** we say "is related to", not "causes", unless we have much stronger evidence.

## Checking with a partner

When our insights are ready, swap notebooks with a partner. For each of their insights:

1. Read only the chart title and look at the chart for ten seconds. Write down what the chart seems to show.
2. Check it against the list above.
3. Give them one thing that works well and one thing to improve.

Then use their feedback on our own insights.

## Your data story

Under the `## My insights` heading in ***my_data_story.md***:

1. Make sure every insight in your table is done, with a one-sentence finding that includes a number.
2. Record the feedback from your partner, and what you changed because of it.
3. Choose the **one** insight that best answers your question. That's the one you'll turn into your Aha Moment.
