yellow, red, brown, blue, green, purple, orange, black = (1,1,0), (1,0,0), (.545,.27,.074), (0,0,1), (0,1,0), (1,0,1), (1,.55,0), (0,0,0)



logos = {
    'BUF': 'logos/bills.png',
    'NYJ': 'logos/jets.png',
    'LV': 'logos/raiders.png',
    'DEN': 'logos/broncos.png',
    'ATL': 'logos/falcons.png',
    'GB': 'logos/packers.png',
    'CHI': 'logos/bears.png',
    'HOU': 'logos/texans.png',
    'ARI': 'logos/cardinals.png',
    'NO': 'logos/saints.png',
    'LAC': 'logos/chargers.png',
    'CLE': 'logos/browns.png',
    'SEA': 'logos/seahawks.png',
    'MIA': 'logos/dolphins.png',
    'IND': 'logos/colts.png',
    'KC': 'logos/chiefs.png',
    'WAS': 'logos/football_team.png',
    'BAL': 'logos/ravens.png',
    'JAX': 'logos/jaguars.png',
    'PHI': 'logos/eagles.png',
    'PIT': 'logos/steelers.png',
    'LA': 'logos/rams.png',
    'CAR': 'logos/panthers.png',
    'CIN': 'logos/bengals.png',
    'TB': 'logos/buccaneers.png',
    'SF': 'logos/49ers.png',
    'NE': 'logos/patriots.png',
    'DET': 'logos/lions.png',
    'MIN': 'logos/vikings.png',
    'DAL': 'logos/cowboys.png',
    'NYG': 'logos/giants.png',
    'TEN': 'logos/titians.png'
}

def get_labels(data):
    labels = []
    for line in data:
        labels.append(logos[line])
    return labels