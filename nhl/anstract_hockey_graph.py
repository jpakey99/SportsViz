from PIL import Image, ImageDraw, ImageFont
from Graph import BarGraph, Graph2DScatter
from nhl_logos import logo_search
from test import get_list_values, clean_data
from statistics import stdev
import standings

GA, XGA, GF, XGF = 73, 60, 25, 12


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
        adj = len(self.corner_labels[2])//3
        self.draw.text((left_edge, top_edge + trh), text=self.corner_labels[1], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((left_edge, bottom_edge - brh), text=self.corner_labels[3], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((right_edge - trw, top_edge + trh), text=self.corner_labels[0], fill=(0, 0, 0, 255), font=self.sub_title_font)
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
        self.graph.graph().savefig('1', bbox_inches='tight')
        g: Image.Image = Image.open('1.png')
        self.graph_size = g.size
        self.image.paste(g, box=(x, y))
        self.corner_label_placement()


class TeamStatViz(AbstractScatterGraph):
    def __init__(self, team_stats, date: str, title, credits, subtitle, corner_labels):
        super().__init__(title=title, credits=credits, subtitle=subtitle, date=date, corner_labels=corner_labels)
        # self.year = int(date.split('-')[2])

    def display_image(self):
        self.image.show()

    def combine_lists(self, list1, list2):
        combined, x, y, labels = [], [], [], []
        for item in list1:
            team = item[0]
            for i in list2:
                t = i[0]
                if team == t:
                    combined.append((team, item[1], i[1]))
                    x.append(item[1])
                    y.append(i[1])
                    labels.append(team)
        return combined, x, y, labels

    def find_z_score(self, data, value):
        mean = 0
        for item in data:
            mean += item
        mean = mean / len(data)
        top = value - mean
        bottom = stdev(data)
        return top / bottom


class TeamScatterGraph(TeamStatViz):
    def __init__(self, team_stats, date: str, title, credits, subtitle, corner_labels):
        super().__init__(team_stats, title=title, credits=credits, subtitle=subtitle, date=date, corner_labels=corner_labels)


class TeamCard(TeamStatViz):
    def __init__(self, date: str):
        team_data = clean_data()
        team_stats = get_list_values(XGA, XGF, team_data)
        super().__init__(team_stats, date, 'xGoals', 'MoneyPuck', 'hey', ['Good', 'Bad', 'Fun', 'dull'])
