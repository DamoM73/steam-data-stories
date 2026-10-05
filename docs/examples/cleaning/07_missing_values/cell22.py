from datetime import date

DATA_DATE = date(2026, 10, 5)

checks = {
    "every AppID is different": missing["AppID"].is_unique().all(),
    "no negative prices": (missing["Price"] >= 0).all(),
    "every game has a name": missing["Name"].null_count() == 0,
    "no release dates after the data date": (
        missing["Release date"] <= DATA_DATE
    ).all(),
}
checks
