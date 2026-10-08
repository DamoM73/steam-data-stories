# 4. Data, Privacy and Ethics

!!! learn "In this lesson we will learn"
    - what personal information is
    - what the Australian Privacy Principles say about using it
    - how to find personal information in a dataset
    - how to remove columns we shouldn't share
    - why licences and attribution matter

!!! terms "Terminology"
    - **personal information** – any information or opinion that could identify a person, such as a name, email address or photo.
    - **Privacy Act 1988** – the Australian law that sets the rules for how organisations and government agencies handle personal information.
    - **Australian Privacy Principles** – the 13 rules in the Privacy Act about collecting, using, sharing and protecting personal information.
    - **null** – Polars' way of saying a value is missing.
    - **depersonalising** – removing or replacing the personal details in data, while keeping the part we need.
    - **licence** – a set of rules from a work's owner that says how other people can use it.
    - **attribution** – saying where our data came from, so readers can check our work.

## Introduction

Our data story will end up on screens in front of other people. Before we share anything built from data, we need to check two things: that we aren't sharing information about people that we shouldn't, and that we're allowed to use the data at all. Let's look at both.

## Personal information

**Personal information** is any information, or opinion, that could identify a person. Obvious examples are a name, a phone number, a home address and a photo. Less obvious examples include an IP address and the location data from a phone.

Personal information doesn't have to name someone to identify them. An email address like `j.citizen.games@gmail.com` might not include a full name, but it belongs to one person and can be used to contact them.

### The Australian Privacy Principles

In Australia, the **Privacy Act 1988** sets the rules for how organisations and government agencies handle personal information. At its heart are the 13 **Australian Privacy Principles** (APPs). A few of them matter most when we work with data:

| Principle | What it means for us |
| :-- | :-- |
| **APP 3: Collection** | only collect the personal information we actually need |
| **APP 6: Use or disclosure** | only use or share personal information for the purpose it was collected for |
| **APP 10: Quality** | keep personal information accurate and up to date |
| **APP 11: Security** | protect personal information from misuse and from being seen by people who shouldn't see it |

!!! tip "Does the Privacy Act apply to us?"
    The Privacy Act mainly applies to government agencies and to larger organisations. Our class project isn't covered by it, but the principles are still a good guide to doing the right thing with data about people, and they're the rules we'd have to follow in many jobs that use data.

## Finding personal information in our data

Let's look through our 13 columns for anything that could identify a person. Most columns are about games, not people: names of games, prices, genres and review counts. But one column holds contact details: `Support email`, an email address for getting help with the game.

Many Steam games are made by big companies, with support addresses like `support@company.com`. But lots of games are made by one person working alone, and their support address is often their own personal email.

Start marimo with `marimo edit clean_steam.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Then add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/hook/04_privacy_ethics/cell10.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → counts how many values in the `Support email` column are missing.

The output is **2728**. A missing value is called a **null**. So 2,728 games have no support email, which means 7,522 games do have one.

Now let's find out how many of those addresses are personal email accounts. Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/hook/04_privacy_ethics/cell11.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?
    4. Time to **modify** the code. Change `"@gmail.com"` to another free email service, such as `"@outlook.com"` or `"@qq.com"`, and run it again.

??? note "Code explanation"
    - **line 1** → checks each value in the `Support email` column to see whether it contains the text `@gmail.com`, then adds up how many do.

The output is **1270**. That's 1,270 games whose support address is a free Gmail account. A company usually has its own email address, so many of these are likely to belong to a person.

!!! tip "Missing values are skipped"
    Just like in Lesson 3, `sum` counts each `true` as 1. A missing email can't contain anything, so `str.contains` gives a null for it, and `sum` skips it.

## Removing columns we don't need

These email addresses are already public: anyone can find them on each game's Steam store page. So is it fine to put them in our data story? The APPs give us a useful test: do we **need** them for our purpose?

Our purpose is to tell a story about games and players. No question in our story needs to contact a game's developer, so we don't need `Support email` at all. The safest thing to do with personal information we don't need is to remove it.

Add a new cell, type the code below and run it.

```python linenums="1" title="clean_steam.py"
--8<-- "examples/hook/04_privacy_ethics/cell12.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → makes a copy of `games` without the `Support email` column, and stores it in a new variable called `public_games`.
    - **line 2** → shows the shape of `public_games`.

The output shows **10250** rows and **12** columns: the same games, without the email column. From now on we'll build on `public_games`, so the contact details never end up in our charts or our finished story.

Remember from Lesson 2: in marimo, each variable can only be created in one cell. That's why we didn't write `games = games.drop(...)`. We gave the new version a new name instead, and the original `games` is still there unchanged.

!!! tip "Depersonalising instead of deleting"
    Sometimes we need part of the information without the personal details. For example, if our question were "Do games with a support email get more recommendations?", we could replace each email with just `yes` or `no`. This is called **depersonalising** the data. We'll learn how to make new columns like that in Lesson 7.

## Licences and attribution

Data belongs to someone. Before we use it, we need to know what we're allowed to do with it. A **licence** is a set of rules from the owner that says how others can use their work.

Our Steam games data uses the **MIT licence**. It lets anyone use, copy, change and share the data, as long as they include the original copyright notice and licence. The ***README.txt*** file in our ***data*** folder includes them.

**Attribution** means saying where our data came from. Every good data story includes it, so readers can check our work. For our story, the attribution looks like this:

> Steam games data from the Steam Games Dataset by Fronkon Games (MIT licence), downloaded October 2026.

!!! warning "Game names and images belong to their owners"
    The licence covers the data, not the games. Names like Hollow Knight and images from Steam belong to the companies that made the games, so we can mention them in our story, but we shouldn't copy their logos or artwork.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 4: Privacy and ethics` and record our answers under it.

1. List the columns our own question needs. Does any of them hold personal information? If so, can we answer our question without it?
2. Write the attribution for our data story, using the example above.
3. Think about the people our story is about. Could anything in our finished story be unfair to a person or a small developer? Write down one way we could avoid that.
