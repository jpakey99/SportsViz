import pandas as pd
import  requests


def draft_data(year):
    url = 'https://www.pro-football-reference.com/years/'+year+'/draft.htm'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[0]
    df.to_csv('nfltest.csv')


def season_data(year):
    data = pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/' \
                       'play_by_play_' + str(year) + '.csv.gz?raw=True',
                       compression='gzip', low_memory=False)
    return data


def get_data(data):
    team_dict = {}
    home_team, away_team, home_epa, away_epa = '', '', 0, 0
    home_score, away_score = 0, 0
    correct, total = 0, 0
    for line in range(len(data)):
        if home_team == '':
            home_team = data['home_team'][line]
            away_team = data['away_team'][line]
        elif home_team != data['home_team'][line] and away_team != data['away_team'][line]:
            if home_team in team_dict:
                if (home_score - away_score) > 0 and (team_dict[home_team]['offense'] + team_dict[away_team]['defense'] - team_dict[away_team]['offense'] + team_dict[home_team]['defense']) > 0:
                    correct += 1
                if (home_score - away_score) < 0 and (team_dict[home_team]['offense'] + team_dict[away_team]['defense'] - team_dict[away_team]['offense'] + team_dict[home_team]['defense']) < 0:
                    correct += 1
                total += 1
                team_dict[home_team]['offense'] += home_epa
                team_dict[home_team]['defense'] += away_epa
                team_dict[home_team]['games'] += 1
                team_dict[away_team]['offense'] += away_epa
                team_dict[away_team]['defense'] += home_epa
                team_dict[away_team]['games'] += 1
            else:
                team_dict[home_team] = {
                    'offense': home_epa,
                    'defense': away_epa,
                    'games': 1
                }
                team_dict[away_team] = {
                    'offense': away_epa,
                    'defense': home_epa,
                    'games': 1
                }

            # print(home_team, away_team, home_score-away_score, home_epa-away_epa)
            home_team = data['home_team'][line]
            away_team = data['away_team'][line]
            home_epa, away_epa = 0, 0
        else:
            home_epa, away_epa = round(float(data['total_home_epa'][line]), 2), round(float(data['total_away_epa'][line]), 2)
            if data['total_home_score'][line] != '' or  data['total_away_score'][line] != '':
                # print('h')
                home_score, away_score = int(data['total_home_score'][line]), int(data['total_away_score'][line])
    print(correct, total, correct/total)
    print(team_dict)
    return team_dict


def prediction(team_data):
    file = open('schedule.csv')
    predictions = []
    for line in file:
        stripline = line.strip('\n')
        splitline = stripline.split(',')
        home_team = splitline[1]
        away_team = splitline[0]
        # print()
        home_epa_o = team_data[home_team]['offense'] / team_data[home_team]['games']
        home_epa_d = team_data[home_team]['defense'] / team_data[home_team]['games']
        away_epa_o = team_data[away_team]['offense'] / team_data[away_team]['games']
        away_epa_d = team_data[away_team]['defense'] / team_data[away_team]['games']
        pred = (home_epa_o + away_epa_d) - (away_epa_o  + home_epa_d )
        if pred > 0:
            predictions.append((home_team, away_team, home_team))
        else:
            predictions.append((home_team, away_team, away_team))
    return predictions


if __name__ == '__main__':
    tesm_data = get_data(season_data(2021))
    prediction(tesm_data)