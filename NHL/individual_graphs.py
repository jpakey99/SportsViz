from NHL.anstract_hockey_graph import TeamScatterGraph
from Graph import Graph2DScatter
from NHL.nhl_logos import *
import NHL.data as nhl_data
from NHL.hockey_graphs import HockeyGraph

GA, XGA, GF, XGF = 123, 115, 93, 85
ICE, NAME, TEAM, GAME_SCORE = 7, 2, 3, 9
STAN, PP, PK, OTHER, ALL = '5on5', '5on4', '4on5', 'other', 'all'


def top_23_skaters(players: list):
    if len(players) <= 23:
        return players
    else:
        # print('Players ', players)
        top_players = [0] * 23
        p = 0
        for player in range(len(players)):
            found = False
            current_lowest_index, current_lowest_value = -1, 0
            for space in top_players:
                # print('SPACE', top_players)
                if not found:
                    if space == 0:
                        found = True
                        top_players[top_players.index(space)] = players[player]
                        p += 1
                    elif current_lowest_value < players[player][-1]:
                        current_lowest_index = players.index(players[player])
                        current_lowest_value = players[player][-1]
            if not found:
                if p <= 22:
                    top_players[current_lowest_index] = players[player]
                    p += 1
        return top_players


def get_list_values(value1:int, value2:int, team_list:list, team='ALL', per60=True):
    # values are integers that represent an index in the list
    teams, vl1, vl2, combined, names = [], [], [], [], []
    for player in team_list:
        if team == player[TEAM] or team == 'ALL':
            ice_time = float(player[ICE])
            if per60:
                ice = ice_time / 60
                t, v1, v2 = player[TEAM], (float(player[value1])/ice)*60, (float(player[value2])/ice)*60
                n = player[NAME]
            else:
                t = player[TEAM].split(' ')[-1]
                v1 = float(player[value1])
                v2 = float(player[value2])
                n = player[NAME]
            names.append(n)
            teams.append(t)
            vl1.append(v1)
            vl2.append(v2)
            combined.append((t, v1, v2, n, ice_time))
    return combined


def depack_values(players):
    teams, vl1, vl2, names = [], [], [], []
    for player in players:
        teams.append(player[0])
        vl1.append(player[1])
        vl2.append(player[2])
        names.append(player[3])
    return [], teams,vl1, vl2, names


class xIndivOverall(HockeyGraph):
    def __init__(self, date: str, team, xaxis, yaxis):
        print(team, xaxis, yaxis)
        team_data = nhl_data.clean_data(STAN, 'players.csv')
        players = get_list_values(XGF, XGA, team_data, team)
        ts = top_23_skaters(players)
        team_stats = depack_values(ts)
        # print(team_stats)
        title = 'xGoals 5v5 Individual: ' + team
        super().__init__(team_stats, date, title=title)
        self.axis_labels =  ('xGoalsFor/60', 'xGoalsAgainst/60')
        self.team = team
        self.logos = logo_search(team_stats[1])
        # , xaxis = xaxis, yaxis = yaxis
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=True, diag_lines=False, dot_labels=team_stats[4], xaxis = xaxis, yaxis = yaxis)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('NHL/graphs/' + 'xIndiv'+self.team+'_Tiers' + '_' + self.date + '.png')


class TeamGameScore(HockeyGraph):
    def __init__(self, date: str, team):
        title = 'xGoals 5v5 Individual: ' + team
        self.team = team
        team_data = nhl_data.clean_data(ALL, 'players.csv')
        self.team_stats = get_list_values(GAME_SCORE, ICE, team_data, team, per60=False)
        super().__init__(self.team_stats, date, title)

    def create_image(self):
        x, y, c_x, size, spacing_x, spacing_y = 800, 20, 800, 70, 500, 10
        self.title_placement()
        logo = logos[self.team]
        print(self.team_stats)
        for i in range(0, len(self.team_stats[-1])):
            color = (255,0,0,255)
            self.draw.rectangle((c_x, y, c_x+size, y+size), fill=color)
            print(self.team_stats[2][i])
            self.draw.text((c_x, y, c_x+size, y+size), text=str(self.team_stats[2][i]), fill=(0, 0, 0, 255), font=self.sub_title_font)
            self.draw.text((c_x + size + 10, y, c_x + size, y + size), text=str(self.team_stats[4][i]), fill=(0, 0, 0, 255), font=self.sub_title_font)
            if (c_x + size + spacing_x) >= (self.width - size * 2):
                y += size + spacing_y
                c_x = x
            else:
                c_x += size + spacing_x

    def save_image(self):
        self.image.save('NHL/graphs/' + 'ScoreCard_'+self.team+'_Tiers' + '_' + self.date + '.png')

    def sort_by_ice(self):
        for i in range(0, len(self.team_stats[-1])):
            for j in range(1, len(self.team_stats[-1])):
                # if self.team_stats[2][i] >:
                pass