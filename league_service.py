'''Handles any league of legends related bot calls and returns errors'''
import match_v5_service
import league_response_helper


def get_latest_match_bot_string():
    '''Fetches match data for the latest match and returns a formatted bot-string for output'''
    latest_match_id = match_v5_service.get_match_ids(num_matches=1)
    if latest_match_id is None:
        return "Error fetching matches"

    if len(latest_match_id) < 0:
        return "No recent matches found"

    latest_match_id = latest_match_id[0]
    latest_match_data = match_v5_service.get_match_data_by_id(latest_match_id)
    if latest_match_data is None:
        return f"Error fetching match data for match id {latest_match_id}"

    response = league_response_helper.get_bot_string_from_match_data(
        latest_match_data)
    if response is None:
        return f"Error generating response for match id {latest_match_id}"

    return response
