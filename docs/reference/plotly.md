# Plotly Express

!!! learn "On this page we will learn"
    - the Plotly Express charts used in this course
    - the options we use to make charts clear
    - how to design a chart that tells a story

**Plotly Express** draws a whole interactive chart from a DataFrame in one function call. We import it with `import plotly.express as px`. It needs **NumPy** to draw charts from Polars data, which we installed in [Setting Up](../start/setup.md#install-the-libraries).

## Choosing a chart

| Our question | Chart | Function | Where we learned it |
| :-- | :-- | :-- | :-- |
| how does one number compare across groups? | bar chart | `px.bar` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#bar-charts) |
| how are values spread out? | histogram | `px.histogram` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#histograms) |
| how does the spread compare between groups? | box plot | `px.box` | [Box Plots and Better Charts](../insights/10_better_charts.md#box-plots) |
| how does something change over time? | line chart | `px.line` | [Trends and Relationships](../insights/11_trends_relationships.md#trends-over-time) |
| are two number columns related? | scatter plot | `px.scatter` | [Trends and Relationships](../insights/11_trends_relationships.md#looking-for-a-relationship) |

## A basic chart

Every Plotly Express chart starts the same way: the data, then which columns go where.

```python title="steam_story.py"
px.bar(
    per_group,
    x="Group",
    y="Median review score",
    title="Median review score of Indie and other games",
)
```

In marimo, a chart that's the last value in a cell is shown as the cell's output.

## Options

| Option | What it does | Example | Where we learned it |
| :-- | :-- | :-- | :-- |
| `x` | the column for the x-axis, along the bottom | `x="Group"` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#bar-charts) |
| `y` | the column for the y-axis, up the side | `y="Median review score"` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#bar-charts) |
| `title` | the chart's title | `title="Indie games get a higher share of positive reviews"` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#bar-charts) |
| `nbins` | about how many bins a histogram has | `nbins=45` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#histograms) |
| `color` | a different colour for each group | `color="Group"` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#comparing-two-groups) |
| `barmode` | draws the groups' bars over the top of each other | `barmode="overlay"` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#comparing-two-groups) |
| `histnorm` | shows each bar as a percentage of its own group | `histnorm="percent"` | [Bar Charts and Histograms](../insights/09_bar_histogram.md#comparing-two-groups) |
| `category_orders` | sets the order of the groups | `category_orders={"Group": ["Indie", "Not Indie"]}` | [Box Plots and Better Charts](../insights/10_better_charts.md#making-a-chart-better) |
| `labels` | replaces column names on the axes and legend | `labels={"Review score": "Positive reviews (%)"}` | [Box Plots and Better Charts](../insights/10_better_charts.md#making-a-chart-better) |
| `markers` | draws a dot on each point of a line | `markers=True` | [Trends and Relationships](../insights/11_trends_relationships.md#trends-over-time) |
| `hover_name` | the column shown in bold when we hover over a mark | `hover_name="Name"` | [Trends and Relationships](../insights/11_trends_relationships.md#looking-for-a-relationship) |
| `opacity` | how solid each mark is, from 0 to 1 | `opacity=0.4` | [Trends and Relationships](../insights/11_trends_relationships.md#looking-for-a-relationship) |
| `color_discrete_map` | chooses the colour for each group | `color_discrete_map={"Indie": "royalblue", "Not Indie": "lightgrey"}` | [The Aha Moment](../aha/14_aha_moment.md#making-one-line-stand-out) |

## Annotations

An **annotation** is a note on the chart, with an arrow pointing at a spot. Store the chart in a variable first, add the annotation, then show the chart:

```python title="steam_story.py"
aha_chart = px.line(per_year_group, x="Release year", y="Median review score")
aha_chart.add_annotation(x=2018, y=87.05, text="The gap starts here", ax=-120, ay=-40)
aha_chart
```

| Option | What it does |
| :-- | :-- |
| `x` and `y` | the point the arrow points to, in the chart's own units |
| `text` | the text of the note |
| `ax` | how many pixels left (negative) or right (positive) of the point the text goes |
| `ay` | how many pixels up (negative) or down (positive) from the point the text goes |

See [The Aha Moment](../aha/14_aha_moment.md#making-one-line-stand-out).

## Colours

Plotly understands colour names such as `"royalblue"`, `"darkorange"`, `"crimson"` and `"lightgrey"`. To make one group stand out, give it a strong colour and give everything else grey.

!!! warning "Colour blindness"
    Never use red against green as the only way to tell two groups apart. A strong colour against grey works for almost everyone.

## Using a chart

| Action | What it does |
| :-- | :-- |
| hover over a mark | shows its exact values |
| drag across the chart | zooms in |
| **Reset axes** (house icon) in the toolbar at the top right | zooms back out |
| click a name in the legend | hides or shows that group |
| camera icon in the top-right corner | downloads the chart as a PNG image |

## Designing a chart for a story

- **One message per chart.** Decide what the chart should say before we draw it.
- **Headline title.** Say what the chart shows, not what it is: "Indie games get a higher share of positive reviews", not "Review scores by group". See [Box Plots and Better Charts](../insights/10_better_charts.md#titles-that-tell).
- **Fair comparisons.** When groups are different sizes, compare percentages, not counts. See [Bar Charts and Histograms](../insights/09_bar_histogram.md#comparing-two-groups).
- **Use colour to point.** Highlight the finding, and make everything else grey. See [The Aha Moment](../aha/14_aha_moment.md#making-one-line-stand-out).
- **Clear labels.** Replace column names with words our audience understands.
- **Keep colours the same.** Give each group the same colour on every chart, so our audience doesn't have to read the legend each time.

!!! tip "The official documentation"
    The [Plotly Express documentation](https://plotly.com/python/plotly-express/){ target="_blank" rel="noopener" } has examples of every chart type.
