time.sleep(2)
next_response = requests.get(
    API_URL,
    params={"cursor": page["nextCursor"]},
    timeout=30,
)
second_page = pl.DataFrame(next_response.json()["history"])
pl.concat([first_page, second_page])
