import requests


abbr = {
    'Hurricanes': 'CAR',
    'Capitals': 'WSH',
    'Rangers': 'NYR',
    'Jackets': 'CBJ',
    'Flyers' : 'PHI',
    'Devils': 'NJD',
    'Islanders': 'NYI',
    'Penguins': 'PIT',
    'Panthers': 'FLA',
    'Sabres': 'BUF',
    'Wings': 'DET',
    'Lightning': 'TBL',
    'Leafs': 'TOR',
    'Bruins': 'BOS',
    'Senators': 'OTT',
    'Canadiens': 'MTL',
    'Blues' : 'STL',
    'Jets' : 'WPG',
    'Wild': 'MIN',
    'Predators': 'NSH',
    'Avalanche': 'COL',
    'Stars': 'DAL',
    'Blackhawks': 'CHI',
    'Coyotes': 'ARI',
    'Flames': 'CGY',
    'Oilers': 'EDM',
    'Sharks': 'SJS',
    'Ducks': 'ANA',
    'Knights': 'VGK',
    'Kings': 'LAK',
    'Kraken': 'SEA',
    'Canucks': 'VAN',
}


def pythag_record(goals_for, goals_against):
    return round((goals_for * goals_for) / ((goals_for * goals_for) + goals_against * goals_against), 2) * 100


def standings_call():
    standings = {}
    url = 'https://statsapi.web.nhl.com/api/v1/standings'
    api_response = requests.get(url)
    response = api_response.json()
    for thing in response['records']:
        for team in thing['teamRecords']:
            # print(response['dates'][0][thing])
            team_name, w_per, p_per = team['team']['name'], team['leagueRecord']['wins']/(team['leagueRecord']['losses']+team['leagueRecord']['ot']+ team['leagueRecord']['wins']), (2*team['leagueRecord']['wins'] + team['leagueRecord']['ot'])/(team['leagueRecord']['losses']+team['leagueRecord']['ot']+ team['leagueRecord']['wins'])
            ab_team = abbr[team_name.split(' ')[-1]]
            standings[ab_team] = {
                'w_per' : round(w_per, 2) * 100,
                'p_per' : round(p_per, 2) * 100
            }
    return standings


if __name__ == '__main__':
    standings_call()