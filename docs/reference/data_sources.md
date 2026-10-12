# Finding Data

!!! learn "On this page we will learn"
    - how to choose a dataset for our own data story
    - where to find open data about Brisbane and South East Queensland
    - where to find data about Queensland, Australia and the world
    - where to find data about sport, games, movies, music, books and other things we're into
    - how to record where our data came from

!!! terms "Terminology"
    - **open data** – data that anyone can download, use and share for free, as long as we follow its licence.

After the tutorials, we'll tell a new data story with data we find ourselves, in [Your Data Story Project](../project/data_story_project.md). Lots of organisations publish **open data**: data that anyone can download, use and share for free, as long as we follow its licence. This page lists good places to start, beginning close to home, then data about sport, games, movies, music, books and other things we might be into. We can't use the Steam data for our project, because we've already told a story with it.

## Choosing a dataset

Before we spend time on a dataset, check it against this list. Each check comes from something we did in the tutorials.

1. **We can download it as a CSV or JSON file**, without writing code or using an API. Then we can load a CSV file with `pl.read_csv`, just like in [Exploring Our Data](../hook/02_exploring_data.md#load-the-data), or a JSON file as shown in [Loading JSON files](polars.md#loading-json-files).
2. **It has enough rows.** A few hundred rows or more gives us groups big enough to compare. Remember the warning about small groups in [Summarising Groups](../insights/08_summarising_groups.md#games-per-year).
3. **It has columns we can compare**, such as a group column (like suburb, sport or genre) and a number column (like visitors, rainfall or price). A date column lets us look for trends.
4. **We know what every column means.** Look for a page that describes the columns, often called a data dictionary.
5. **It has no personal information**, or we can remove it, just like the support emails in [Data, Privacy and Ethics](../hook/04_privacy_ethics.md#removing-columns-we-dont-need).
6. **Its licence lets us reuse it**, and we know how to give attribution. See [Data, Privacy and Ethics](../hook/04_privacy_ethics.md#licences-and-attribution).
7. **It can answer an investigable question** that's specific, measurable and open. See [Asking a Question Data Can Answer](../hook/03_asking_questions.md#investigable-questions).

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
| [ABS Cultural and creative activities](https://www.abs.gov.au/statistics/people/people-and-communities/cultural-and-creative-activities/2021-22){ target="_blank" rel="noopener" } | how many Australians take part in cultural activities, like singing or playing a musical instrument, by age group, including children aged 5 to 14. Download the tables at the bottom of the page | Are older children less likely to play a musical instrument than younger ones? |
| [data.gov.au](https://data.gov.au/){ target="_blank" rel="noopener" } | the Australian Government's open data portal, which also lists many state and council datasets | |

## The world

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [Our World in Data](https://ourworldindata.org/){ target="_blank" rel="noopener" } | charts about health, energy, the environment and more for every country. Every chart has a **Download** button with the data as a CSV file | How does Australia's energy use compare with other countries? |
| [Blood type distribution by country](https://en.wikipedia.org/wiki/Blood_type_distribution_by_country){ target="_blank" rel="noopener" } | the percentage of people with each blood type (A, B, AB and O, positive and negative) in over 100 countries. It's a Wikipedia table, so copy it into Google Sheets, then choose **File** → **Download** → **CSV** | Is O+ the most common blood type in every part of the world? |
| [Malaysia blood donations](https://data.moh.gov.my/data-catalogue/blood_donations){ target="_blank" rel="noopener" } | the number of blood donations in Malaysia every day, for each blood type, as a CSV file | Do blood donations drop during school holidays or festivals? |
| [Gapminder](https://www.gapminder.org/data/){ target="_blank" rel="noopener" } | country statistics going back hundreds of years, as CSV or Excel files. Data can be reused freely, as long as we attribute the original source and Gapminder | How has life expectancy in Australia changed compared with the rest of the world? |

## Sport

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [Cricsheet](https://cricsheet.org/downloads/){ target="_blank" rel="noopener" } | ball-by-ball data for thousands of cricket matches, including Tests, ODIs, T20 internationals, the Big Bash League and the IPL. Choose a competition, then download it in **CSV** format | Which Big Bash team hits the most sixes, and has that changed over the seasons? |
| [Basketball Reference](https://www.basketball-reference.com/){ target="_blank" rel="noopener" }, [FBref](https://fbref.com/){ target="_blank" rel="noopener" }, [Pro Football Reference](https://www.pro-football-reference.com/){ target="_blank" rel="noopener" } and [Hockey Reference](https://www.hockey-reference.com/){ target="_blank" rel="noopener" } | team and player statistics for the NBA, soccer leagues around the world (including the A-League), the NFL and the NHL. Above most tables, click **Export Data**, then **Get table as CSV**. Copy the text that appears into a new file in VS Code, and save it as a ***.csv*** file | Have NBA teams been shooting more three-pointers each season? |
| [Tennis data by Jeff Sackmann](https://github.com/JeffSackmann/tennis_atp){ target="_blank" rel="noopener" } | every men's professional tennis match since 1968, one CSV file per year, including the surface each match was played on. There's a [women's version](https://github.com/JeffSackmann/tennis_wta){ target="_blank" rel="noopener" } too. Click a file, then the download button. Check the page's licence before we use it | Do players serve more aces on grass courts than on clay? |
| [Useless NRL Stats](https://github.com/uselessnrlstats/uselessnrlstats){ target="_blank" rel="noopener" } | every NSWRL, ARL and NRL match since 1908 as CSV files, including scores, crowds, ladders and each player's tries and goals. There's NRLW and State of Origin data too. Open the ***cleaned_data*** folder, click a file, then the download button. The data comes from the Rugby League Project, so say that in our attribution | Are NRL games higher-scoring than they were 20 years ago? |
| [AFL Tables](https://afltables.com/afl/afl_index.html){ target="_blank" rel="noopener" } | AFL results and statistics going back to 1897. The tables are web pages, not CSV files, so look for an AFL dataset on Kaggle (below) instead, and use AFL Tables to check its numbers | Has home-ground advantage in the AFL changed over time? |

!!! tip "Players are people too"
    Sport data is about real people. A player's game statistics, like goals, runs or points, are public records of how they played, so they're fine to use. But leave out personal details, like a player's height, weight or date of birth, unless our question really needs them. Focus our story on teams, matches and seasons, and never use data to make fun of a player.

## Games, hobbies and other interests

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [Rebrickable LEGO database](https://rebrickable.com/downloads/){ target="_blank" rel="noopener" } | every LEGO set, theme, part and colour, as CSV files. Each file is compressed (it ends in ***.csv.gz***), so extract it before we load it. ***sets.csv*** has the year and number of parts of every set | Are LEGO sets getting bigger, and which themes have the most parts? |
| [StatCounter Global Stats](https://gs.statcounter.com/){ target="_blank" rel="noopener" } | the share of web traffic from each operating system, browser, device and screen size, plus how many website visits come from each social media site, for Australia or any country since 2009. Choose a chart, then **Download Data** | How quickly has Android caught up with iOS in Australia? |
| [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/){ target="_blank" rel="noopener" } | every planet found outside our solar system, including how and when it was discovered. Open the **Planetary Systems** table, then choose **Download Table** and **CSV format** | Which way of finding planets has found the most since 2010? |
| [FuelEconomy.gov](https://www.fueleconomy.gov/feg/download.shtml){ target="_blank" rel="noopener" } | fuel use, engine size and range for cars sold in the US since 1984, as one CSV file | How far can electric cars go on one charge, and has that improved? |

## Movies, TV, music, books and games

| Source | What's there | A question we could ask |
| :-- | :-- | :-- |
| [What we watched on Netflix](https://github.com/rfordatascience/tidytuesday/tree/main/data/2025/2025-07-29){ target="_blank" rel="noopener" } | ***movies.csv*** and ***shows.csv***: how many hours people spent watching every Netflix title from late 2023 to mid 2025, from Netflix's own engagement reports | Do new shows get watched more than older ones? |
| [Billboard Hot 100 number ones](https://github.com/rfordatascience/tidytuesday/tree/main/data/2025/2025-08-26){ target="_blank" rel="noopener" } | every song that reached number one on the US Billboard Hot 100, with how long it stayed there and details about the song | Do number one songs stay at the top for less time than they used to? |
| [Spotify songs](https://github.com/rfordatascience/tidytuesday/tree/main/data/2020/2020-01-21){ target="_blank" rel="noopener" } | about 30,000 Spotify songs with their genre, popularity, danceability, energy, tempo and instrumentalness (how likely a song is to have no singing) | Are instrumental songs less popular than songs with singing? |
| [Pixar films](https://github.com/rfordatascience/tidytuesday/tree/main/data/2025/2025-03-11){ target="_blank" rel="noopener" } | every Pixar film, with ratings from critics and audiences | Have Pixar's films been reviewed better or worse over time? |
| [goodbooks-10k](https://github.com/zygmuntz/goodbooks-10k){ target="_blank" rel="noopener" } | ***books.csv***: the 10,000 most-rated books on Goodreads, with their authors, year and average rating | Do older books get higher ratings than newer ones? |
| [Dungeons & Dragons monsters](https://github.com/rfordatascience/tidytuesday/tree/main/data/2025/2025-05-27){ target="_blank" rel="noopener" } | ***monsters.csv***: every monster in the free D&D rules (2024), with its type, size, challenge rating, armour class, hit points and ability scores | Which type of monster is toughest for its challenge rating? |
| [IMDb datasets](https://data.imdb.com/non-commercial-datasets){ target="_blank" rel="noopener" } | ratings, votes, genres, years and running times for millions of movies and TV shows. Free for personal and non-commercial use | Have movies been getting longer? |

For each TidyTuesday dataset (the first five above), open the link, click the ***.csv*** file, then the download button.

!!! tip "Challenge: loading the IMDb data"
    The IMDb files are much harder to load than our Steam data. They're compressed (they end in ***.tsv.gz***), so extract them first. They're **tab-separated**, not comma-separated, and they use `\N` to mean "missing". Some have millions of rows, so start with ***title.ratings.tsv*** and ***title.basics.tsv***. We can load them with `pl.read_csv("data/title.ratings.tsv", separator="\t", null_values="\\N")`. If we get an error about quotes, add `quote_char=None` inside the brackets too.

## Surveys of students like us

[CensusAtSchool New Zealand](https://new.censusatschool.org.nz/random-sampler/){ target="_blank" rel="noopener" } asks school students to fill in a survey about themselves every two years: things like their eye colour, whether they're left- or right-handed, their height, how they get to school and their reaction time. No names are collected. Its **random sampler** gives us a random sample of up to 1,000 students' answers, chosen by school year, from New Zealand, the USA or the international database (which includes Australian students). We must agree to its conditions of use first: the data is only for teaching and learning. A question we could ask: are left-handed students faster on the reaction-time test?

!!! tip "Data about bodies"
    Data like eye colour, height and blood type is about people's bodies, so we use it carefully. Every source above shares it without names, or as totals for a whole country. Keep it that way: never try to work out who a row belongs to, and never collect this kind of data from our classmates without our teacher's approval.

## TidyTuesday

[TidyTuesday](https://github.com/rfordatascience/tidytuesday){ target="_blank" rel="noopener" } is a weekly data project that has shared a new dataset every week since 2018, over 400 so far. Every dataset is a clean CSV file on GitHub, so we don't need an account. Each week's page describes every column and says where the data came from. Browse the tables of datasets by year to find one that interests us. In 2025 alone there were datasets about Pokémon, chess player ratings, EuroLeague basketball and Australian frogs.

Lots of other datasets about video games, Pokémon, Formula 1, chess, football, streamers and podcasts are on Kaggle. See below.

## Kaggle

[Kaggle](https://www.kaggle.com/datasets){ target="_blank" rel="noopener" } has thousands of datasets shared by its users, about topics like games, music, sport and films. It's a great place to find a dataset about something we're interested in. Try searching for:

- [Pokémon](https://www.kaggle.com/datasets?search=pokemon){ target="_blank" rel="noopener" }: the stats and types of every Pokémon
- [video game sales](https://www.kaggle.com/datasets?search=video+game+sales){ target="_blank" rel="noopener" }: sales of games by platform, genre and year
- [Formula 1](https://www.kaggle.com/datasets?search=formula+1){ target="_blank" rel="noopener" }: every race, driver and result since 1950
- [AFL](https://www.kaggle.com/datasets?search=afl){ target="_blank" rel="noopener" }, [NRL](https://www.kaggle.com/datasets?search=nrl){ target="_blank" rel="noopener" } or [Big Bash](https://www.kaggle.com/datasets?search=big+bash){ target="_blank" rel="noopener" }: Australian sport results and statistics
- [chess](https://www.kaggle.com/datasets?search=chess+games){ target="_blank" rel="noopener" }: thousands of online chess games and their results
- [Twitch streamers](https://www.kaggle.com/datasets/aayushmishra1512/twitchdata){ target="_blank" rel="noopener" }: the top 1,000 Twitch streamers, with their watch time, followers, viewers and language
- [Spotify podcasts](https://www.kaggle.com/datasets?search=spotify+podcasts){ target="_blank" rel="noopener" }: daily podcast charts from Spotify
- [Netflix](https://www.kaggle.com/datasets?search=netflix+titles){ target="_blank" rel="noopener" }, [Disney+](https://www.kaggle.com/datasets?search=disney+plus){ target="_blank" rel="noopener" } or [Prime Video](https://www.kaggle.com/datasets?search=amazon+prime+titles){ target="_blank" rel="noopener" }: every movie and show on each streaming service
- [Spotify tracks](https://www.kaggle.com/datasets?search=spotify+tracks){ target="_blank" rel="noopener" }: songs with their genre, popularity and features
- [Metacritic games](https://www.kaggle.com/datasets?search=metacritic+games){ target="_blank" rel="noopener" }: critic and player scores for thousands of games, with their platform and release date
- [game consoles](https://www.kaggle.com/datasets?search=best+selling+game+consoles){ target="_blank" rel="noopener" }: the best-selling game consoles of all time, with their maker, release year and units sold
- [social media](https://www.kaggle.com/datasets?search=social+media+users){ target="_blank" rel="noopener" }: how many people use each social media platform
- [EA SPORTS FC](https://www.kaggle.com/datasets?search=ea+fc+player+ratings){ target="_blank" rel="noopener" } or [FIFA](https://www.kaggle.com/datasets?search=fifa+player+ratings){ target="_blank" rel="noopener" }: the ratings of every player in the game

There are two things to know first:

- **It needs us to sign in** before we can download a dataset. Choose **Sign in with Google** and use our school Google account.
- **Anyone can upload a dataset.** Some are excellent, and some are copied, out of date or made up. Check the dataset's page for where the data came from, when it was collected and its licence. If it doesn't say, choose a different dataset.

!!! warning "Avoid private data about people"
    Some open datasets describe individual people's private lives, or sensitive topics such as crime or health. Even when they're published openly, they can hurt or identify real people. For our data story, choose data about things, places and events, such as sport results, games, weather, transport or animals.

## Recording our source

As soon as we choose a dataset, add a heading `## Our data source` to ***my_data_story.md*** and record:

1. the name of the dataset and who published it
2. its web address
3. the date we downloaded it
4. its licence, and the attribution it asks for
5. what one row represents, just like we worked out for the Steam data in [What is a Data Story?](../hook/01_data_story.md#what-one-row-represents)

We'll need all of these for the attribution in our finished story.
