API_URL = "https://games-popularity.com/swagger/api/game/players/1808500"
response = requests.get(API_URL, timeout=30)
response.status_code
