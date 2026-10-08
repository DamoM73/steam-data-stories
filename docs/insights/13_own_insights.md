# 13. Our Own Insights

!!! learn "In this lesson we will learn"
    - how to plan the insights for our own data story
    - how to reuse the patterns from Lessons 7–12
    - how to check that each insight is ready for our audience

## Introduction

In Lessons 7 to 12 we built up the evidence for our example story one piece at a time. Along the way, the **Our data story** tasks asked us to try each step on our own question. This lesson is different: there's no new code. Instead, we'll pull our own work together into a set of Rising Insights that lead up to our Aha Moment in Lesson 14.

## Our example story so far

Let's look back at the insights we found for our example question, **Do Indie games review as well as games from big studios, and do they cost less?**

| Insight | Evidence | Lesson |
| :-- | :-- | :-- |
| the typical Indie game gets more positive reviews | median review score 86.5 vs 83.2 | 8 |
| Indie games cost less | median price $3.84 vs $4.99 | 8 |
| a bigger share of Indie games get very high scores | histogram by group, as percentages | 9 |
| the whole spread of Indie scores sits higher | box plot | 10 |
| the gap has lasted every year since 2018 | line chart by year | 11 |
| price isn't related to review score | scatter plot | 11 |
| our data has fewer recent games | 2025 prediction check | 12 |

Notice how each insight builds on the one before. The first is a single number, the next few show the same finding in more detail, and the line chart shows it's not a one-off. The last row is a limitation, which we'll need in our Resolution.

## Planning our insights

Open ***my_data_story.md*** and read back through our notes from Lessons 3 to 12. Then add a new heading `## Lesson 13: Our insights` and plan **three to five** insights in a table like this one:

```text title="my_data_story.md"
| Insight | Summary or chart | Columns | Done? |
| :-- | :-- | :-- | :-- |
| ... | ... | ... | ... |
```

For each insight, write:

1. **Insight:** what we expect to find, in one sentence
2. **Summary or chart:** which pattern from the table below we'll use
3. **Columns:** which columns it needs
4. **Done?:** leave this empty until the insight is finished

!!! tip "Start with a number, end with a chart"
    A good order is: one summary table that gives the headline number, then one or two charts that show the same finding in more detail, then a trend or relationship that makes it stronger.

## Patterns we can reuse

Every insight in our example came from one of these patterns. Copy the pattern from the lesson, then change the column names and variable names for our own question.

| To find… | Pattern | Lesson |
| :-- | :-- | :-- |
| a new column from other columns | `with_columns(... .alias("New name"))` | [7](07_new_columns.md#calculating-a-review-score) |
| a label for each group | `pl.when(...).then(...).otherwise(...)` | [7](07_new_columns.md#years-and-groups) |
| a summary of each group | `group_by("Group").agg(...)` | [8](08_summarising_groups.md#comparing-our-two-groups) |
| a comparison of one number | `px.bar` | [9](09_bar_histogram.md#bar-charts) |
| how values are spread out | `px.histogram`, with `histnorm="percent"` for groups | [9](09_bar_histogram.md#comparing-two-groups) |
| how spread compares between groups | `px.box` | [10](10_better_charts.md#box-plots) |
| a change over time | `group_by("Release year", ...)` then `px.line` | [11](11_trends_relationships.md#trends-over-time) |
| a relationship between two numbers | `px.scatter` | [11](11_trends_relationships.md#looking-for-a-relationship) |
| unusual values | the IQR upper fence | [12](12_outliers_predictions.md#finding-outliers) |

!!! warning "One variable, one cell"
    When we copy a pattern, give every new variable a new name, like `per_genre` instead of `per_group`. Remember from Lesson 2: if two cells create the same variable, marimo stops both of them with a `MultipleDefinitionError`.

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
3. **Right chart:** the chart type matches the question, using the table from [Lesson 10](10_better_charts.md#choosing-a-chart).
4. **Headline title:** the title states the finding, and the finding is true.
5. **Clear labels:** the axes and legend use words our audience understands.
6. **Honest claim:** we say "is related to", not "causes", unless we have much stronger evidence.

## Checking with a partner

When our insights are ready, swap notebooks with a partner. For each of their insights:

1. Read only the chart title and look at the chart for ten seconds. Write down what the chart seems to show.
2. Check it against the list above.
3. Give them one thing that works well and one thing to improve.

Then use their feedback on our own insights.

## Our data story

Under the `## Lesson 13: Our insights` heading in ***my_data_story.md***:

1. Make sure every insight in our table is done, with a one-sentence finding that includes a number.
2. Record the feedback from our partner, and what we changed because of it.
3. Choose the **one** insight that best answers our question. That's the one we'll turn into our Aha Moment in Lesson 14.
