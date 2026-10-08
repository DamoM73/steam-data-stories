# Introduction

!!! learn "On this page we will learn"
    - what a data story is and why we tell them
    - what data we're going to explore
    - which tools we'll use
    - what we need to know before we start

!!! terms "Terminology"
    - **data story** – a way of using data, charts and words together to explain something and convince people it's true.
    - **hook** – the first stage of a data story, which grabs attention with a question worth answering.
    - **behind the scenes** – the stage of a data story where we collect and clean the data so it can be trusted.
    - **rising insights** – the stage of a data story that builds up the evidence, one finding at a time.
    - **aha moment** – the stage of a data story that shows the key insight so clearly no one can miss it.
    - **resolution** – the final stage of a data story, which explains what the finding means and what should happen next.
    - **Polars** – a Python library for loading, cleaning and analysing tables of data.
    - **Plotly Express** – a Python library for making interactive charts.
    - **marimo** – a notebook program where we write Python code in cells and see the results straight away.

In this course we're going to learn how to turn a big pile of real-world data into a story that people understand. We'll load the data, clean it, explore it, find the interesting parts and then present what we found as a **data story**.

## What is a data story?

A **data story** uses data, charts and words together to explain something and convince people it's true. A chart on its own shows numbers. A data story tells us why those numbers matter.

Data stories follow the same shape as any good story. There's a hook that makes us want to know more, a build-up of evidence, a moment where it all clicks, and an ending that tells us what it means. We'll use these stages to organise the whole course:

| Stage | What happens | Lessons |
| :-- | :-- | :-- |
| **Hook** | we meet our data and ask a question worth answering | 1–4 |
| **Behind the Scenes** | we clean the data so we can trust it | 5–6 |
| **Rising Insights** | we explore, summarise and chart the data, then work on our own question | 7–13 |
| **Aha Moment** | we find the key insight and make it stand out | 14 |
| **Resolution** | we publish and present our finished data story | 15–16 |

## The data

We're going to explore **Steam**, the biggest online store for PC games. We'll use the **Steam games dataset**: details of the 10,250 games on Steam with at least 500 player reviews, including their names, release dates, prices, genres and reviews.

Real data is messy. In our data, dates are stored as text, some numbers really mean "missing" and some games appear more than once. Part of telling a data story is fixing these problems before anyone else sees our charts, and that's what the Behind the Scenes lessons are for.

## Our example story

Each lesson works through one example question:

> **Do Indie games review as well as games from big studios?**

Indie games, like Hollow Knight and Stardew Valley, are made by small, independent teams. Big studios spend far more money on their games, so we might expect players to like them more. Do they? And do Indie games cost less? We'll find out together.

At the end of each lesson there's an **Our data story** task. That's where we use what we've just learnt to work on our own question about the same Steam data, so by the end of the course we'll each have our own data story.

## The tools

| Tool | What it does |
| :-- | :-- |
| **Python** | the programming language we write all our code in |
| **Polars** | a Python library for loading, cleaning and analysing tables of data |
| **Plotly Express** | a Python library for making interactive charts |
| **marimo** | a notebook where we write code in small blocks called cells and see the results straight away |
| **VS Code** | the editor we use to manage our files and run commands |

That's a lot of new tools, but we don't need to learn them all at once. We'll learn each one when our story needs it, and the **Reference** section has a summary of each tool we can come back to.

## Required knowledge

We'll need solid Python skills before we start. We don't need to know anything about data science; we'll learn that as we go.

| Skills | Course |
| :-- | :-- |
| Basic syntax and structure<br>Control flow<br>Functions<br>Data structures | [A Turtle Introduction to Python](https://damom73.github.io/turtle-introduction-to-python/) |
| Object-oriented programming | [Deepest Dungeon - Python OOP](https://damom73.github.io/python-oop-with-deepest-dungeon/) |

Now that we know where we're heading, the next page sets up our computer for the course.
