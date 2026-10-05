def to_list(column):
    return pl.col(column).str.split(",")
