from anstract_hockey_graph import TeamScatterGraph
from Graph import BarGraph, Graph2DScatter
from nhl_logos import logo_search
from test import get_list_values, clean_data
from statistics import stdev
import standings

GA, XGA, GF, XGF = 73, 60, 25, 12
STAN, PP, PK, OTHER, ALL = '5on5', '5on4', '4on5', 'other', 'all'


class HockeyGraph(TeamScatterGraph):
    def __init__(self, team_stats, date: str, title, credits='Twitter: @GraphingSports, Idea: @ChartingHockey\n data: MoneyPuck',
                 subtitle='', corner_labels=('good', 'dull', 'fun', 'bad')):
        if subtitle == '':
            subtitle = 'Updated: ' + date
        super().__init__(team_stats, date, title, credits, subtitle, corner_labels)


class xTeamOverall(HockeyGraph):
    def __init__(self, date: str):
        team_data = clean_data(STAN)
        team_stats = get_list_values(XGF, XGA, team_data)
        title = 'xGoals 5v5'
        super().__init__(team_stats, date, title=title)
        self.axis_labels =  ('xGoalsFor/60', 'xGoalsAgainst/60')
        self.logos = logo_search(team_stats[1])
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=True, diag_lines=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'xTeam_Tiers' + '_' + self.date + '.png')


class TeamOverall(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data()
        team_stats = get_list_values(GF, GA, team_data)
        title = 'Goals 5v5'
        super().__init__(team_stats, date, title=title)
        self.axis_labels =  ('GoalsFor/60', 'GoalsAgainst/60')
        self.logos = logo_search(team_stats[1])
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=True, diag_lines=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'Team_Tiers' + '_' + self.date + '.png')


class GoalsFor(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data()
        team_stats = get_list_values(XGF, GF, team_data)
        subtitle = 'Updated: ' + date
        title = 'Goals For 5v5'
        credits = 'Twitter: @GraphingSports, Idea: @ChartingHockey\n data: MoneyPuck'  #Fine tone centering 2nd line
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, subtitle=subtitle, credits=credits, corner_labels=corner_labels)
        self.axis_labels =  ('xGoalsFor/60', 'GoalsFor/60')
        self.logos = logo_search(team_stats[1])
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=False, diag_lines=False)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'Goals_For' + '_' + self.date + '.png')


class GoalsAgainst(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data()
        team_stats = get_list_values(XGA, GA, team_data)
        title = 'Goals Against 5v5'
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, corner_labels=corner_labels)
        self.axis_labels =  ('xGoalsAgainst/60', 'GoalsAgainst/60')
        self.logos = logo_search(team_stats[1])
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=True, diag_lines=False, invertx=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'Goals_Against' + '_' + self.date + '.png')


class PythagGoals(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data(ALL)
        goal_data = get_list_values(GF, GA, team_data)
        team_standings = standings.standings_call()
        team_stats, x, y= [], [], []
        for team in goal_data[0]:
            x_wper = standings.pythag_record(team[1], team[2])
            t = team[0]
            wper = team_standings[t]['w_per']
            team_stats.append((t, x_wper, wper))
            x.append(x_wper)
            y.append(wper)

        subtitle = 'Using Actual Goals for and against\n' + 'Updated: ' + date
        title = 'Pythagorean Win Percentage'
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, subtitle=subtitle, corner_labels=corner_labels)
        self.axis_labels =  ('expected winning percentage', 'actual winning percentage')
        self.logos = logo_search(goal_data[1])
        self.graph = Graph2DScatter(x, y, self.logos, self.axis_labels ,inverty=False, diag_lines=False, invertx=False, best_fit=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'pygoals' + '_' + self.date + '.png')


class xPythagGoals(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data(ALL)
        goal_data = get_list_values(XGF, XGA, team_data)
        team_stats, x, y= [], [], []
        team_standings = standings.standings_call()
        for team in goal_data[0]:
            x_wper = standings.pythag_record(team[1], team[2])
            t = team[0]
            wper = team_standings[t]['w_per']
            team_stats.append((t, x_wper, wper))
            x.append(x_wper)
            y.append(wper)

        subtitle = 'Using Expected Goals for and against\n' + 'Updated: ' + date
        title = 'Pythagorean Win Percentage'
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, subtitle=subtitle, corner_labels=corner_labels)
        self.axis_labels =  ('expected winning percentage', 'actual winning percentage')
        self.logos = logo_search(goal_data[1])
        self.graph = Graph2DScatter(x, y, self.logos, self.axis_labels ,inverty=False, diag_lines=False, invertx=False, best_fit=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'xpygoals' + '_' + self.date + '.png')


class PythagGoalsCom(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data(ALL)
        goal_data = get_list_values(XGF, XGA, team_data)
        team_stats, x, y = [], [], []
        act_goals = get_list_values(GF, GA, team_data)
        for team in goal_data[0]:
            for a_team in act_goals[0]:
                if team[0] == a_team[0]:
                    x_wper = standings.pythag_record(team[1], team[2])
                    wper = standings.pythag_record(a_team[1], a_team[2])
                    t = team[0]
                    team_stats.append((t, x_wper, wper))
                    x.append(x_wper)
                    y.append(wper)
        subtitle = 'Using Expected Goals and Actual Goals\n' + 'Updated: ' + date
        title = 'Pythagorean Win Percentage'
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, subtitle=subtitle, corner_labels=corner_labels)
        self.axis_labels =  ('Pythagorean Win Percentage using xGoals', 'Pythagorean Win Percentage using actual goals')
        self.logos = logo_search(goal_data[1])
        self.graph = Graph2DScatter(x, y, self.logos, self.axis_labels ,inverty=False, diag_lines=False, invertx=False, best_fit=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'pygoalscom' + '_' + self.date + '.png')


class PowerPlay(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data(PP)
        team_stats = get_list_values(XGF, GF, team_data)
        subtitle = 'Updated: ' + date
        title = 'Power Play (5v4) Goals For'
        credits = 'Twitter: @GraphingSports, Idea: @ChartingHockey\n data: MoneyPuck'  #Fine tone centering 2nd line
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, subtitle=subtitle, credits=credits, corner_labels=corner_labels)
        self.axis_labels =  ('xGoalsFor/60', 'GoalsFor/60')
        self.logos = logo_search(team_stats[1])
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=False, diag_lines=False)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'powerplay' + '_' + self.date + '.png')


class PenaltyKill(HockeyGraph):

    def __init__(self, date: str):
        team_data = clean_data(PK)
        team_stats = get_list_values(XGA, GA, team_data)
        title = 'Penalty Kill (4v5) Goals Against'
        corner_labels = ('good', 'lucky', 'unlucky', 'bad')
        super().__init__(team_stats, date, title=title, corner_labels=corner_labels)
        self.axis_labels =  ('xGoalsAgainst/60', 'GoalsAgainst/60')
        self.logos = logo_search(team_stats[1])
        self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=True, diag_lines=False, invertx=True)
        self.graph_size = (0, 0)

    def save_image(self):
        self.image.save('graphs/' + 'penaltykill' + '_' + self.date + '.png')


if __name__ == '__main__':
    g = TeamOverall('10-29-2021')
    g.create_image()
    g.save_image()