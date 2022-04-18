import mlbgame
import pybaseball
import datetime
from pybaseball import batting_stats_bref, pitching_stats_bref, rosters, bwar_bat


import requests
# batting_stats = batting_stats_bref(2021)
# bstats = batting_stats.to_json()

date = datetime.date.today()
s_date = date.strftime('%Y%m%d')
print(s_date)
team_ids = [108,117,133,141,144,158,138,112,109,119,137,114,136,146,121,120,110,135,143,140,139,113,111,115,118,116,142,145,147]

for team_id in team_ids:
    x = requests.get('http://mlb.mlb.com/lookup/json/named.roster_40.bam?team_id={0}'.format(team_id))
    r = x.json()
    f = open('rosters/'+str(team_id)+'_roster_'+ s_date+'.csv','w')
    f.write("id,name,position,games_played,WAR\n")
    for p in r['roster_40']['queryResults']['row']:
        player_id = p['player_id']
        position = p['primary_position']
        name = p['name_display_first_last']
        team = p['team_abbrev']
        # f.write('{},{},{},{},{}\n'.format(player_id, name, position, 0, 0))
        # print(player_id, name, position)


