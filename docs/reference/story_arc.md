# The Data Story Arc

!!! learn "On this page we will learn"
    - the stages of the data story arc
    - what each stage does in our notebook
    - questions to check each stage

Every data story in this course follows the same five stages. We met them in [What is a Data Story?](../hook/01_data_story.md#the-data-story-arc), and each section of the course matches one stage.

| Stage | What it does | Where it starts | Does our audience see it? |
| :-- | :-- | :-- | :-- |
| Hook | grabs attention with a question worth answering | [What is a Data Story?](../hook/01_data_story.md) | yes |
| Behind the Scenes | gets the data ready so it can be trusted | [Choosing Columns and Rows](../cleaning/05_select_filter.md) | a short summary |
| Rising Insights | builds up the evidence, one finding at a time | [Making New Columns](../insights/07_new_columns.md) | yes |
| Aha Moment | the key insight, shown so clearly no one can miss it | [The Aha Moment](../aha/14_aha_moment.md) | yes |
| Resolution | answers the question, and says how sure we are | [Publishing Our Data Story](../resolution/15_publishing.md) | yes |

## Hook

The Hook gives our audience a reason to keep reading.

- **In our notebook:** a `mo.md` cell at the top, with our question as the title and a short paragraph explaining why it matters.
- **In our example:** "Do Indie games review as well as games from big studios, and do they cost less?"

Check the Hook:

1. Is our question **specific**, **measurable** and **open**? See [Asking a Question Data Can Answer](../hook/03_asking_questions.md#investigable-questions).
2. Have we defined every word in the question that could mean different things, like "Indie"? See [Asking a Question Data Can Answer](../hook/03_asking_questions.md#defining-our-terms).
3. Would someone who doesn't play games still want to know the answer?

## Behind the Scenes

Behind the Scenes is where we earn our audience's trust. Most of the work happens here, but our audience only sees a sentence or two about it.

- **In our notebook:** all of ***clean_steam.py***. In our finished story: a sentence in the Hook saying what data we used.
- **In our example:** we removed the support emails, chose 10 columns, turned the release dates from text into dates, turned Metacritic scores of 0 into nulls, checked the repeated names, and saved ***clean_games.parquet***.

Check Behind the Scenes:

1. Did we remove personal information we don't need? See [Data, Privacy and Ethics](../hook/04_privacy_ethics.md#removing-columns-we-dont-need).
2. Is every column the right data type?
3. Have we found values that really mean "missing"? See [Fixing Our Data](../cleaning/06_fixing_data.md#values-that-mean-missing).
4. Have we written down every cleaning decision, and why, in ***my_data_story.md***?

## Rising Insights

Rising Insights builds the evidence, one step at a time. Each insight is a finding backed by a number or a chart.

- **In our notebook:** for each insight, a `mo.md` cell with a heading and the numbers, then its chart.
- **In our example:** the typical Indie game gets more positive reviews and costs less, the whole spread of Indie scores sits higher, and price isn't related to review score.

Check each Rising Insight, using the list from [Our Own Insights](../insights/13_own_insights.md#checking-each-insight):

1. Does every group have enough rows?
2. Did we choose the mean or the median on purpose?
3. Does the chart suit the question? See [Choosing a chart](../insights/10_better_charts.md#choosing-a-chart).
4. Does it have a headline title that states the finding, and is the finding true?
5. Do the axes and legend use words our audience understands?
6. Have we said "is related to", not "causes"?

## Aha Moment

The Aha Moment is the one chart the whole story builds up to.

- **In our notebook:** the Aha chart, with colour pointing at the finding, grey for everything else, a headline title and an annotation. UI elements for exploring can come after it.
- **In our example:** the Indie line in blue against a grey line for other games, titled "Since 2018, Indie games have reviewed better every year".

Check the Aha Moment:

1. Can someone get the message in five seconds?
2. Does the colour point at the finding?
3. Does the chart answer the question from the Hook?

## Resolution

The Resolution answers our question, and tells our audience how sure we can be.

- **In our notebook:** a `mo.md` cell at the bottom with our answer and our limitations, using f-strings for any numbers.
- **In our example:** Indie games get a higher share of positive reviews and cost less; limitations include how we chose our groups and the 500-review rule.

Check the Resolution:

1. Does it answer the question in plain words?
2. Does it list our limitations honestly? See [Publishing Our Data Story](../resolution/15_publishing.md#being-honest-about-limitations).
3. Can our audience follow the whole story in app view, without us explaining it?
