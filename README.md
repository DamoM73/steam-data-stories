# Steam Data Stories

Tutorials for telling data stories about Steam games with Python, [Polars](https://pola.rs/), [Plotly Express](https://plotly.com/python/plotly-express/) and [marimo](https://marimo.io/). Written for Year 9 Digital Technologies students using VS Code.

Live site: <https://damom73.github.io/steam-data-stories/> (once published)

## Preview the site

```
pip install -r requirements.txt
zensical serve
```

Then open <http://localhost:8000>. To build the site: `zensical build --clean` (expect `No issues found`).

## Scripts

- `python scripts/check_explanations.py` checks every Code explanation box against the code it explains (expect `0 issue(s) found`).

## Layout

```
zensical.toml                 site config and navigation
docs/
  index.md                    home page
  start/                      introduction, setting up
  hook/                       lessons 1–4: data stories, exploring, questions, privacy
  cleaning/                   lessons 5–8: behind the scenes (cleaning)
  insights/                   lessons 9–14: rising insights, API, joins
  aha/                        lesson 15: the aha moment
  resolution/                 lesson 16: publishing
  reference/                  story arc, Polars, Plotly, marimo, errors, licence
  assets/                     images
  stylesheets/extra.css       colours, callouts and code block styles
scripts/                      check_explanations.py
```

## Licence

Content is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Code is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html). The Steam Games Dataset by Fronkon Games is MIT licensed.
