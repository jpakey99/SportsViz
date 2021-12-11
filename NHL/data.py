import requests
import pandas as pd


def download_data():
    url = 'https://moneypuck.com/moneypuck/playerData/seasonSummary/2021/regular/teams.csv'
    r = requests.get(url, allow_redirects=True)
    open('moneypuck.csv', 'wb').write(r.content)

    url ='http://www.naturalstattrick.com/teamtable.php'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    df.to_csv('stattrick.csv')

    url = 'https://moneypuck.com/moneypuck/playerData/seasonSummary/2021/regular/skaters.csv'
    r = requests.get(url, allow_redirects=True)
    open('players.csv', 'wb').write(r.content)


def clean_data(situation='5on5', file='moneypuck.csv'):
    stats = open(file, 'r')
    team_list = []

    for line in stats:
        split_line = line.split(',')
        if split_line[5] == situation:
            team_list.append(split_line)

    return team_list


def clean_data_stattrick():
    stats = open('stattrick.csv', 'r')
    team_list = []
    stats.readline()
    for line in stats:
        split_line = line.split(',')
        team_list.append(split_line)

    return team_list


def get_list_values(value1:int, value2:int, team_list:list, per60=True):
    # values are integers that represent an index in the list
    teams, vl1, vl2, combined = [], [], [], []
    for team in team_list:
        if per60:
            ice = float(team[10]) / 60
            t, v1, v2 = team[0], (float(team[value1])/ice)*60, (float(team[value2])/ice)*60
        else:
            t = team[2].split(' ')[-1]
            v1 = float(team[value1])
            v2 = float(team[value2])
        teams.append(t)
        vl1.append(v1)
        vl2.append(v2)
        combined.append((t, v1, v2))
    return combined, teams, vl1, vl2


download_data()

# team_list = clean_data()
# print(get_list_values(60, 12,team_list)[0])