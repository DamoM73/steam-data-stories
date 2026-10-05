# 13. Getting Player History from an API

!!! learn "In this lesson we will learn"
    - what an API is and why data stories use them
    - how to request data from a web API with Requests
    - what HTTP status codes tell us
    - how to read JSON data into a DataFrame
    - how to get more than one page of results with a cursor
    - how to load several saved JSON files at once

## Introduction

Back in Lesson 3, we found a big gap in our data. `Peak CCU` and `Estimated owners` can't tell us how many people play recent games, and they only give one number for each game. Our question is about how the number of players **changed** over time. We need a second source of data.

That data comes from an **API**.

## What is an API?

An **API**, short for **application programming interface**, is a way for one program to ask another program for data. A **web API** works over the internet: our code sends a **request** to a web address, and the server sends back a **response** holding the data.

We use the web every day in the same way. When we open a web page, our browser sends a request and the server sends back a page for people to read. A web API sends back data for programs to read instead.

Our player history comes from the [Games Popularity](https://games-popularity.com/) API. It has recorded how many people were playing each Steam game, every hour, since the game came out.

## Importing the libraries

We need three more libraries in this lesson:

- **Requests**, to send requests to the API
- **json**, which is built into Python, to read saved JSON files
- **time**, also built into Python, to pause between requests

Start marimo with `marimo edit steam_story.py` and press ++ctrl+shift+r++ (++cmd+shift+r++ on a Mac) to run our earlier cells. Change the first cell to match the code below and run it.

```python linenums="1" title="steam_story.py" hl_lines="1 2 6"
--8<-- "examples/insights/13_api/story01.py"
```

??? note "Code explanation"
    - **line 1** → imports Python's `json` library, for reading JSON files.
    - **line 2** → imports Python's `time` library, so we can pause our code.
    - **line 6** → imports the Requests library, for sending requests over the internet.

The blank line separates libraries that come with Python from libraries we installed. It's a common way to arrange imports.

## Sending a request

!!! warning "Go easy on the API"
    Without an account, the Games Popularity API allows **100 requests a day** from each internet address. Everyone at school usually shares one internet address, so the whole class shares those 100 requests. Run the request cells in this lesson **once**, and don't keep re-running them. If the API stops answering, the saved files in the last section still work.

Add a new cell at the bottom, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/13_api/story14.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → stores the web address for ARC Raiders' player history in `API_URL`. The number at the end is ARC Raiders' AppID.
    - **line 2** → sends a request to that address, using `requests.get`, and stores the server's response in `response`. `timeout=30` means give up if there's no answer within 30 seconds.
    - **line 3** → shows the response's **status code**.

The output is **200**. Every response comes with a **status code**, a number that says how the request went:

| Status code | Meaning |
| :-- | :-- |
| **200** | OK: here's the data |
| **404** | not found: check the web address |
| **429** | too many requests: we've used up our limit, so wait and try again later |
| **500** | the server had a problem |

!!! tip "Requests and marimo"
    marimo re-runs a cell whenever a variable it uses changes. If we edit `API_URL`, the request cell and every cell after it runs again, and each run uses up a request. That's another reason to keep API cells short and leave them alone once they work.

## Reading JSON

The data comes back as **JSON**, short for **JavaScript Object Notation**. JSON is the most common format for sending data over the web. It looks a lot like Python dictionaries and lists:

```json title="part of the response"
{
  "steamId": "1808500",
  "history": [
    {"players": 16317, "added": "2026-10-05T09:00:11.406"},
    {"players": 15894, "added": "2026-10-05T08:00:05.034"}
  ],
  "nextCursor": "MjAyNi0wOS0yMw=="
}
```

Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/13_api/story15.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → turns the JSON in the response into a Python dictionary, using the response's `json` method, and stores it in `page`.
    - **line 2** → makes a DataFrame from the list stored under the `history` key. Each dictionary in the list becomes a row, and each key becomes a column.
    - **line 3** → shows the `nextCursor` value and the number of rows in `first_page`.

The output shows a short piece of text, the **cursor**, and **1000**. Our numbers might be different, because the API is always adding new hours. The first page holds the 1,000 most recent hours: about six weeks of data.

## Getting the next page

ARC Raiders has been out for almost a year, which is more than 8,000 hours. An API that sends lots of data usually splits it into **pages**. The **cursor** is a bookmark: we send it back with our next request, and the API sends the next page. Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/13_api/story16.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → pauses for 2 seconds before the next request, so we don't send requests too quickly.
    - **lines 2–6** → send a second request to the same address, with the cursor from the first page as a **parameter**, and store the response in `next_response`. Requests adds the parameter to the end of the web address for us, like `?cursor=MjAyNi0wOS0yMw==`.
    - **line 7** → turns the second page's `history` into a DataFrame called `second_page`.
    - **line 8** → joins the two pages together, one under the other, using `pl.concat`, and shows the result.

<!-- SCREENSHOT: assets/l13_two_pages.png — the concatenated first_page and second_page, 2,000 rows -->

We now have **2000** rows: about twelve weeks of hourly player counts.

!!! tip "Be a polite API user"
    Pausing between requests is good manners. A server shared by thousands of people can slow down, or block us, if one program sends requests as fast as it can. Many APIs have rules about how often we can ask, so always read the API's documentation first.

## Loading the saved history

Getting the full history of all six games would take about 60 requests, and the whole class would quickly run out. So we've already collected the history once, and saved each game's JSON in our ***data/player_history*** folder. Each file is named after the game's AppID, like ***1808500.json***.

Add a new cell, type the code below and run it.

```python linenums="1" title="steam_story.py"
--8<-- "examples/insights/13_api/story17.py"
```

!!! primm "PRIMM"
    1. **Predict** what you think will happen when we run the cell. Be specific.
    2. **Run** the cell.
    3. Time to **investigate** the code. What does each line do?

??? note "Code explanation"
    - **line 1** → creates an empty list called `history_frames`, to hold one DataFrame for each game.
    - **line 2** → loops through every AppID in `story_games`.
    - **line 3** → opens the saved file for that AppID. `with` makes sure the file is closed again when we're finished with it.
    - **line 4** → reads the JSON in the file into a Python dictionary called `saved`.
    - **lines 5–9** → make a DataFrame from that game's `history`, add a column called `AppID` holding the game's `steamId`, and add the DataFrame to the end of `history_frames`. `pl.lit` puts the same value in every row.
    - **line 10** → joins all six DataFrames together, one under the other, and stores the result in `history`.
    - **line 11** → shows `history` as the cell's output.

<!-- SCREENSHOT: assets/l13_history.png — the history DataFrame with players, added and AppID columns -->

`history` has **59828** rows: every hour of every one of our six games. Look closely at the column types. `added` is a **str**, not a date and time, and `AppID` is a **str** too, because the API stores it as text. Sound familiar? It's time for some more Behind the Scenes work, which we'll do next lesson.

## Our data story

Open ***my_data_story.md***, add a new heading `## Lesson 13: More data` and record our answers under it.

1. Does our question need a second source of data? Write down what extra data would help, and where we might find it.
2. Write the attribution for any new data source, like we did in Lesson 4.
3. If our question is about player numbers over time, choose which of our six games it needs, or look up the AppIDs of other games on the Steam store. Write them down, and ask our teacher about getting their history.
