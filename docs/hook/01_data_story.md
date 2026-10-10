# 1. What is a Data Story?

!!! learn "In this lesson we will learn"
    - what makes a data story different from a chart
    - the five stages of the data story arc
    - where the Steam dataset comes from and what one row represents
    - how to brainstorm story angles

!!! terms "Terminology"
    - **data story arc** – the five stages of a data story: Hook, Behind the Scenes, Rising Insights, Aha Moment and Resolution.
    - **AppID** – the number Steam uses to identify each game; no two games share an AppID.
    - **MIT licence** – a licence that lets anyone use, copy, change and share a work, as long as they include the original copyright notice.
    - **Indie** – a game made by a small, independent team, often without a big publisher paying for it.
    - **story angle** – the part of a topic we choose to focus on when we tell a data story.
    - **Markdown** – plain text with a few symbols for formatting, such as # for a heading and - for a dot point.

## Introduction

Every day we see charts in the news, in games and in apps. Most of them show us numbers and leave us to work out what they mean. A **data story** does that work for us: it uses data, charts and words together to explain something and convince us it's true.

In this course we're going to tell our own data stories about Steam games. Before we write any code, let's look at one of the most famous data stories ever told, and work out what makes it work.

## A famous data story

In 1854 Britain was fighting the Crimean War. Florence Nightingale, a nurse, was sent to run the British Army hospital at Scutari, in what is now Istanbul. What she found shocked her: soldiers were dying in huge numbers, and most of them weren't dying from their wounds.

Nightingale kept careful records. During her first winter at Scutari, 4,077 British soldiers died there, and about ten times more soldiers died from diseases like typhus, cholera and dysentery than from battle wounds. Those diseases spread because of dirty water, blocked sewers and crowded wards, so most of the deaths could have been prevented. In March 1855 a Sanitary Commission arrived, flushed out the sewers and improved the ventilation, and the death rate fell sharply.

Back in England, Nightingale wanted the army to change for good. Working with the statistician William Farr, she turned her records into charts. The most famous is her **Diagram of the causes of mortality in the army in the East** (1858), now often called the **Nightingale rose**:

![Florence Nightingale's Diagram of the causes of mortality in the army in the East, two rose-shaped charts made of coloured wedges, one wedge for each month from April 1854 to March 1856](../assets/nightingale_rose.jpg)

*Diagram of the causes of mortality in the army in the East, Florence Nightingale, 1858. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Nightingale-mortality.jpg).*

Each wedge is one month. The blue part of each wedge shows deaths from preventable diseases, and the red part shows deaths from wounds. The blue is so much bigger that nobody looking at the chart could miss the point. Her charts were shown to Parliament and the Queen, and they helped bring in reforms that made army hospitals and barracks cleaner and safer.

!!! tip "Why a story and not just a table?"
    Nightingale's numbers were available before she drew her charts, but few people paid attention to tables of figures. Her story picked one clear message, showed the evidence in a way anyone could understand, and ended with what needed to change. That's what turns data into a data story.

## The data story arc

Nightingale's story has the same shape as a good novel or film. We'll call this shape the **data story arc**:

| Stage | What it does | In Nightingale's story |
| :-- | :-- | :-- |
| **Hook** | grabs attention with a question worth answering | why are so many soldiers dying in hospital? |
| **Behind the Scenes** | collects and checks the data so it can be trusted | her careful records of every death and its cause |
| **Rising Insights** | builds up the evidence, one finding at a time | deaths rise in winter; most are from disease |
| **Aha Moment** | the key insight, shown so clearly no one can miss it | the rose: the blue dwarfs the red |
| **Resolution** | what it means and what should happen next | clean the hospitals, and the deaths will fall |

Our course follows the same arc. The lessons in each section of this site match one stage, so by the end we'll have worked through every stage of our own data story.

!!! tip "Behind the Scenes matters"
    Audiences rarely see the Behind the Scenes stage, but it's where most of the work happens. If the data is wrong, the whole story is wrong, no matter how good the charts look.

## Meet the Steam dataset

**Steam** is the biggest online store for PC games. Our dataset holds information about the most-reviewed games on Steam: the 10,250 games that players have reviewed at least 500 times.

