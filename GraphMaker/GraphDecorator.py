from PIL import Image, ImageDraw, ImageFont
# from Graph import *


class GraphComponent():
    def make_graph(self):
        pass


class ConceteGraph(GraphComponent):
    def __init__(self):
        self.children = []
        self.width, self.height = 1920, 1028
        self.image = Image.new('RGBA', (self.width, self.height))
        self.draw = ImageDraw.ImageDraw(self.image)
        self.draw.rectangle((0, 0, self.width, self.height), fill=(255, 255, 255, 255))

    def make_graph(self):
        for child in self.children:
            child.make_graph()
        return self.image

    def add_children(self, child):
        if isinstance(child, GraphComponent):
            self.children.append(child)


class ScatterTitle(GraphComponent):
    def __init__(self, title, subtitle, credits, image, draw):
        self.title_font = ImageFont.truetype('Roboto-Regular.ttf', 50)
        self.sub_title_font = ImageFont.truetype('Roboto-Regular.ttf', 30)
        self.width, self.height = 1920, 1028
        self.title = title
        self.subtitle = subtitle
        self.credits = credits
        self.image = image
        self.draw = draw

    def make_graph(self):
        text_box = 70
        tw, th = self.draw.textsize(self.title, font=self.title_font)
        sw, sh = self.draw.textsize(self.subtitle, font=self.sub_title_font)
        cw, ch = self.draw.textsize(self.credits, font=self.sub_title_font)
        self.draw.text(((text_box), (self.height / 2) - th), text=self.title, fill=(0, 0, 0, 255), font=self.title_font)
        self.draw.text(((text_box), (self.height / 2) + (sh)), text=self.subtitle, fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text(((text_box), (self.height / 2) + (2 * ch)), text=self.credits, fill=(0, 0, 0, 255), font=self.sub_title_font)


class ScatterCornerPlacement(GraphComponent):
    def __init__(self, corner_labels, image, draw):
        self.corner_labels = corner_labels
        self.image = image
        self.draw = draw
        self.title_font = ImageFont.truetype('Roboto-Regular.ttf', 50)
        self.sub_title_font = ImageFont.truetype('Roboto-Regular.ttf', 30)

    def make_graph(self):
        x, y = 800, 20
        g: Image.Image = Image.open('1.png')
        graph_size = g.size
        gx, gy = graph_size
        right_edge = x + gx - 20
        left_edge = x + 110
        bottom_egge = y + gy - 80
        top_edge = y - 20
        trw, trh = self.draw.textsize(self.corner_labels[0], font=self.sub_title_font)
        brw, brh = self.draw.textsize(self.corner_labels[3], font=self.sub_title_font)
        self.draw.text((left_edge, top_edge + trh), text=self.corner_labels[1], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((left_edge, bottom_egge - brh), text=self.corner_labels[3], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((right_edge - trw, top_edge + trh), text=self.corner_labels[0], fill=(0, 0, 0, 255), font=self.sub_title_font)
        self.draw.text((right_edge - brw, bottom_egge - brh), text=self.corner_labels[2], fill=(0, 0, 0, 255), font=self.sub_title_font)

