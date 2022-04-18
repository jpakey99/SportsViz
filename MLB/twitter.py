from MLB.main import run_team_graphs
import datetime


def create_viz():
    run_team_graphs(2022)
    dateo = datetime.date.today()
    string_date = dateo.strftime("%m-%d-%Y")
    image_names = [
        "MLB/graphs/Team_Tiers_" + string_date + ".png",
        "MLB/graphs/RAvRF_" + string_date + ".png",
        "MLB/graphs/xRAvXRF_" + string_date + ".png",
        "MLB/graphs/Run_Diff_" + string_date + ".png",
        "MLB/graphs/xwOBA_Overall_" + string_date + ".png",
        "MLB/graphs/wOBA_Overall_" + string_date + ".png",
        "MLB/graphs/wOBA_Batting_" + string_date + ".png",
        "MLB/graphs/wOBA_Pitching_" + string_date + ".png",
        "MLB/graphs/fielding_" + string_date + ".png",
    ]

    text = [
        "Team Tiers defined by xFIP- (y-axis) vs WRC+ (x-axis).  Last updated " + string_date,
        "Runs against vs Runs for plotted on a 2d graph.  Last updated " + string_date,
        "Expected Runs Against vs Expected Runs For plotted on a 2d graph.  Last updated " + string_date,
        "Team Run Differential.  Last updated " + string_date,
        "Team Tiers defined by Expected Weighted On-base Average for batting (x-axis) and pitching (y-axis).  Last updated " + string_date,
        "Team Tiers defined by Weighted On-base Average for batting (x-axis) and pitching (y-axis).  Last updated " + string_date,
        "Offensive production by team.  Expected Weighted On-base Average (x-axis) and Weighted On-base Average (y-axis).  Last updated " + string_date,
        "Pitching production by team.  Expected Weighted On-base Average (x-axis) and Weighted On-base Average (y-axis).  Last updated " + string_date,
        "Fielding production by team.  Last updated " + string_date,
    ]

    return text, image_names

# create_viz()