It comes from the **Steam Games Dataset** by Fronkon Games, who collected it from the Steam store and from a site called SteamSpy. It's published under the **MIT licence**, which lets anyone use and share it as long as they say where it came from. Our classroom copy keeps only games with at least 500 reviews, and has had games with adult content removed.

### What one row represents

The data is a table. Each **row** is one game, and each **column** is one fact about that game. There are 13 columns. Here's the whole row for Hollow Knight, made by Team Cherry, a small studio in Adelaide:

| Column | Hollow Knight | What it means |
| :-- | :-- | :-- |
| AppID | 367520 | the number Steam uses to identify the game |
| Name | Hollow Knight | the game's name |
| Release date | Feb 24, 2017 | the day the game came out on Steam |
| Price | 7.49 | the price in US dollars when the data was collected (games on sale show their sale price) |
| Positive | 403641 | how many players reviewed the game positively |
| Negative | 12305 | how many players reviewed the game negatively |
| Recommendations | 455843 | the number of player recommendations Steam lists for the game |
| Metacritic score | 87 | the score from professional critics on Metacritic, out of 100 |
| Achievements | 63 | how many achievements players can unlock in the game |
| Developers | Team Cherry | who made the game |
| Publishers | Team Cherry | who released and sold the game (often a bigger company than the developer) |
| Genres | Action,Adventure,Indie | the kinds of game it is, separated by commas |
| Support email | info@teamcherry.com.au | the email address players can use to get help |

The **AppID** is the number Steam uses to identify each game. Two games can share a name, but they never share an AppID.

!!! tip "What our data can't tell us"
    Our data doesn't include how many people play each game, how long they play for, how many copies were sold, or how much money a game made. It also has no age ratings or player ages. A question that needs any of these can't be answered with our data, so we'll choose questions that use the 13 columns above.

!!! warning "Real data is messy"
    Our data is real, and it hasn't been cleaned. Some numbers really mean "missing", some columns store dates as text, and some games appear more than once. We'll find and fix these problems in the Behind the Scenes lessons, so for now, don't trust every number we see.

## Brainstorming story angles

A **story angle** is the part of a topic we choose to focus on. The same dataset can tell lots of different stories, depending on the angle. Here are some angles the Steam data could support:

- **change over time:** how have Steam games changed since 2010?
- **comparison:** are some kinds of games more popular than others?
- **money:** what does a game's price tell us about it?
- **surprise:** what's true in the data that most people would guess wrong?
- **a single game:** what happened to one game, and was it normal?

Our example story uses the comparison angle. Hollow Knight, Stardew Valley and Terraria are all **Indie** games: games made by small, independent teams, often without a big publisher paying for them. Big studios spend millions of dollars on their games, so we might expect their games to be better. But are they? So our hook is:

> **Do Indie games review as well as games from big studios?**

We'll compare Indie games with all the other games in our data, and find out whether they also cost less.

## Our data story

Now it's our turn to start our own data story about Steam games. We'll record our ideas and decisions in a file called ***my_data_story.md***, and add to it at the end of every lesson.

### Create our data story file

1. Open our ***steam_data_stories*** folder in VS Code.
2. Choose **File** → **New File…**, type `my_data_story.md` and press ++enter++. When VS Code asks where to save it, choose our ***steam_data_stories*** folder.
3. Add the text below and save the file.

```text title="my_data_story.md"
# My Data Story

## Lesson 1: Story angles
```

!!! tip "Markdown files"
    A file ending in ***.md*** is a **Markdown** file: plain text with a few symbols for formatting. A line starting with `#` is a heading, `##` is a smaller heading, and a line starting with `-` is a dot point. To see the formatted version, press ++ctrl+shift+v++ (++cmd+shift+v++ on a Mac) in VS Code. Our tutorial pages are written in Markdown too.

### Brainstorm our angles

Under the **Lesson 1: Story angles** heading in ***my_data_story.md***:

1. Pick two story angles from the list above, and make up a third angle of our own.
2. For each of the three angles, write one question about Steam games that we'd really like to know the answer to. Under each question, list the columns from the table above that we'd need to answer it.
3. Choose the question that interests us most. Don't worry if it isn't perfect yet: in Lesson 3 we'll check whether the data can answer it, and sharpen it.

Save ***my_data_story.md***. We'll come back to these questions in the next two lessons.
