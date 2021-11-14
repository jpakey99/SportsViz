logos = {
    'NYR': 'nhl/NYR.png',
    'NYI': 'nhl/NYI.png',
    'CGY': 'nhl/CGY.png',
    'VAN': 'nhl/VAN.png',
    'LAK': 'nhl/LAK.png',
    'VGK': 'nhl/VGK.png',
    'STL': 'nhl/STL.png',
    'ARI': 'nhl/ARI.png',
    'SJS': 'nhl/SJS.png',
    'PHI': 'nhl/PHI.png',
    'OTT': 'nhl/OTT.png',
    'MIN': 'nhl/MIN.png',
    'WPG': 'nhl/WPG.png',
    'CBJ': 'nhl/CBJ.png',
    'NJD': 'nhl/NJD.png',
    'PIT': 'nhl/PIT.png',
    'COL': 'nhl/COL.png',
    'WSH': 'nhl/WSH.png',
    'NSH': 'nhl/NSH.png',
    'TBL': 'nhl/TBL.png',
    'BOS': 'nhl/BOS.png',
    'CHI': 'nhl/CHI.png',
    'ANA': 'nhl/ANA.png',
    'BUF': 'nhl/BUF.png',
    'MTL': 'nhl/MTL.png',
    'SEA': 'nhl/SEA.png',
    'DET': 'nhl/DET.png',
    'FLA': 'nhl/FLA.png',
    'DAL': 'nhl/DAL.png',
    'EDM': 'nhl/EDM.png',
    'TOR': 'nhl/TOR.png',
    'CAR': 'nhl/CAR.png'
}

def logo_search(teams):
    logo = []
    for team in teams:
        # print(team)
        logo.append(logos[team])
    return logo