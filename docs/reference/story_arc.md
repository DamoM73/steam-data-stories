# The Data Story Arc

!!! learn "On this page we will learn"
    - the stages of the data story arc
    - what each stage does in our notebook
    - questions to check each stage

Every data story in this course follows the same five stages. We met them in [Lesson 1](../hook/01_data_story.md#the-data-story-arc), and each section of the course matches one stage.

| Stage | What it does | Lessons | Audience sees it? |
| :-- | :-- | :-- | :-- |
| **Hook** | grabs attention with a question worth answering | [1–4](../hook/01_data_story.md) | yes |
| **Behind the Scenes** | collects and checks the data so it can be trusted | [5–8](../cleaning/05_select_filter.md) | a short summary |
| **Rising Insights** | builds up the evidence, one finding at a time | [9–14](../insights/09_new_columns.md) | yes |
| **Aha Moment** | the key insight, shown so clearly no one can miss it | [15](../aha/15_aha_moment.md) | yes |
| **Resolution** | what it means, how sure we are, and what's next | [16](../resolution/16_publishing.md) | yes |

## Hook

The Hook gives our audience a reason to keep reading.

- **In our notebook:** a heading with our question, and a short paragraph explaining why it matters.
- **In our example:** "Was ARC Raiders' drop in players unusual?"

Check the Hook:

- Is the question **specific**, **measurable** and **open**? See [Lesson 3](../hook/03_asking_questions.md#investigable-questions).
- Have we defined every fuzzy word in the question?
- Would someone who doesn't play games still want to know the answer?

## Behind the Scenes

Behind the Scenes is where we earn our audience's trust. Most of the work happens here, but our audience only sees a short summary.

- **In our notebook:** all of ***clean_steam.py***, plus the cleaning of the player history in [Lesson 14](../insights/14_combining.md#cleaning-the-history). In the finished story: one Markdown cell summarising what we did, and the attribution.
- **In our example:** we removed contact details, chose 13 columns, fixed dates and owner numbers, turned fake 0s into nulls, removed a nameless game and a future release date, turned labels into lists, and removed duplicate hours.

Check Behind the Scenes:

- Did we remove personal information we don't need?
- Is every column the right data type?
- Have we written down every cleaning decision, and why?
- Did our checks pass?

## Rising Insights

Rising Insights builds the evidence, one step at a time. Each insight is a finding backed by a number or a chart.

- **In our notebook:** summaries, charts and combined data, each with a Markdown cell explaining it.
- **In our example:** we compared genres and prices, saw the boom in Steam releases, fetched player history from an API, and turned it into monthly percentages of peak.

Check each Rising Insight:

- Does the chart suit the question? See [Choosing a chart](../insights/11_charts_compare.md#choosing-a-chart).
- Does it have a headline title that states the finding?
- Have we said whether we used the mean or the median, and why?
- Have we avoided saying "causes" when we only found a relationship?

## Aha Moment

The Aha Moment is the one chart the whole story builds up to.

- **In our notebook:** the Aha chart, with clutter removed, colour pointing at the finding, clear labels and an annotation. Interactive controls can come after it.
- **In our example:** ARC Raiders in red against five grey games, titled "ARC Raiders kept its players for three months, then lost most of them".

Check the Aha Moment:

- Can someone get the message in five seconds?
- Does the colour point at the finding, and work for people with colour blindness?
- Does the chart answer the question from the Hook?

## Resolution

The Resolution answers three questions: what did we find, how sure are we, and so what?

- **In our notebook:** Markdown cells with our answer, our limitations and what should happen next, using f-strings for any numbers.
- **In our example:** ARC Raiders' drop wasn't unusual, PvE on its own didn't decide which games kept their players, and updates are worth investigating next.

Check the Resolution:

- Does it answer the question in plain words?
- Does it list our limitations honestly?
- Does it say what someone should do or investigate next?
