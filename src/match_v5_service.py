'''Responsible for contacting the riot games MATCH-V5 API and logging errors'''
import requests
import dotenv
import os
import json
from http import HTTPStatus


dotenv.load_dotenv()
BASE_MATCH_URL = 'https://europe.api.riotgames.com/lol/match/v5/matches'
API_KEY = os.environ.get("LEAGUE_API_KEY")
PUUID = os.environ.get("LEAGUE_PUUID")


def get_match_ids(num_matches: int):
    '''Fetches match ids for the player'''
    url = f"{BASE_MATCH_URL}/by-puuid/{PUUID}/ids?queue=420&start=0&count={num_matches}"
    api_response = requests.get(url, headers={"X-Riot-Token": API_KEY})

    print(f"MATCH-API matches-by-puuid response: {api_response.status_code}")
    if (api_response.status_code != HTTPStatus.OK):
        print(
            f"MATCH-V5 API error {api_response.status_code}: error accessing MATCH-API")
        return None

    match_id_list = json.loads(api_response.content.decode())
    print(f"Match list: {match_id_list}")

    return match_id_list


def get_match_data_by_id(match_id: str):
    '''Fetches match data for a given match id'''
    url = f"{BASE_MATCH_URL}/{match_id}"
    api_response = requests.get(url, headers={"X-Riot-Token": API_KEY})

    print(f"MATCH-API matches-data-by-id response: {api_response.status_code}")
    if (api_response.status_code != HTTPStatus.OK):
        print(
            f"MATCH-V5 API error {api_response.status_code}: error accessing MATCH-API")
        return None

    match_data = json.loads(api_response.content.decode())
    print(f"Match data: {match_data}")
    return match_data
