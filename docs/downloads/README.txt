Steam Data Stories: classroom data (2026-10-07)

Files
  steam_games.csv   one row per Steam game (10250 games with at least
                    500 reviews)

The data is real and has NOT been cleaned. Cleaning it is part of the
course: https://damom73.github.io/steam-data-stories/

Sources
  steam_games.csv is built from the Steam Games Dataset by Fronkon Games
  (https://huggingface.co/datasets/FronkonGames/steam-games-dataset),
  downloaded 2026-10-07, which collects data from the Steam store and SteamSpy.
  Changes made for the classroom copy:
    - only games with at least 500 reviews are included
    - only 13 columns are kept
    - games with no genres are removed
    - games with adult content are removed

Licences
  The Steam Games Dataset is published under the MIT licence:

  Copyright (c) Fronkon Games

  Permission is hereby granted, free of charge, to any person obtaining a
  copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to permit
  persons to whom the Software is furnished to do so, subject to the
  following conditions:

  The above copyright notice and this permission notice shall be included
  in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
  NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
  USE OR OTHER DEALINGS IN THE SOFTWARE.

  Steam and game names are trademarks of their owners. This data is for
  classroom use and isn't affiliated with Valve or Steam.
