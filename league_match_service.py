import requests
import dotenv
import os
import json


dotenv.load_dotenv()


BASE_MATCH_URL = 'https://europe.api.riotgames.com/lol/match/v5/matches'
API_KEY = os.environ.get("LEAGUE_API_KEY")
PUUID = os.environ.get("LEAGUE_PUUID")


def get_latest_match_id():
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?queue=420&start=0&count=1"
    api_response = requests.get(url, headers={"X-Riot-Token": API_KEY})

    print(f"MATCH-API matches-by-puuid response: {api_response.status_code}")
    if (api_response.status_code != 200):
        print("Error accessing MATCH-API")
        return None

    match_id_list = json.loads(api_response.content.decode())
    print(f"Match list: {match_id_list}")
    if len(match_id_list) == 0:
        print("No latest match found")
        return None

    latest_match_id = match_id_list[0]
    print(f"Latest match : {latest_match_id}")
    return latest_match_id
