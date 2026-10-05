page = response.json()
first_page = pl.DataFrame(page["history"])
page["nextCursor"], first_page.height
