# Setting Up

!!! learn "On this page we will learn"
    - how to install Python and VS Code
    - how to create a project folder and a virtual environment
    - how to install Polars, Plotly and marimo
    - how to download the Steam data
    - how to open our first marimo notebook

We'll do all our work in a project folder on our own computer, using **VS Code** to manage our files and **marimo** to write our code. Before we start, we need to install the tools, download the data and check everything works. Follow each step in order.

Most steps are the same on Windows and macOS. Where they're different, the page has a tab for each, so click the tab for our computer.

## Install Python and VS Code

If Python and VS Code are already on our computer, skip to [Create the project folder](#create-the-project-folder).

1. Download and install Python from [python.org](https://www.python.org/downloads/).
    - **Why:** all our code is Python, and the libraries we use are Python libraries.

    === "Windows"

        - **Important:** on the first screen of the installer, tick **Add python.exe to PATH**.
        - **Expected result:** the installer finishes with "Setup was successful".

        <!-- SCREENSHOT: assets/setup_python_windows.png — Windows Python installer first screen, "Add python.exe to PATH" ticked -->

    === "macOS"

        - **Important:** download the **macOS 64-bit universal2 installer**, open the ***.pkg*** file and click **Continue** through each screen.
        - **Expected result:** the installer finishes with "The installation was successful" and a ***Python*** folder opens in Finder. We can close it.

        <!-- SCREENSHOT: assets/setup_python_macos.png — macOS Python installer, "The installation was successful" screen -->

2. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
    - **Why:** VS Code is where we'll manage our files and type commands.
    - **Expected result:** VS Code opens with a Welcome tab. On a Mac, drag **Visual Studio Code** into the ***Applications*** folder first, so it's easy to find.
3. In VS Code, click the **Extensions** icon in the left bar, search for **Python** and install the extension by Microsoft.
    - **Why:** the extension lets VS Code use virtual environments.
    - **Expected result:** the Python extension shows as installed.

    <!-- SCREENSHOT: assets/setup_python_extension.png — VS Code Extensions panel with the Microsoft Python extension installed -->

## Create the project folder

1. Create a new folder called ***steam_data_stories*** somewhere easy to find, such as our ***Documents*** folder.
    - **Why:** our data and both of our notebooks will live in this folder.
    - **Expected result:** an empty ***steam_data_stories*** folder.
2. In VS Code, choose **File** → **Open Folder…** and open the ***steam_data_stories*** folder. If VS Code asks whether we trust the authors of the files, choose **Yes**.
    - **Why:** VS Code works with everything in the open folder, and the terminal will start in this folder.
    - **Expected result:** the Explorer panel on the left shows **STEAM_DATA_STORIES** with no files.

    <!-- SCREENSHOT: assets/setup_open_folder.png — VS Code Explorer showing the empty STEAM_DATA_STORIES folder -->

## Create a virtual environment

A **virtual environment** is a private copy of Python just for this project. The libraries we install go into the virtual environment rather than into the computer's main Python, so different projects can't interfere with each other.

1. Press ++ctrl+shift+p++ (++cmd+shift+p++ on a Mac), type **Python: Create Environment** and press ++enter++. Choose **Venv**, then choose the Python version we installed.
    - **Why:** this creates the virtual environment in a folder called ***.venv*** inside our project.
    - **Expected result:** after a few seconds a ***.venv*** folder appears in the Explorer panel.

    <!-- SCREENSHOT: assets/setup_create_environment.png — Command Palette with "Python: Create Environment" typed, then Venv chosen -->
2. Choose **Terminal** → **New Terminal**.
    - **Why:** we'll type commands to install libraries and start marimo in the terminal.
    - **Expected result:** a terminal opens at the bottom of VS Code. The prompt starts with `(.venv)`, which means the virtual environment is active.

    <!-- SCREENSHOT: assets/setup_venv_terminal.png — VS Code terminal with the (.venv) prompt (one each for Windows and macOS if they look different) -->

!!! warning "No (.venv) in the terminal"
    If the prompt doesn't start with `(.venv)`, close the terminal with the bin icon and open a new one. Libraries installed without `(.venv)` go into the wrong Python, and marimo won't be able to find them.

## Install the libraries

1. In the terminal, type the command below and press ++enter++.

    ```text
    pip install marimo polars==2.0.0rc2 plotly numpy requests
    ```

    - **Why:** this installs marimo (our notebook), Polars (for working with tables of data), Plotly (for charts), NumPy (which Plotly needs to draw charts from Polars data) and Requests (for getting data from the internet in Lesson 13).
    - **Expected result:** lots of downloading messages, ending with a line starting `Successfully installed`.

    <!-- SCREENSHOT: assets/setup_pip_install.png — terminal after pip install, showing the "Successfully installed" line -->
2. Check marimo installed correctly by typing:

    ```text
    marimo --version
    ```

    - **Expected result:** a version number such as `0.25.1`. Ours might be a little different.

!!! tip "Why polars==2.0.0rc2?"
    The `==2.0.0rc2` part asks for one exact version of Polars. **rc** stands for **release candidate**: a version that's almost finished and being tested before its official release. Polars 2.0 changes a few commands, and this course uses the new versions, so we all need the same one.

## Download the data

1. Go to the [Steam Data Stories data page](https://github.com/DamoM73/steam-data-stories/releases/latest) and click the file that starts with ***steam_data_stories_data*** and ends in ***.zip*** to download it.
    - **Why:** this zip holds our classroom copy of the Steam data. Everyone in the class uses the same copy, so our results match the lessons.
    - **Expected result:** the zip file appears in our ***Downloads*** folder. It's large, so it might take a minute.

    <!-- SCREENSHOT: assets/setup_release_download.png — GitHub release page with the steam_data_stories_data zip highlighted -->
2. Unzip the data into a folder called ***data*** inside our project.
    - **Why:** our notebooks will look for the data in the ***data*** folder.

    === "Windows"

        Right-click the zip file and choose **Extract All…**. Click **Browse…**, choose our ***steam_data_stories*** folder, then add `\data` to the end of the folder path and click **Extract**.

        <!-- SCREENSHOT: assets/setup_extract_windows.png — Windows "Extract Compressed (Zipped) Folders" dialog with the path ending in \data -->

    === "macOS"

        Double-click the zip file in Finder. macOS unzips it into a new folder with the same name as the zip. Rename that folder to `data`, then drag it into our ***steam_data_stories*** folder.

        <!-- SCREENSHOT: assets/setup_extract_macos.png — Finder showing the unzipped folder renamed to data inside steam_data_stories -->

    - **Expected result:** VS Code's Explorer panel shows a ***data*** folder holding ***README.txt***, ***steam_games.csv*** and a ***player_history*** folder.

    <!-- SCREENSHOT: assets/setup_data_folder.png — VS Code Explorer with the data folder expanded -->

Our project folder should now look like this:

```text
steam_data_stories/
    .venv/
    data/
        player_history/
        README.txt
        steam_games.csv
```

!!! warning "Don't open steam_games.csv"
    ***steam_games.csv*** is about 400 MB. Opening it in VS Code, Excel or Numbers will be very slow and might freeze the program. We'll look at it with code instead, starting in Lesson 2.

## Open our first notebook

1. In the terminal, type the command below and press ++enter++.

    ```text
    marimo edit clean_steam.py
    ```

    - **Why:** this starts marimo and creates a new notebook called ***clean_steam.py***. We'll use this notebook to explore and clean our data in Lessons 2–8.
    - **Expected result:** the terminal shows "Edit clean_steam.py in your browser" with a URL, a new tab opens in our web browser showing an empty marimo notebook, and ***clean_steam.py*** appears in VS Code's Explorer panel.

    <!-- SCREENSHOT: assets/setup_marimo_empty.png — browser tab with the new, empty clean_steam.py marimo notebook (plus the terminal message if useful) -->
2. Back in VS Code, click in the terminal and press ++ctrl+c++ (also ++ctrl+c++ on a Mac, not ++cmd+c++). When marimo asks "Are you sure you want to quit? (y/N)", type `y` and press ++enter++.
    - **Why:** marimo keeps running in the terminal until we stop it. It asks first so we don't stop it by accident.
    - **Expected result:** the terminal shows the `(.venv)` prompt again, and the browser tab says it has lost its connection.

    <!-- SCREENSHOT: assets/setup_marimo_quit.png — terminal showing marimo's "Are you sure you want to quit? (y/N)" prompt -->

!!! warning "Keep the terminal open"
    The marimo notebook in our browser only works while marimo is running in the VS Code terminal. If we close the terminal or press ++ctrl+c++ (on Windows and macOS), the notebook stops working. On a Mac, closing the VS Code window or quitting VS Code with ++cmd+q++ also closes the terminal and stops marimo. Our code is saved in ***clean_steam.py***, so we can start marimo again with the same command and carry on.

Our computer is ready. In the first lesson we'll find out what makes a good data story.
