# 1. What is a Data Story?

!!! learn "In this lesson we will learn"
    - what makes a data story different from a chart
    - the five stages of the data story arc
    - where the Steam dataset comes from and what one row represents
    - how to brainstorm story angles

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

**Steam** is the biggest online store for PC games. Our main dataset holds information about almost every game on Steam: about 138,000 of them.

It comes from the **Steam Games Dataset** by Fronkon Games, who collected it from the Steam store and from a site called SteamSpy. It's published under the **MIT licence**, which lets anyone use and share it as long as they say where it came from. Our classroom copy has had games with adult content removed.

### What one row represents

The data is a table. Each **row** is one game, and each **column** is one fact about that game. For example, here are a few of the columns for one row:

| Column | Value |
| :-- | :-- |
| AppID | 1808500 |
| Name | ARC Raiders |
| Release date | Oct 30, 2025 |
| Price | 31.99 |
| Genres | Action |

The **AppID** is the number Steam uses to identify each game. Two games can share a name, but they never share an AppID.

There are 40 columns in total. They fall into a few groups:

- **about the game:** name, release date, developers, publishers, genres, tags, supported languages
- **price:** price and discount (prices are in US dollars, and on-sale games show their sale price)
- **players:** estimated owners, peak players, average and median playtime
- **reviews:** positive and negative reviews, recommendations, Metacritic score
- **links:** website, support email, screenshots

We'll also use a second set of data: **player history**, which records how many people were playing a game every hour since it came out. We have this for the six games in our example story.

!!! warning "Real data is messy"
    Our data is real, and it hasn't been cleaned. Some numbers are missing, some are impossible, and some columns store numbers as text. We'll find and fix these problems in the Behind the Scenes lessons, so for now, don't trust every number we see.

## Brainstorming story angles

A **story angle** is the part of a topic we choose to focus on. The same dataset can tell lots of different stories, depending on the angle. Here are some angles the Steam data could support:

- **change over time:** how have Steam games changed since 2010?
- **comparison:** are some kinds of games more popular than others?
- **money:** what does a game's price tell us about it?
- **surprise:** what's true in the data that most people would guess wrong?
- **a single game:** what happened to one game, and was it normal?

Our example story uses the last angle. ARC Raiders launched in October 2025, and hundreds of thousands of people played it at once. A few months later most of them had stopped. So our hook is:

> **Was ARC Raiders' drop in players unusual?**

We'll compare ARC Raiders with other games like it, and find out whether games that let us play without fighting other players keep their players for longer.

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

<!-- SCREENSHOT: assets/l01_my_data_story.png — VS Code with my_data_story.md open in the steam_data_stories folder, editor and preview side by side -->

!!! tip "Markdown files"
    A file ending in ***.md*** is a **Markdown** file: plain text with a few symbols for formatting. A line starting with `#` is a heading, `##` is a smaller heading, and a line starting with `-` is a dot point. To see the formatted version, press ++ctrl+shift+v++ (++cmd+shift+v++ on a Mac) in VS Code. Our tutorial pages are written in Markdown too.

### Brainstorm our angles

Under the **Lesson 1: Story angles** heading in ***my_data_story.md***:

1. Pick two story angles from the list above, and make up a third angle of our own.
2. For each of the three angles, write one question about Steam games that we'd really like to know the answer to.
3. Choose the question that interests us most. Don't worry if it isn't perfect yet: in Lesson 3 we'll check whether the data can answer it, and sharpen it.

Save ***my_data_story.md***. We'll come back to these questions in the next two lessons.
