# Finding Data

!!! learn "On this page we will learn"
    - how to choose a dataset for our own data story
    - where to find open data about Brisbane and South East Queensland
    - where to find data about Queensland, Australia and the world
    - how to record where our data came from

!!! terms "Terminology"
    - **open data** – data that anyone can download, use and share for free, as long as we follow its licence.

After the tutorials, we'll tell a new data story with data we find ourselves. Lots of organisations publish **open data**: data that anyone can download, use and share for free, as long as we follow its licence. This page lists good places to start, beginning close to home.

## Choosing a dataset

Before we spend time on a dataset, check it against this list. Each check comes from something we did in the tutorials.

1. **We can download it as a CSV file**, without writing code or using an API. Then we can load it with `pl.read_csv`, just like in [Lesson 2](../hook/02_exploring_data.md#load-the-data).
2. **It has enough rows.** A few hundred rows or more gives us groups big enough to compare. Remember the warning about small groups in [Lesson 8](../insights/08_summarising_groups.md#games-per-year).
3. **It has columns we can compare**, such as a group column (like suburb, sport or genre) and a number column (like visitors, rainfall or price). A date column lets us look for trends.
4. **We know what every column means.** Look for a page that describes the columns, often called a data dictionary.
5. **It has no personal information**, or we can remove it, just like the support emails in [Lesson 4](../hook/04_privacy_ethics.md#removing-columns-we-dont-need).
6. **Its licence lets us reuse it**, and we know how to give attribution. See [Lesson 4](../hook/04_privacy_ethics.md#licences-and-attribution).
7. **It can answer an investigable question** that's specific, measurable and open. See [Lesson 3](../hook/03_asking_questions.md#investigable-questions).

!!! tip "Question first, or data first?"
    We can start with a question and look for data that answers it, or browse a portal until a dataset makes us curious. Either way works, but check the dataset against the list above before we commit to it.

## Brisbane and South East Queensland

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [Brisbane City Council open data](https://data.brisbane.qld.gov.au/){ target="_blank" rel="noopener" } | hundreds of datasets about Brisbane, such as library checkouts, bikeway counts and council events. They're also listed on the [Queensland Government open data portal](https://www.data.qld.gov.au/organization/brisbane-city-council){ target="_blank" rel="noopener" } | Which Brisbane library branch borrows the most books in a language other than English? |
| [Translink monthly performance data](https://www.data.qld.gov.au/dataset/translink-monthly-performance-data){ target="_blank" rel="noopener" } | public transport patronage, customer satisfaction and complaints for South East Queensland, as CSV files | How has public transport patronage in South East Queensland changed since 2019? |
| [Seqwater historic dam levels](https://www.seqwater.com.au/historic-dam-levels){ target="_blank" rel="noopener" } | daily levels of South East Queensland's dams, including Wivenhoe and Somerset. Choose the dates and dams, then **Download as CSV** | How low did our dams get in dry years, and how quickly did they refill? |
| [Atlas of Living Australia](https://www.ala.org.au/){ target="_blank" rel="noopener" } | sightings of plants and animals, which we can filter to Brisbane. Downloading records needs us to log in | In which months are koalas reported most often around Brisbane? |

## Queensland

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [Queensland Government open data portal](https://www.data.qld.gov.au/){ target="_blank" rel="noopener" } | thousands of datasets from Queensland government departments and councils, many as CSV files | |
| [Queensland state school enrolments](https://www.data.qld.gov.au/dataset/state-school-enrolments){ target="_blank" rel="noopener" } | the number of students at each state school, by year | Which schools around Brisbane have grown the fastest? |
| [Queensland Regional Profiles](https://statistics.qgso.qld.gov.au/qld-regional-profiles){ target="_blank" rel="noopener" } | statistics about any Queensland region, such as population, age and housing, from the Queensland Government Statistician's Office | How does the age of people in our suburb compare with the rest of Brisbane? |

## Australia

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [ABS Data Explorer](https://dataexplorer.abs.gov.au/){ target="_blank" rel="noopener" } | official statistics from the Australian Bureau of Statistics, such as population, jobs and prices. Choose the data, then export it as a CSV file | Which Australian states are growing fastest? |
| [Bureau of Meteorology Climate Data Online](https://www.bom.gov.au/climate/data/){ target="_blank" rel="noopener" } | daily and monthly rainfall and temperatures from weather stations, including several in Brisbane, going back many years. Downloads come as CSV files | Are Brisbane's summers getting hotter? |
| [data.gov.au](https://data.gov.au/){ target="_blank" rel="noopener" } | the Australian Government's open data portal, which also lists many state and council datasets | |

## The world

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [Our World in Data](https://ourworldindata.org/){ target="_blank" rel="noopener" } | charts about health, energy, the environment and more for every country. Every chart has a **Download** button with the data as a CSV file | How does Australia's energy use compare with other countries? |
| [Gapminder](https://www.gapminder.org/data/){ target="_blank" rel="noopener" } | country statistics going back hundreds of years, as CSV or Excel files. Data can be reused freely, as long as we attribute the original source and Gapminder | How has life expectancy in Australia changed compared with the rest of the world? |

## Kaggle

[Kaggle](https://www.kaggle.com/datasets){ target="_blank" rel="noopener" } has thousands of datasets shared by its users, about topics like games, music, sport and films. It's a great place to find a dataset about something we're interested in, but there are two things to know first:

- **It needs an account.** Students under 16 need a parent or guardian's permission to have one, so check with our teacher before signing up.
- **Anyone can upload a dataset.** Some are excellent, and some are copied, out of date or made up. Check the dataset's page for where the data came from, when it was collected and its licence. If it doesn't say, choose a different dataset.

!!! warning "Avoid data about people"
    Some open datasets describe individual people, or sensitive topics such as crime or health. Even when they're published openly, they can hurt or identify real people. For our data story, choose data about things, places and events, such as games, weather, transport or animals.

## Recording our source

As soon as we choose a dataset, add a heading `## Our data source` to ***my_data_story.md*** and record:

1. the name of the dataset and who published it
2. its web address
3. the date we downloaded it
4. its licence, and the attribution it asks for
5. what one row represents, just like we worked out for the Steam data in [Lesson 1](../hook/01_data_story.md#what-one-row-represents)

We'll need all of these for the attribution in our finished story.
