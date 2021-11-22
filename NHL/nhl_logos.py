logos = {
    'NYR': 'NHL/nhl/NYR.png',
    'NYI': 'NHL/nhl/NYI.png',
    'CGY': 'NHL/nhl/CGY.png',
    'VAN': 'NHL/nhl/VAN.png',
    'LAK': 'NHL/nhl/LAK.png',
    'VGK': 'NHL/nhl/VGK.png',
    'STL': 'NHL/nhl/STL.png',
    'ARI': 'NHL/nhl/ARI.png',
    'SJS': 'NHL/nhl/SJS.png',
    'PHI': 'NHL/nhl/PHI.png',
    'OTT': 'NHL/nhl/OTT.png',
    'MIN': 'NHL/nhl/MIN.png',
    'WPG': 'NHL/nhl/WPG.png',
    'CBJ': 'NHL/nhl/CBJ.png',
    'NJD': 'NHL/nhl/NJD.png',
    'PIT': 'NHL/nhl/PIT.png',
    'COL': 'NHL/nhl/COL.png',
    'WSH': 'NHL/nhl/WSH.png',
    'NSH': 'NHL/nhl/NSH.png',
    'TBL': 'NHL/nhl/TBL.png',
    'BOS': 'NHL/nhl/BOS.png',
    'CHI': 'NHL/nhl/CHI.png',
    'ANA': 'NHL/nhl/ANA.png',
    'BUF': 'NHL/nhl/BUF.png',
    'MTL': 'NHL/nhl/MTL.png',
    'SEA': 'NHL/nhl/SEA.png',
    'DET': 'NHL/nhl/DET.png',
    'FLA': 'NHL/nhl/FLA.png',
    'DAL': 'NHL/nhl/DAL.png',
    'EDM': 'NHL/nhl/EDM.png',
    'TOR': 'NHL/nhl/TOR.png',
    'CAR': 'NHL/nhl/CAR.png'
}

logos_name = {
    'Rangers': 'NHL/nhl/NYR.png',
    'Islanders': 'NHL/nhl/NYI.png',
    'Flames': 'NHL/nhl/CGY.png',
    'Canucks': 'NHL/nhl/VAN.png',
    'Kings': 'NHL/nhl/LAK.png',
    'Knights': 'NHL/nhl/VGK.png',
    'Blues': 'NHL/nhl/STL.png',
    'Coyotes': 'NHL/nhl/ARI.png',
    'Sharks': 'NHL/nhl/SJS.png',
    'Flyers': 'NHL/nhl/PHI.png',
    'Senators': 'NHL/nhl/OTT.png',
    'Wild': 'NHL/nhl/MIN.png',
    'Jets': 'NHL/nhl/WPG.png',
    'Jackets': 'NHL/nhl/CBJ.png',
    'Devils': 'NHL/nhl/NJD.png',
    'Penguins': 'NHL/nhl/PIT.png',
    'Avalanche': 'NHL/nhl/COL.png',
    'Capitals': 'NHL/nhl/WSH.png',
    'Predators': 'NHL/nhl/NSH.png',
    'Lightning': 'NHL/nhl/TBL.png',
    'Bruins': 'NHL/nhl/BOS.png',
    'Blackhawks': 'NHL/nhl/CHI.png',
    'Ducks': 'NHL/nhl/ANA.png',
    'Sabres': 'NHL/nhl/BUF.png',
    'Canadiens': 'NHL/nhl/MTL.png',
    'Kraken': 'NHL/nhl/SEA.png',
    'Wings': 'NHL/nhl/DET.png',
    'Panthers': 'NHL/nhl/FLA.png',
    'Stars': 'NHL/nhl/DAL.png',
    'Oilers': 'NHL/nhl/EDM.png',
    'Leafs': 'NHL/nhl/TOR.png',
    'Hurricanes': 'NHL/nhl/CAR.png'
}

abbr ={
    'Rangers': 'NYR',
    'Islanders': 'NYI',
    'Flames': 'CGY',
    'Canucks': 'VAN',
    'Kings': 'LAK',
    'Knights': 'VGK',
    'Blues': 'STL',
    'Coyotes': 'ARI',
    'Sharks': 'SJS',
    'Flyers': 'PHI',
    'Senators': 'OTT',
    'Wild': 'MIN',
    'Jets': 'WPG',
    'Jackets': 'CBJ',
    'Devils': 'NJD',
    'Penguins': 'PIT',
    'Avalanche': 'COL',
    'Capitals': 'WSH',
    'Predators': 'NSH',
    'Lightning': 'TBL',
    'Bruins': 'BOS',
    'Blackhawks': 'CHI',
    'Ducks': 'ANA',
    'Sabres': 'BUF',
    'Canadiens': 'MTL',
    'Kraken': 'SEA',
    'Wings': 'DET',
    'Panthers': 'FLA',
    'Stars': 'DAL',
    'Oilers': 'EDM',
    'Leafs': 'TOR',
    'Hurricanes': 'CAR'
}

def logo_search(teams):
    logo = []
    for team in teams:
        # print(team)
        logo.append(logos[team])
    return logo


def logo_search_name(teams):
    logo = []
    for team in teams:
        # print(team)
        logo.append(logos_name[team])
    return logo