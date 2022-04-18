yellow, red, brown, blue, green, purple, orange, black = (1,1,0), (1,0,0), (.545,.27,.074), (0,0,1), (0,1,0), (1,0,1), (1,.55,0), (0,0,0)


class MLBLabel:
    def __init__(self):
        self.logos = {
            'mlb': 'MLB/logos/_MLB_logo.png',
            'LAA': 'MLB/logos/angels.png',
            'HOU': 'MLB/logos/astros.png',
            'OAK': 'MLB/logos/athletics.png',
            'TOR': 'MLB/logos/blueJays.png',
            'ATL': 'MLB/logos/braves.png',
            'MIL': 'MLB/logos/brewers.png',
            'STL': 'MLB/logos/cardinals.png',
            'STl': 'MLB/logos/cardinals.png',
            'CHC': 'MLB/logos/cubs.png',
            'ARI': 'MLB/logos/diamondbacks.png',
            'LAD': 'MLB/logos/dodgers.png',
            'SFG': 'MLB/logos/giants.png',
            'CLE': 'MLB/logos/gaurdians.png',
            'SEA': 'MLB/logos/mariners.png',
            'MIA': 'MLB/logos/marlins.png',
            'NYM': 'MLB/logos/mets.png',
            'WSN': 'MLB/logos/nationals.png',
            'WSH': 'MLB/logos/nationals.png',
            'BAL': 'MLB/logos/orioles.png',
            'SDP': 'MLB/logos/padres.png',
            'PHI': 'MLB/logos/phillies.png',
            'PIT': 'MLB/logos/pirates.png',
            'TEX': 'MLB/logos/rangers.png',
            'TBR': 'MLB/logos/rays.png',
            'CIN': 'MLB/logos/reds.png',
            'BOS': 'MLB/logos/redSox.png',
            'COL': 'MLB/logos/rockies.png',
            'KCR': 'MLB/logos/royals.png',
            'DET': 'MLB/logos/tigers.png',
            'MIN': 'MLB/logos/twins.png',
            'CHW': 'MLB/logos/whiteSox.png',
            'NYY': 'MLB/logos/yankees.png'
        }
        self.id_logos = {
            108 : 'MLB/logos/angels.png',
            117 : 'MLB/logos/astros.png',
            133 : 'MLB/logos/athletics.png',
            141 : 'MLB/logos/blueJays.png',
            144 : 'MLB/logos/braves.png',
            158 : 'MLB/logos/brewers.png',
            138 : 'MLB/logos/cardinals.png',
            112 : 'MLB/logos/cubs.png',
            109 : 'MLB/logos/diamondbacks.png',
            119 : 'MLB/logos/dodgers.png',
            137 : 'MLB/logos/giants.png',
            114 : 'MLB/logos/gaurdians.png',
            136 : 'MLB/logos/mariners.png',
            146 : 'MLB/logos/marlins.png',
            121 : 'MLB/logos/mets.png',
            120 : 'MLB/logos/nationals.png',
            110 : 'MLB/logos/orioles.png',
            135 : 'MLB/logos/padres.png',
            143 : 'MLB/logos/phillies.png',
            134 : 'MLB/logos/pirates.png',
            140 : 'MLB/logos/rangers.png',
            139 : 'MLB/logos/rays.png',
            113 : 'MLB/logos/reds.png',
            111 : 'MLB/logos/redSox.png',
            115 : 'MLB/logos/rockies.png',
            118 : 'MLB/logos/royals.png',
            116 : 'MLB/logos/tigers.png',
            142 : 'MLB/logos/twins.png',
            145: 'MLB/logos/whiteSox.png',
            147 : 'MLB/logos/yankees.png'
        }

        self.id_abbr = {
            108: 'LAA',
            117: 'HOU',
            133: 'OAK',
            141: 'TOR',
            144: 'ATL',
            158: 'MIL',
            138: 'STL',
            112: 'CHC',
            109: 'ARI',
            119: 'LAD',
            137: 'SFG',
            114: 'CLE',
            136: 'SEA',
            146: 'MIA',
            121: 'NYM',
            120: 'WSH',
            110: 'BAL',
            135: 'SDP',
            143: 'PHI',
            134: 'PIT',
            140: 'TEX',
            139: 'TBR',
            113: 'CIN',
            111: 'BOS',
            115: 'COL',
            118: 'KCR',
            116: 'DET',
            142: 'MIN',
            145: 'CHW',
            147: 'NYY'
        }

        self.colors = {
            'mlb': blue,
            'LAA': red,
            'HOU': orange,
            'OAK': green,
            'TOR': blue,
            'ATL': red,
            'MIL': blue,
            'STL': red,
            'CHC': blue,
            'ARI': red,
            'LAD': blue,
            'SFG': orange,
            'CLE': red,
            'SEA': blue,
            'MIA': orange,
            'NYM': orange,
            'WSN': red,
            'WSH': red,
            'BAL': orange,
            'SDP': brown,
            'PHI': red,
            'PIT': yellow,
            'TEX': blue,
            'TBR': blue,
            'CIN': red,
            'BOS': red,
            'COL': purple,
            'KCR': blue,
            'DET': blue,
            'MIN': red,
            'CHW': black,
            'NYY': blue
        }
        self.abbr = {
            'LAA': 'Los Angeles Angels',
            'HOU': 'Houston Astros',
            'OAK': 'Oakland Athletics',
            'TOR': 'Toronto Blue Jays',
            'ATL': 'Atlanta Braves',
            'MIL': 'Milwaukee Brewers',
            'STL': 'St. Louis Cardinals',
            'CHC': 'Chicago Cubs',
            'ARI': 'Arizona Diamondbacks',
            'LAD': 'Los Angeles Dodgers',
            'SFG': 'San Francisco Giants',
            'CLE': 'Cleveland Indians',
            'SEA': 'Seattle Mariners',
            'MIA': 'Miami Marlins',
            'NYM': 'New York Mets',
            'WSN': 'Washington Nationals',
            'BAL': 'Baltimore Orioles',
            'SDP': 'San Diego Padres',
            'PHI': 'Philadelphia Phillies',
            'PIT': 'Pittsburgh Pirates',
            'TEX': 'Texas Rangers',
            'TBR': 'Tampa Bay Rays',
            'CIN': 'Cincinnati Reds',
            'BOS': 'Boston Red Sox',
            'COL': 'Colorado Rockies',
            'KCR': 'Kansas City Royals',
            'DET': 'Detroit Tigers',
            'MIN': 'Minnesota Twins',
            'CHW': 'Chicago White Sox',
            'NYY': 'New York Yankees'
        }

        self.names = {
            'Los Angeles Angels': 'LAA',
            'Houston Astros': 'HOU',
            'Oakland Athletics': 'OAK',
            'Toronto Blue Jays': 'TOR',
            'Atlanta Braves': 'ATL',
            'Milwaukee Brewers':'MIL',
            'St. Louis Cardinals' : 'STL',
            'Chicago Cubs': 'CHC',
            'Arizona Diamondbacks': 'ARI',
            'Los Angeles Dodgers' : 'LAD',
            'San Francisco Giants': 'SFG',
            'Cleveland Guardians': 'CLE',
            'Seattle Mariners': 'SEA',
            'Miami Marlins' : 'MIA',
            'New York Mets' : 'NYM',
            'Washington Nationals' : 'WSH',
            'Baltimore Orioles' : 'BAL',
            'San Diego Padres' : 'SDP',
            'Philadelphia Phillies' : 'PHI',
            'Pittsburgh Pirates' : 'PIT',
            'Texas Rangers' : 'TEX',
            'Tampa Bay Rays':'TBR',
            'Cincinnati Reds' : 'CIN',
            'Boston Red Sox' : 'BOS',
            'Colorado Rockies': 'COL',
            'Kansas City Royals': 'KCR',
            'Detroit Tigers': 'DET',
            'Minnesota Twins' : 'MIN',
            'Chicago White Sox': 'CHW',
            'New York Yankees' : 'NYY'
        }

    def get_labels(self, data):
        labels = []
        for line in data:
            labels.append(self.logos[line])
        return labels

    def get_labels_by_id(self, data):
        labels = []
        for line in data:
            labels.append(self.id_logos[line])
        return labels

    def get_colors(self, data):
        labels = []
        for line in data:
            labels.append(self.colors[line])
        return labels