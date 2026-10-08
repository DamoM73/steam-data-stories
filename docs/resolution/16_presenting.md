# 16. Presenting and Feedback

!!! learn "In this lesson we will learn"
    - how to plan a three-minute talk that follows the data story arc
    - how to present our story from the app view
    - how to give useful feedback with the arc checklist and two stars and a wish
    - how to use feedback to make our final edits

!!! terms "Terminology"
    - **peer review** – checking a classmate's work against agreed criteria and giving them feedback to improve it.

## Introduction

Our story is written and published. Now it's time to tell it. In this lesson we'll present our data story to the class in **three minutes**, give feedback on each other's stories, and use the feedback to make our story as good as it can be.

A data story told out loud is different from one that's read. Our audience can't scroll back up or read at their own pace, so we lead them through it: one idea at a time, with each chart on screen while we talk about it.

## Planning our talk

Three minutes isn't long, so we plan how to use it. Our talk follows the same arc as our story:

| Stage | Time | What we do |
| :-- | :-- | :-- |
| Hook | 30 seconds | ask our question and say why it's interesting |
| Behind the Scenes | 15 seconds | say what data we used, and one thing we had to clean |
| Rising Insights | 60 seconds | show two or three insights, one chart at a time |
| Aha Moment | 45 seconds | show our Aha chart and point to the finding, then use a control to show it holds |
| Resolution | 30 seconds | answer our question, and give our most important limitation |

For our example story, the Aha Moment might sound like this:

```text title="Aha Moment (45 seconds)"
This is the chart that answers our question. The blue line is Indie
games and the grey line is everything else. Look at 2018: from then on,
the blue line stays above the grey line every single year, about 4 to 8
points ahead. And if I drag the slider to start at 2018, the gap is
still there in every year.
```

Open ***my_data_story.md***, add a new heading `## Lesson 16: Presenting`, and write a short plan for each stage, using the table above. Write **dot points**, not a script: one or two points per stage, with the numbers we'll mention.

!!! tip "One number per chart"
    Our audience will only remember a few numbers. For each chart, choose the **one** number that matters most, say it clearly, and point to it on the screen.

## Rehearsing

Open our story in app view, using our address on the class server or `marimo run steam_story.py` on our own computer. Then practise our talk out loud, with a timer.

1. Scroll so only the chart we're talking about is on the screen.
2. Hover over the points we mention, so our audience can see the exact numbers.
3. Practise using our controls during the Aha Moment, so we don't fumble them in front of the class.
4. If we go over three minutes, cut words, not the Aha Moment.

!!! warning "Check the class server first"
    Before our talk, open our story on the class server and scroll through it to the end. If it's slow or shows an empty page, tell our teacher straight away, and present from `marimo run` on our own computer instead.

## Giving feedback

While each person presents, we'll give them a **peer review**. It has two parts.

### The arc checklist

For each stage, decide whether the presenter's story did it, and write **yes**, **partly** or **no**:

1. **Hook:** the question was clear, and we wanted to know the answer.
2. **Behind the Scenes:** we knew what data they used and where it came from.
3. **Rising Insights:** each insight had a number and a chart, and they built towards the Aha Moment.
4. **Aha Moment:** the Aha chart answered the question in one look, with a headline title and the finding highlighted.
5. **Resolution:** they answered the question and gave at least one honest limitation.
6. **Charts:** every chart had clear labels and the right type of chart for its question.
7. **Time:** they finished within three minutes.

### Two stars and a wish

Then write **two stars and a wish**: two things that worked well, and one thing to improve. Make each one specific, so the presenter knows exactly what to keep and what to change.

```text title="Feedback for Sam"
Star: your Aha chart was really clear. The orange line made the
  difference jump out straight away.
Star: using the slider to show the gap started in 2020 was convincing.
Wish: your scatter plot had no headline title, so I wasn't sure what
  it was meant to show.
```

!!! tip "Specific beats nice"
    "Great job!" feels good, but it doesn't help anyone improve. "Your box plot's title told me the finding before I read the axes" tells the presenter exactly what to keep doing.

## Making our final edits

After our talk, we'll get feedback from several classmates. Read it all, then look for the points that more than one person made. Those are the ones to fix first.

1. Under our `## Lesson 16: Presenting` heading in ***my_data_story.md***, copy in the feedback we got.
2. Choose up to three changes to make, and write down why.
3. Make the changes in ***steam_story.py***, check our story again with `marimo run`, then hand in the final version the same way as in Lesson 15.

## Our data story

Under the `## Lesson 16: Presenting` heading in ***my_data_story.md***, finish our data story with a reflection:

1. What was the most interesting thing we found in our data, and how did we find it?
2. Which stage of the data story arc was hardest to get right, and what did we do about it?
3. If we had another week, what other question would we ask of our data?
