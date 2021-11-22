# epa - offense/defense and pass/rush
# points - offense/defense
# penalties - offense/defense
# series conversion - conversion/attempts on 1st, 2nd, 3rd, and 4th down
# total plays offense/defense
# plays/drive

# home_team
# away_team
# posteam - 9
# defteam - 10
# week - 7
# drive -20
# play_type - 29
# total_home_score - 56
# total_away_score - 57
# total_home_epa - 76
# total_away_epa - 76
# total_home_rush - 77
# total_away_rush - 78
# total_home_pass - 79
# total_away_pass - 80
# drive_play_count - 308
# penalty_team - 274

import nfl_data

def initialize_team(t_dict, team):
    t_dict[team] = {
        'epa_o_total' : 0,
        'epa_o_rush' : 0,
        'epa_o_pass': 0,
        'epa_d_total': 0,
        'epa_d_rush': 0,
        'epa_d_pass': 0,
        'points_o' : 0,
        'points_d': 0,
        'penalties_o_taken': 0,
        'penalties_d_taken': 0,
        'penalties_d_drawn': 0,
        'penalties_o_drawn': 0,
        'drives' : {
            'total_o_drives' : 0,
            'total_o_plays' : 0,
            'total_d_drives': 0,
            'total_d_plays': 0,
        },
        'conversions' : {
            'first_down':{
                'attempts': 0,
                'success': 0,
            },
            'second_down': {
                'attempts': 0,
                'success': 0,
            },
            'third_down': {
                'attempts': 0,
                'success': 0,
            },
            'forth_down': {
                'attempts': 0,
                'success': 0,
            }
        }

    }


def update_team(team_dict, team, home_epa_total, home_epa_passing, home_epa_rushing, away_epa_total, away_epa_passing, away_epa_rushing,
                home_offensive_plays, away_offensive_plays, home_score, away_score, home_drives, away_drives, home_offensive_penalties,
                home_defensive_penalties, away_offensive_penalties, away_defensive_penalties, first_down_attempts, first_down_success,
                second_down_attempts, second_down_success, third_down_attempts, third_down_success, forth_down_attempts, forth_down_success):
    team_dict[team]['epa_o_total'] += home_epa_total
    team_dict[team]['epa_o_rush'] += home_epa_rushing
    team_dict[team]['epa_o_pass'] += home_epa_passing
    team_dict[team]['epa_d_total'] += away_epa_total
    team_dict[team]['epa_d_rush'] += away_epa_rushing
    team_dict[team]['epa_d_pass'] += away_epa_passing
    team_dict[team]['points_o'] += home_score
    team_dict[team]['points_d'] += away_score
    team_dict[team]['penalties_o_taken'] += home_offensive_penalties
    team_dict[team]['penalties_d_taken'] += home_defensive_penalties
    team_dict[team]['penalties_d_drawn'] += away_offensive_penalties
    team_dict[team]['penalties_o_drawn'] += away_defensive_penalties
    team_dict[team]['drives']['total_o_drives'] += home_drives
    team_dict[team]['drives']['total_d_drives'] += away_drives
    team_dict[team]['drives']['total_o_plays'] += home_offensive_plays
    team_dict[team]['drives']['total_d_plays'] += away_offensive_plays
    team_dict[team]['conversions']['first_down']['attempts'] += first_down_attempts
    team_dict[team]['conversions']['first_down']['success'] += first_down_success
    team_dict[team]['conversions']['second_down']['attempts'] += second_down_attempts
    team_dict[team]['conversions']['second_down']['success'] += second_down_success
    team_dict[team]['conversions']['third_down']['attempts'] += third_down_attempts
    team_dict[team]['conversions']['third_down']['success'] += third_down_success
    team_dict[team]['conversions']['forth_down']['attempts'] += forth_down_attempts
    team_dict[team]['conversions']['forth_down']['success'] += forth_down_success



