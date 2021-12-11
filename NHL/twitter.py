import datetime
from NHL.hockey_graphs import *
from NHL.individual_graphs import *
from NHL.nhl_logos import abbr
import requests


def create_viz():
    time = datetime.datetime.now()
    date = time.strftime("%m-%d-%Y")
    viz_list = [xTeamOverall,
                TeamOverall,
                GoalsFor,
                GoalsAgainst,
                xPythagGoals,
                PythagGoals,
                PythagGoalsCom,
                PowerPlay,
                PenaltyKill,
                PenaltysForxGoalsFor,
                # PenaltysForxGoalsAgainst
                PDO
                ]

    images  = ["NHL/graphs//xTeam_Tiers_" + date + ".png",
               "NHL/graphs//Team_Tiers_" + date + ".png",
               "NHL/graphs//Goals_For_" + date + ".png",
               "NHL/graphs//Goals_Against_" + date + ".png",
               "NHL/graphs//xpygoals_" + date + ".png",
               "NHL/graphs//pygoals_" + date + ".png",
               "NHL/graphs//pygoalscom_" + date + ".png",
               "NHL/graphs//powerplay_" + date + ".png",
               "NHL/graphs//penaltykill_" + date + ".png",
               "NHL/graphs//penaltiesxgf_" + date + ".png",
               # "NHL/graphs//penaltiesxga_" + date + ".png",
               "NHL/graphs//pdo_" + date + ".png",
               ]

    text = ["xGoals per 60 at 5 on 5.  Updated: " + date,
            "Goals per 60 at 5 on 5.  Updated: " + date,
            "Goals For per 60 at 5 on 5.  Updated: " + date,
            "Goals Against per 60 at 5 on 5.  Updated: " + date,
            "Pythagorean Win Percentage using xGoals.  Updated: " + date,
            "Pythagorean Win Percentage using actual Goals.  Updated: " + date,
            "Pythagorean Win Percentage using actual Goals vs Pythagorean Win Percentage using xGoals.  Updated: " + date,
            "Power play goals for and expected goals for.  Only 5 on 4 power plays.  Updated: " + date,
            "Penalty kills goals against and expected goals against.  Only 4 on 5 power plays.  Updated: " + date,
            "xGoals For vs Penalties drawn per 60.  Updated: " + date,
            # "xGoals Against vs Penalties drawn per 60  Updated: " + date,
            "PDO - Save % vs Shooting % All situations.  Updated: " + date
            ]

    for v in viz_list:
        print('hey')
        viz = v(date)
        viz.create_image()
        viz.save_image()

    return text, images


def get_teams_playing(date):
    url = 'https://statsapi.web.nhl.com/api/v1/schedule?date=' + date
    api_response = requests.get(url)
    response = api_response.json()
    teams = []
    for thing in response['dates'][0]['games']:
        # print(response['dates'][0][thing])
        away_team = thing['teams']['away']['team']['name'].split(' ')[-1]
        home_team = thing['teams']['home']['team']['name'].split(' ')[-1]
        teams.append(abbr[away_team])
        teams.append(abbr[home_team])
    return teams


def create_indiv_viz():
    time = datetime.datetime.now()
    date = time.strftime("%m-%d-%Y")
    y_d = time.strftime("%Y-%m-%d")

    team_data = nhl_data.clean_data(STAN, 'players.csv')
    players = get_list_values(XGF, XGA, team_data, 'ALL')
    ts = top_23_skaters(players)
    team_stats = depack_values(ts)
    xmin, xmax = min(team_stats[2]), max(team_stats[2])
    ymin, ymax = min(team_stats[3]), max(team_stats[3])

    viz_list = [
        xIndivOverall,
        # TeamGameScore
    ]

    teams = get_teams_playing(y_d)

    text, images = [], []

    for t in teams:
        text.append("Individual On-Ice xGoals 5on5 for " + t + ".  Updated: " + date,)
        images.append("NHL/graphs//xIndiv"+t+"_Tiers_" + date + ".png",)

        for v in viz_list:
            viz = v(date, t, xaxis=(xmin, xmax), yaxis=(ymin, ymax))
            viz.create_image()
            viz.save_image()

    return text, images

# http://www.naturalstattrick.com/teamtable.php#