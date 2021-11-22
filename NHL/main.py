import requests


def add_player_to_dict(p_dict, player_name, draft_team, pick_num, player_id):
    p_dict[player_name] = {
        'prospect_id': player_id,
        'draft_team': draft_team,
        'pick_num': pick_num,
        'position': None,
        'height': None,
        'weight': None,
        'day_age': 0,
        'handiness': None,
        'position_type': None,
        'nhl_game': -1
    }

def main():
    draft_url = 'https://statsapi.web.nhl.com/api/v1/draft/'
    p_url = 'https://statsapi.web.nhl.com/api/v1/people/8471675/?stats=careerRegularSeason'

    year = 2005
    players = {}
    while year <= 2015:
        url = draft_url + str(year)
        api_response = requests.get(url)
        response = api_response.json()
        year += 1
        # loop over rounds
        for round in response['drafts'][0]['rounds']:
            # loop over picks
            for pick in round['picks']:
                # save prospect_name, draft_team, pick_num
                name = pick['prospect']['fullName']
                draft_team = pick['team']['id']
                pick_num = pick['pickOverall']
                if 'id' in pick['prospect']:
                    id = pick['prospect']['id']
                else:
                    id = None
                add_player_to_dict(players, name, draft_team, pick_num, id)
    print(players)

    prospect_url = 'https://statsapi.web.nhl.com/api/v1/draft/prospects/'

    for player in players.keys():
        if players[player]['prospect_id'] is not None:
            url = prospect_url + str(players[player]['prospect_id'])
            api_response = requests.get(url)
            response = api_response.json()
            print(response)
        else:
            # delete player from dict
            pass


def schedule():
    url = 'https://statsapi.web.nhl.com/api/v1/schedule?date=2021-03-05'
    api_response = requests.get(url)
    response = api_response.json()
    print(response)
    for thing in response['dates'][0]['games']:
        # print(response['dates'][0][thing])
        print(thing)
    # 201702065
    # url = 'https://statsapi.web.nhl.com/api/v1/game/2020020017/boxscore'
    # api_response = requests.get(url)
    # response = api_response.json()
    # for thing in response:
        # print(thing)
    # print(response)



# schedule()