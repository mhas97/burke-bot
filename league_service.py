import match_v5_service
import league_response_helper


def get_latest_match_bot_string():
    latest_match_id = match_v5_service.get_latest_match_id()
    if latest_match_id is None:
        return None

    latest_match_data = match_v5_service.get_match_data_by_id(latest_match_id)
    if latest_match_data is None:
        return None

    response = league_response_helper.get_bot_string_from_match_data(
        latest_match_data)

    return response
