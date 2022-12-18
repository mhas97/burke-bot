import dotenv
import os


PUUID = os.environ.get("LEAGUE_PUUID")


def get_bot_string_from_match_data(match_data):
    participants = match_data["info"]["participants"]
    player_list = [p for p in participants if p["puuid"] == PUUID]
    if (len(player_list) != 1):
        return "No match data found"

    player = player_list[0]
    won = player["win"]
    result_string = "was victorious" if won else "was defeated"
    kills = player["kills"]
    deaths = player["deaths"]
    assists = player["assists"]
    kda = kills+assists if deaths == 0 else round((kills+assists)/deaths, 2)
    champion_name = player["championName"]
    damage_dealt = player["totalDamageDealtToChampions"]
    minions_killed = player["totalMinionsKilled"] + \
        player["neutralMinionsKilled"]
    game_duration_minutes = match_data["info"]["gameDuration"] / 60
    cs_per_min = round(minions_killed/game_duration_minutes, 2)
    bot_string = f'Burke {result_string} in a {kills}/{deaths}/{assists} ({kda} kda) performance as {champion_name}. He dealt {damage_dealt} damage to champions and averaged {cs_per_min} minions per minute\n'

    return bot_string
