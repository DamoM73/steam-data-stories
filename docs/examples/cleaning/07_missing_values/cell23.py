checked = missing.filter(
    pl.col("Name").is_not_null(),
    pl.col("Release date") <= DATA_DATE,
)
checked.height
