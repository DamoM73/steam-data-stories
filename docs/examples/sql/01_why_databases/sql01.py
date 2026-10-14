import marimo as mo
import sqlite3

conn = sqlite3.connect(mo.notebook_dir() / "data" / "steam.db")
