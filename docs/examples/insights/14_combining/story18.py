history.filter(pl.struct("AppID", "added").is_duplicated()).height