def get_data(data):
    team_dict = {}
    home_team, away_team = '', ''
    home_epa_total, home_epa_passing, home_epa_rushing = 0, 0, 0
    away_epa_total, away_epa_passing, away_epa_rushing = 0, 0, 0
    home_offensive_plays, away_offensive_plays = 0, 0
    home_score, away_score = 0, 0
    drive_number, home_drives, away_drives = 0, 0, 0
    home_offensive_penalties, home_defensive_penalties, away_offensive_penalties, away_defensive_penalties = 0,0,0,0
    home_first_d_a, home_first_down_s, home_second_d_a, home_second_d_s, home_third_d_a, home_third_down_s, home_forth_d_a, home_forth_d_s = 0, 0, 0, 0, 0, 0, 0, 0
    away_first_d_a, away_first_down_s, away_second_d_a, away_second_d_s, away_third_d_a, away_third_down_s, away_forth_d_a, away_forth_d_s = 0, 0, 0, 0, 0, 0, 0, 0
    for line in range(len(data)):
        if home_team == '':
            home_team = data['home_team'][line]
            away_team = data['away_team'][line]
        elif home_team != data['home_team'][line] and away_team != data['away_team'][line]:
            if home_team in team_dict:
                update_team(team_dict, home_team, home_epa_total, home_epa_passing, home_epa_rushing, away_epa_total, away_epa_passing, away_epa_rushing,
                            home_offensive_plays, away_offensive_plays, home_score, away_score, home_drives, away_drives, home_offensive_penalties,
                            home_defensive_penalties, away_offensive_penalties, away_defensive_penalties, home_first_d_a, home_first_down_s,
                            home_second_d_a, home_second_d_s, home_third_d_a, home_third_down_s, home_forth_d_a, home_forth_d_s)
                update_team(team_dict, away_team, away_epa_total, away_epa_passing, away_epa_rushing, home_epa_total, home_epa_passing, home_epa_rushing,
                            away_offensive_plays, home_offensive_plays, away_score, home_score, away_drives, home_drives, away_offensive_penalties,
                            away_defensive_penalties, home_offensive_penalties, home_defensive_penalties, away_first_d_a, away_first_down_s,
                            away_second_d_a, away_second_d_s, away_third_d_a, away_third_down_s, away_forth_d_a, away_forth_d_s)
            else:
                initialize_team(team_dict, home_team)
                initialize_team(team_dict, away_team)

            # print(home_team, away_team, home_score-away_score, home_epa-away_epa)
            home_team = data['home_team'][line]
            away_team = data['away_team'][line]
            home_epa_total, home_epa_passing, home_epa_rushing = 0, 0, 0
            away_epa_total, away_epa_passing, away_epa_rushing = 0, 0, 0
            home_offensive_plays, away_offensive_plays = 0, 0
            home_score, away_score = 0, 0
            drive_number, home_drives, away_drives = 0, 0, 0
            home_offensive_penalties, home_defensive_penalties, away_offensive_penalties, away_defensive_penalties = 0, 0, 0, 0
        else:
            if drive_number == data['drive'][line]:
                pass
            else:
                if home_team == data['posteam'][line]:
                    home_drives += 1
                    home_offensive_plays = data['drive_play_count'][line]
                else:
                    away_drives += 1
                    away_offensive_plays = data['drive_play_count'][line]
                drive_number = data['drive'][line]
            if data['penalty_team'][line] == home_team:
                if home_team == data['posteam'][line]:
                    home_offensive_penalties += 1
                else:
                    home_defensive_penalties += 1
            else:
                if away_team == data['posteam'][line]:
                    away_offensive_penalties += 1
                else:
                    away_defensive_penalties += 1
            home_epa_total = data['total_home_epa'][line]
            home_epa_passing = data['total_home_pass_epa'][line]
            home_epa_rushing = data['total_home_rush_epa'][line]
            away_epa_total = data['total_away_epa'][line]
            away_epa_passing = data['total_away_pass_epa'][line]
            away_epa_rushing = data['total_away_rush_epa'][line]
            home_score = data['total_home_score'][line]
            away_score = data['total_away_score'][line]

    print(team_dict)
    return team_dict


get_data(nfl_data.season_data(2021))