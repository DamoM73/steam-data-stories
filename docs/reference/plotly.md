# Plotly Express

!!! learn "On this page we will learn"
    - the Plotly Express charts used in this course
    - the options we use to make charts clear
    - how to design a chart that tells a story

**Plotly Express** draws a whole interactive chart from a DataFrame in one function call. We import it with `import plotly.express as px`. It needs **NumPy** to draw charts from Polars data, which we installed in [Setting Up](../start/setup.md#install-the-libraries).

## Choosing a chart

| Our question | Chart | Function | Lesson |
| :-- | :-- | :-- | :-- |
| how do groups compare? | bar chart | `px.bar` | [11](../insights/11_charts_compare.md#bar-charts) |
| how are values spread out? | histogram | `px.histogram` | [11](../insights/11_charts_compare.md#histograms) |
| how does the spread compare between groups? | box plot | `px.box` | [11](../insights/11_charts_compare.md#box-plots) |
| how does something change over time? | line chart | `px.line` | [12](../insights/12_trends_outliers.md#trends-over-time) |
| are two number columns related? | scatter plot | `px.scatter` | [12](../insights/12_trends_outliers.md#looking-for-a-relationship) |

## A basic chart

Every Plotly Express chart starts the same way: the data, then which columns go where.

```python title="steam_story.py"
px.bar(
    per_genre,
    x="Genres",
    y="Games",
    title="Indie is the most common genre on Steam",
)
```

In marimo, a chart that's the last value in a cell is shown as the cell's output.

## Options

| Option | What it does | Example | Lesson |
| :-- | :-- | :-- | :-- |
| `x` | the column for the x-axis, along the bottom | `x="Release year"` | [11](../insights/11_charts_compare.md#bar-charts) |
| `y` | the column for the y-axis, up the side | `y="Games"` | [11](../insights/11_charts_compare.md#bar-charts) |
| `title` | the chart's title | `title="Steam releases have boomed since 2013"` | [11](../insights/11_charts_compare.md#titles-that-tell) |
| `color` | a different colour for each group | `color="Name"` | [15](../aha/15_aha_moment.md#a-first-attempt) |
| `color_discrete_map` | chooses the colour for each group | `color_discrete_map={"ARC Raiders": "#D62728"}` | [15](../aha/15_aha_moment.md#designing-the-aha-chart) |
| `line_dash` | a different line style for each group | `line_dash="PvE"` | [15](../aha/15_aha_moment.md#letting-our-audience-explore) |
| `markers` | draws a dot on each point of a line | `markers=True` | [12](../insights/12_trends_outliers.md#trends-over-time) |
| `labels` | replaces column names on the axes and legend | `labels={"Month": "Months since launch"}` | [15](../aha/15_aha_moment.md#designing-the-aha-chart) |
| `category_orders` | sets the order of groups | `category_orders={"Price band": ["Free", "Under $10"]}` | [11](../insights/11_charts_compare.md#box-plots) |
| `nbins` | about how many bins a histogram has | `nbins=60` | [11](../insights/11_charts_compare.md#histograms) |
| `hover_name` | the column shown in bold when we hover | `hover_name="Name"` | [12](../insights/12_trends_outliers.md#looking-for-a-relationship) |
| `opacity` | how solid each mark is, from 0 to 1 | `opacity=0.4` | [12](../insights/12_trends_outliers.md#looking-for-a-relationship) |

## Annotations

An **annotation** is a note on the chart. Store the chart in a variable first, then add to it:

```python title="steam_story.py"
aha_chart = px.line(first_year, x="Month", y="Percent of peak", color="Name")
aha_chart.add_annotation(x=4, y=52, text="Half its peak after 4 months", showarrow=True)
aha_chart
```

`x` and `y` are the position of the point the arrow points to, in the chart's own units. See [Lesson 15](../aha/15_aha_moment.md#designing-the-aha-chart).

## Colours

Colours are written as **hex codes**: a `#` and six characters. These work well together:

| Colour | Hex code | Use for |
| :-- | :-- | :-- |
| red | `#D62728` | the thing we want our audience to look at |
| blue | `#1F77B4` | a second thing to compare with |
| light grey | `#BBBBBB` | context that shouldn't compete for attention |

!!! warning "Colour blindness"
    Never use red against green as the only way to tell two things apart. Red against grey or blue works for almost everyone.

## Using the chart

| Action | What it does |
| :-- | :-- |
| hover over a mark | shows its exact values |
| drag across the chart | zooms in |
| double-click | zooms back out |
| click a name in the legend | hides or shows that group |
| camera icon in the top right | downloads the chart as a PNG image |

## Designing a chart for a story

- **One message per chart.** Decide what the chart should say before drawing it.
- **Headline title.** Say what the chart shows, not what it is: "Indie is the most common genre on Steam", not "Games per genre".
- **Remove clutter.** Leave out rows and groups the message doesn't need, and say what we left out.
- **Use colour to point.** Highlight the finding, and make everything else grey.
- **Clear labels.** Replace column names with words our audience understands.

!!! tip "The official documentation"
    The [Plotly Express documentation](https://plotly.com/python/plotly-express/) has examples of every chart type.
