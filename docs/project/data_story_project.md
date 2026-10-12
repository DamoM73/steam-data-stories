# Your Data Story Project

!!! learn "On this page we will learn"
    - how to tell a data story with a dataset we choose ourselves
    - the steps of a data story project, from finding data to presenting
    - where to look back in the tutorials for each step

## Introduction

In the tutorials we learnt to tell a data story by working through one example, and practised each step on our own question about the Steam data. Now it's time to put it all together. In our project, we'll choose our **own** dataset, ask our own question, and tell a data story about it from start to finish.

The steps are the same ones we followed with the Steam data, in the same order as the data story arc. The difference is that nobody has checked our dataset for us. It will have its own problems to find and fix, and its own story to discover. Each step below links back to the tutorial pages where we learnt how to do it, so when we get stuck, we can look back at how we did it with the Steam data.

!!! tip "Our new data, our same skills"
    Every pattern we need is in the tutorials. When we copy a pattern, change the column names, variable names and file names to match our new data. The [Patterns we can reuse](../insights/13_own_insights.md#patterns-we-can-reuse) table and the [Polars](../reference/polars.md), [Plotly Express](../reference/plotly.md) and [marimo](../reference/marimo.md) reference pages are good places to start.

## Step 1: Find our data

**Story stage:** Hook

Our data story starts with a dataset we're curious about. Browse the sources on the [Finding Data](../reference/data_sources.md) page, starting close to home, until a dataset makes us want to know more.

1. Check the dataset against the list in [Choosing a dataset](../reference/data_sources.md#choosing-a-dataset). If it fails any check, choose a different dataset.
2. Make a new folder for our project, with a ***data*** folder inside it, and save the CSV file in the ***data*** folder.
3. Create a new ***my_data_story.md*** in the project folder. This is our record for the whole project, just like the one we kept for the Steam data.
4. Under a `## Our data source` heading, record where our data came from, as described in [Recording our source](../reference/data_sources.md#recording-our-source).

!!! warning "Choose data about things, not people"
    Choose data about things, places and events, such as sport results, games, weather, transport or animals. Private data about individual people can hurt or identify them, even when it's published openly. See [Data, Privacy and Ethics](../hook/04_privacy_ethics.md).

## Step 2: Explore our data

**Story stage:** Hook

Before we ask a question, we need to know what's in our data. Make a new cleaning notebook in our project folder, just like ***clean_steam.py***, and name it after our data, for example ***clean_dams.py***.

1. Load the CSV file and look at its shape, its schema and the table viewer. See [Exploring Our Data](../hook/02_exploring_data.md).
2. Work out what one row represents, just like we did in [What one row represents](../hook/01_data_story.md#what-one-row-represents).
3. Find out what every column means. Look for the data dictionary on the page we downloaded the data from.
4. Under a `## Exploring the data` heading in ***my_data_story.md***, record what one row represents, what each column means, and anything that looks strange.

## Step 3: Ask a question

**Story stage:** Hook

Now we can choose the question our story will answer.

1. Brainstorm three questions, using the story angles in [Brainstorming story angles](../hook/01_data_story.md#brainstorming-story-angles).
2. Check each one against the data with summary statistics and counts, then choose the best. See [Asking a Question Data Can Answer](../hook/03_asking_questions.md).
3. Make sure our question is specific, measurable and open, and define every word in it that could mean different things. See [Investigable questions](../hook/03_asking_questions.md#investigable-questions) and [Defining our terms](../hook/03_asking_questions.md#defining-our-terms).
4. Under a `## Our question` heading, record our question, our definitions, and why we chose it.

## Step 4: Check privacy and ethics

**Story stage:** Behind the Scenes

1. Look for columns with personal information, and remove any we don't need. See [Removing columns we don't need](../hook/04_privacy_ethics.md#removing-columns-we-dont-need).
2. Check the licence and work out the attribution it asks for. See [Licences and attribution](../hook/04_privacy_ethics.md#licences-and-attribution).
3. Under a `## Privacy and ethics` heading, record what we removed, the licence and our attribution.

## Step 5: Clean our data

**Story stage:** Behind the Scenes

Our dataset will have its own problems, and they may not be the same ones the Steam data had. So let's look for each kind of problem we've met:

1. Keep only the columns and rows our question needs. See [Choosing Columns and Rows](../cleaning/05_select_filter.md).
2. Check the data type of every column. Are dates stored as text? Are numbers stored as text? See [Text into dates](../cleaning/06_fixing_data.md#text-into-dates). Our dates may be written differently from the Steam dates, so work out their format code.
3. Look for values that mean "missing", like 0, -1 or blank text, and decide whether each one is real. See [Values that mean "missing"](../cleaning/06_fixing_data.md#values-that-mean-missing).
4. Look for repeated rows, and work out whether they're mistakes or real. See [Repeated names](../cleaning/06_fixing_data.md#repeated-names).
5. Save our clean data as a Parquet file. See [Saving our clean data](../cleaning/06_fixing_data.md#saving-our-clean-data).
6. Under a `## Clean data` heading, record every cleaning decision we made and why, starting each one with "We decided…".

!!! tip "When we get an error"
    Errors are a normal part of working with new data. Read the error message in parts, then check the [Common Errors](../reference/common_errors.md) page. Most of the errors we'll meet are there, with how to fix them.

## Step 6: Find our insights

**Story stage:** Rising Insights

Make a new story notebook for our project, just like ***steam_story.py***, for example ***dams_story.py***, and load our clean Parquet file. See [A new notebook](../insights/07_new_columns.md#a-new-notebook).

1. Plan three to five insights that build towards answering our question, just like in [Planning our insights](../insights/13_own_insights.md#planning-our-insights).
2. Build each one using the patterns we've learnt:
    - new columns and group labels: [Making New Columns](../insights/07_new_columns.md)
    - summaries of each group, using the right average: [Summarising Groups](../insights/08_summarising_groups.md)
    - the right chart for each question: [Choosing a chart](../insights/10_better_charts.md#choosing-a-chart)
    - trends and relationships: [Trends and Relationships](../insights/11_trends_relationships.md)
    - outliers, checked before we decide what to do with them: [Outliers and Predictions](../insights/12_outliers_predictions.md)
3. Check every insight against the list in [Checking each insight](../insights/13_own_insights.md#checking-each-insight).
4. Under a `## Our insights` heading, record each finding in one sentence, with a number, and any new limitations we find.

## Step 7: Design our Aha Moment

**Story stage:** Aha Moment

1. Choose the one insight that best answers our question.
2. Redesign its chart so the finding is impossible to miss: one colour for the part that matters, grey for the rest, a headline title and an annotation. See [Making one line stand out](../aha/14_aha_moment.md#making-one-line-stand-out).
3. Add at least one UI element that lets our audience explore our data, shown in the same cell as the chart it changes. See [Letting our audience explore](../aha/14_aha_moment.md#letting-our-audience-explore).
4. Under a `## Aha Moment` heading, record our Aha chart's title, and what someone else said it showed after looking at it for five seconds.

## Step 8: Publish our story

**Story stage:** Resolution

1. Write the words of our story with `mo.md`: a Hook, a heading and a sentence for each insight, and a Resolution that answers our question. Use f-strings for our numbers. See [Publishing Our Data Story](../resolution/15_publishing.md).
2. Be honest about our limitations, and include our attribution. See [Being honest about limitations](../resolution/15_publishing.md#being-honest-about-limitations).
3. Tidy our notebook for our audience and check it in app view. See [Tidying for our audience](../resolution/15_publishing.md#tidying-for-our-audience) and [Checking the app view](../resolution/15_publishing.md#checking-the-app-view).
4. Load our data with `mo.notebook_dir()` and hand in our story. See [Getting ready for the class server](../resolution/15_publishing.md#getting-ready-for-the-class-server).

## Step 9: Present our story

**Story stage:** Resolution

1. Plan and rehearse a three-minute talk that follows the data story arc. See [Planning our talk](../resolution/16_presenting.md#planning-our-talk) and [Rehearsing](../resolution/16_presenting.md#rehearsing).
2. Present our story, and give feedback on our classmates' stories with the arc checklist and two stars and a wish. See [Giving feedback](../resolution/16_presenting.md#giving-feedback).
3. Make our final edits, then hand in our final version. See [Making our final edits](../resolution/16_presenting.md#making-our-final-edits).

!!! tip "Check every stage"
    The [Data Story Arc](../reference/story_arc.md) page has questions to check each stage of our story. Use them as we finish each step, not just at the end.
