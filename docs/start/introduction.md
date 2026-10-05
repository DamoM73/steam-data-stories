# Introduction

!!! learn "On this page we will learn"
    - what a data story is and why we tell them
    - what data we're going to explore
    - which tools we'll use
    - what we need to know before we start

In this course we're going to learn how to turn a big pile of real-world data into a story that people understand. We'll load the data, clean it, explore it, find the interesting parts and then present what we found as a **data story**.

## What is a data story?

A **data story** uses data, charts and words together to explain something and convince people it's true. A chart on its own shows numbers. A data story tells us why those numbers matter.

Data stories follow the same shape as any good story. There's a hook that makes us want to know more, a build-up of evidence, a moment where it all clicks, and an ending that tells us what it means. We'll use these stages to organise the whole course:

| Stage | What happens | Lessons |
| :-- | :-- | :-- |
| **Hook** | we meet our data and ask a question worth answering | 1–4 |
| **Behind the Scenes** | we clean the data so we can trust it | 5–8 |
| **Rising Insights** | we explore, summarise and chart the data, and bring in more data | 9–14 |
| **Aha Moment** | we find the key insight and make it stand out | 15 |
| **Resolution** | we publish our finished data story | 16 |

## The data

We're going to explore **Steam**, the biggest online store for PC games. We'll use two sets of real data:

- the **Steam games dataset**, with details of about 138,000 games: names, release dates, prices, genres, playtime and more
- **player history**, with the number of people playing a game every hour since it was released

Real data is messy. Dates are stored as text, numbers are missing, some values are impossible and some rows appear twice. Part of telling a data story is fixing these problems before anyone else sees our charts, and that's what the Behind the Scenes lessons are for.

The data file is too big to open in a spreadsheet program like Excel. That's one of the reasons we use code.

## Our example story

Each lesson works through one example question:

> **Was ARC Raiders' drop in players unusual?**

ARC Raiders is an extraction shooter that launched in October 2025. Hundreds of thousands of people played it in its first few months, and then most of them stopped. Was that normal for this kind of game? Do games that let us play without fighting other players keep their players for longer? We'll find out together.

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
