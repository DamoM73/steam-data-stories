# Setting Up

!!! learn "On this page we will learn"
    - how to install Python and VS Code
    - how to create a project folder and a virtual environment
    - how to install Polars, Plotly and marimo
    - how to download the Steam data
    - how to open our first marimo notebook

!!! terms "Terminology"
    - **release candidate** – a version of a program that's almost finished and being tested before its official release.
    - **PowerShell** – the program VS Code uses for its terminal on Windows unless we choose another one.
    - **Command Prompt** – an older Windows terminal program that can switch on a virtual environment without running a PowerShell script.

We'll do all our work in a project folder on our own computer, using **VS Code** to manage our files and **marimo** to write our code. Before we start, we need to install the tools, download the data and check everything works. Follow each step in order.

Most steps are the same on Windows and macOS. Where they're different, the page has a tab for each, so click the tab for our computer.

## Install Python and VS Code

If Python and VS Code are already on our computer, skip to [Create the project folder](#create-the-project-folder).

1. Download and install Python from [python.org](https://www.python.org/downloads/).
    - **Why:** all our code is Python, and the libraries we use are Python libraries.

    === "Windows"

        - **Important:** choose the installer that matches our computer's processor. Open **Settings** → **System** → **About** and look at **System type**:
            - **x64-based processor** → download **Windows installer (64-bit)**
            - **ARM-based processor** → download **Windows installer (ARM64)**
        - **Important:** on the first screen of the installer, tick **Add python.exe to PATH**.
        - **Expected result:** the installer finishes with "Setup was successful".

    === "macOS"

        - **Important:** download the **macOS 64-bit universal2 installer**, open the ***.pkg*** file and click **Continue** through each screen.
        - **Expected result:** the installer finishes with "The installation was successful" and a ***Python*** folder opens in Finder. We can close it.

2. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
    - **Why:** VS Code is where we'll manage our files and type commands.
    - **Windows:** if our **System type** says **ARM-based processor**, choose the **Arm64** download.
    - **Expected result:** VS Code opens with a Welcome tab. On a Mac, drag **Visual Studio Code** into the ***Applications*** folder first, so it's easy to find.
3. In VS Code, click the **Extensions** icon in the left bar, search for **Python** and install the extension by Microsoft.
    - **Why:** the extension lets VS Code use virtual environments.
    - **Expected result:** the Python extension shows as installed.

## Create the project folder

1. Create a new folder called ***steam_data_stories*** somewhere easy to find, such as our ***Documents*** folder.
    - **Why:** our data and both of our notebooks will live in this folder.
    - **Expected result:** an empty ***steam_data_stories*** folder.
2. In VS Code, choose **File** → **Open Folder…** and open the ***steam_data_stories*** folder. If VS Code asks whether we trust the authors of the files, choose **Yes**.
    - **Why:** VS Code works with everything in the open folder, and the terminal will start in this folder.
    - **Expected result:** the Explorer panel on the left shows **STEAM_DATA_STORIES** with no files.

## Create a virtual environment

A **virtual environment** is a private copy of Python just for this project. The libraries we install go into the virtual environment rather than into the computer's main Python, so different projects can't interfere with each other.

1. Press ++ctrl+shift+p++ (++cmd+shift+p++ on a Mac), type **Python: Create Environment** and press ++enter++. Choose **Venv**, then choose the Python version we installed.
    - **Why:** this creates the virtual environment in a folder called ***.venv*** inside our project.
    - **Expected result:** after a few seconds a ***.venv*** folder appears in the Explorer panel.

2. Choose **Terminal** → **New Terminal**.
    - **Why:** we'll type commands to install libraries and start marimo in the terminal.
    - **Expected result:** a terminal opens at the bottom of VS Code. The prompt starts with `(.venv)`, which means the virtual environment is active.

!!! warning "No (.venv) in the terminal"
    If the prompt doesn't start with `(.venv)`, close the terminal with the bin icon and open a new one. Libraries installed without `(.venv)` go into the wrong Python, and marimo won't be able to find them.

### Running scripts is disabled (Windows)

On some Windows computers, the new terminal shows an error like this instead of the `(.venv)` prompt:

``` { .text .error linenums="1" }
Activate.ps1 cannot be loaded because running scripts is disabled
```

- **line 1** → ***Activate.ps1*** is the script that switches on our virtual environment in **PowerShell**, the terminal VS Code uses on Windows. The computer's settings don't allow PowerShell to run scripts, so the virtual environment stays switched off.

We don't need to change the computer's settings. Instead, we'll tell VS Code to use **Command Prompt**, which switches on the virtual environment without a PowerShell script.

1. Press ++ctrl+shift+p++, type **Terminal: Select Default Profile** and press ++enter++. Choose **Command Prompt**.
    - **Why:** every new terminal in VS Code will now open as Command Prompt instead of PowerShell.
    - **Expected result:** the list closes. Nothing else changes yet, because the terminal that's already open is still PowerShell.

2. Close the terminal with the bin icon, then choose **Terminal** → **New Terminal**.
    - **Why:** the new terminal opens as Command Prompt and switches on the virtual environment.
    - **Expected result:** the prompt starts with `(.venv)` and ends with the path to our ***steam_data_stories*** folder and a `>`.

## Install the libraries

1. In the terminal, type the command below and press ++enter++.

    ```text
    pip install marimo polars==2.0.0rc2 plotly numpy
    ```

    - **Why:** this installs marimo (our notebook), Polars (for working with tables of data), Plotly (for charts) and NumPy (which Plotly needs to draw charts from Polars data).
    - **Expected result:** lots of downloading messages, ending with a line starting `Successfully installed`.

2. Check marimo installed correctly by typing:

    ```text
    marimo --version
    ```

    - **Expected result:** a version number such as `0.25.1`. Ours might be a little different.

!!! tip "Why polars==2.0.0rc2?"
    The `==2.0.0rc2` part asks for one exact version of Polars. **rc** stands for **release candidate**: a version that's almost finished and being tested before its official release. Polars 2.0 changes a few commands, and this course uses the new versions, so we all need the same one.

## Download the data

1. In VS Code's Explorer panel, hover over **STEAM_DATA_STORIES**, click the **New Folder** icon and name the folder `data`.
    - **Why:** our notebooks will look for the data in the ***data*** folder.
    - **Expected result:** an empty ***data*** folder appears in the Explorer panel, under ***.venv***.

2. Download both data files: [steam_games.csv](../downloads/steam_games.csv){ download="steam_games.csv" } and [README.txt](../downloads/README.txt){ download="README.txt" }.
    - **Why:** ***steam_games.csv*** is our classroom copy of the Steam data. Everyone in the class uses the same copy, so our results match the lessons. ***README.txt*** explains where the data came from and includes its licence.
    - **Expected result:** both files appear in our ***Downloads*** folder.
3. Open our ***Downloads*** folder in File Explorer (Finder on a Mac), then drag both files onto the ***data*** folder in VS Code's Explorer panel. If VS Code asks whether to copy or move them, choose **Copy**.
    - **Why:** the files need to be inside our project's ***data*** folder, not in ***Downloads***.
    - **Expected result:** VS Code's Explorer panel shows a ***data*** folder holding ***README.txt*** and ***steam_games.csv***.

!!! warning "Check the file names"
    If we download a file more than once, the browser may rename it, such as ***steam_games (1).csv***. Our code looks for ***steam_games.csv*** exactly, so rename the file or delete the extra copy.

Our project folder should now look like this:

```text
steam_data_stories/
    .venv/
    data/
        README.txt
        steam_games.csv
```

!!! warning "Don't change steam_games.csv"
    ***steam_games.csv*** is our original data. If we open it in Excel or Numbers and save it, the program can quietly change values, such as turning dates into a different format. We'll only ever read it with code, starting in Lesson 2, and save our cleaned data as a new file.

## Open our first notebook

1. In the terminal, type the command below and press ++enter++.

    ```text
    marimo edit clean_steam.py
    ```

    - **Why:** this starts marimo and creates a new notebook called ***clean_steam.py***. We'll use this notebook to explore and clean our data in Lessons 2–6.
    - **Expected result:** the terminal shows "Edit clean_steam.py in your browser" with a URL, a new tab opens in our web browser showing an empty marimo notebook, and ***clean_steam.py*** appears in VS Code's Explorer panel.

    <!-- SCREENSHOT: assets/setup_marimo_empty.png — browser tab with the new, empty clean_steam.py marimo notebook (plus the terminal message if useful) -->
2. Back in VS Code, click in the terminal and press ++ctrl+c++ (also ++ctrl+c++ on a Mac, not ++cmd+c++). When marimo asks "Are you sure you want to quit? (y/N)", type `y` and press ++enter++.
    - **Why:** marimo keeps running in the terminal until we stop it. It asks first so we don't stop it by accident.
    - **Expected result:** the terminal shows the `(.venv)` prompt again, and the browser tab says it has lost its connection.

!!! warning "Keep the terminal open"
    The marimo notebook in our browser only works while marimo is running in the VS Code terminal. If we close the terminal or press ++ctrl+c++ (on Windows and macOS), the notebook stops working. On a Mac, closing the VS Code window or quitting VS Code with ++cmd+q++ also closes the terminal and stops marimo. Our code is saved in ***clean_steam.py***, so we can start marimo again with the same command and carry on.

Our computer is ready. In the first lesson we'll find out what makes a good data story.
