from PIL import Image, ImageDraw, ImageFont
from Graph import Graph2DScatter
import labels
from nfl_data import *


XPASS, EPA, POS_TEAM = 370, 73, 7


class AbstractGraph:
    def __init__(self, title, credits, subtitle, date):
        self.title = title
        self.credits = credits
        self.subtitle = subtitle
        self.date = date
        self.width, self.height = 1920, 1028
        self.image = Image.new('RGBA', (self.width, self.height))
        self.draw = ImageDraw.ImageDraw(self.image)
        self.draw.rectangle((0, 0, self.width, self.height), fill=(255, 255, 255, 255))
        self.title_font = ImageFont.truetype('Roboto-Regular.ttf', 50)
        self.sub_title_font = ImageFont.truetype('Roboto-Regular.ttf', 30)

    def save_image(self):
        self.image.save('graphs//' + self.title + '_' + self.date + '.png')


class AbstractScatterGraph(AbstractGraph):
    def __init__(self, title, credits, subtitle,date, corner_labels):
        super().__init__(title, credits, subtitle, date)
        self.corner_labels = corner_labels
        self.graph : Graph2DScatter

    def corner_label_placement(self):
        x, y = 800, 20
        gx, gy = self.graph_size
        right_edge = x+ gx - 20
        left_edge = x + 110
        bottom_edge = y+gy-80
        top_edge = y - 20
        trw, trh = self.draw.textsize(self.corner_labels[0], font=self.sub_title_font)
        brw, brh = self.draw.textsize(self.corner_labels[3], font=self.sub_title_font)
        adj1 = len(self.corner_labels[3])//3
        adj = len(self.corner_labels[2])//3
        self.draw.text((left_edge, top_edge + trh), text=self.corner_labels[1], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((left_edge, bottom_edge - brh), text=self.corner_labels[3], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((right_edge - adj1*trw, top_edge + trh), text=self.corner_labels[0], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((right_edge - adj*(brw),bottom_edge - brh), text=self.corner_labels[2], fill=(0, 0, 0, 255), font=self.sub_title_font)

    def title_placement(self):
        x, y = 800, 20
        text_box = 70
        tw, th = self.draw.textsize(self.title, font=self.title_font)
        sw, sh = self.draw.textsize(self.subtitle, font=self.sub_title_font)
        cw, ch = self.draw.textsize(self.credits, font=self.sub_title_font)
        self.draw.text(((text_box), (self.height / 2) - th), text=self.title, fill=(0, 0, 0, 255), font=self.title_font)
        self.draw.text(((text_box), (self.height / 2) + 10), text=self.subtitle, fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text(((text_box), (self.height / 2) + (ch+sh)), text=self.credits, fill=(0, 0, 0, 255), font=self.sub_title_font)

    def create_image(self):
        x, y = 800, 20
        self.title_placement()
        self.graph.graph()
        # .savefig('1', bbox_inches='tight', pad_inches = .25)
        g: Image.Image = Image.open('1.png')
        # g.show()
        self.graph_size = g.size
        self.image.paste(g, box=(x, y))
        self.corner_label_placement()


class DefenseAfterTimeoPos(AbstractScatterGraph):
    def __init__(self, date: str):
        # team_data = nhl_data.clean_data(STAN)
        # team_stats = nhl_data.get_list_values(XGF, XGA, team_data)
        data = season_data(2021)
        for i, e in enumerate(data.columns):
            print(i,e)
        self.stats = {}
        self.stats = {}
        title = 'EPA Difference'
        team_stats = []
        self.get_stats(data)
        super().__init__(title=title, date=date, corner_labels='', credits='', subtitle='')
        # self.axis_labels =  ('xGoalsFor/60', 'xGoalsAgainst/60')
        # self.graph = Graph2DScatter(team_stats[2], team_stats[3], self.logos, self.axis_labels ,inverty=True, diag_lines=True)
        # self.graph_size = (0, 0)

    def play(self, play):
        pos_team = play[POS_TEAM]
        if pos_team not in self.stats.keys():
            self.stats[pos_team] = {
                'epa_rush' : 0,
                'epa_pass' : 0,
                'pass' : 0,
                'run': 0,
                'xpass': 0
            }
        # print(play[349], play[348])
        if int(play[347]) == 1:
            self.stats[pos_team]['epa_pass'] += play[EPA]
            self.stats[pos_team]['pass'] += 1
            self.stats[pos_team]['xpass'] += play[XPASS]
        elif int(play[348]) == 1:
            self.stats[pos_team]['epa_rush'] += play[EPA]
            self.stats[pos_team]['run'] += 1
            self.stats[pos_team]['xpass'] += play[XPASS]

    def game(self, game):
        for play in game:
            self.play(play)

    def get_stats(self, data):
        game_data = get_indiv_game_data(data)
        for game in game_data:
            self.game(game)
        for team in self.stats:

            print(self.stats[team])

    def save_image(self):
        self.image.save('NHL/graphs/' + 'xTeam_Tiers' + '_' + self.date + '.png')


def market_win_rate():
    m_wp,  = 97
    data_frame = season_data(2021)
    game_data = get_indiv_game_data(data_frame)
    for game in game_data:
        for play in game:



DefenseAfterTimeoPos('013827')