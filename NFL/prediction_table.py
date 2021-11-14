from PIL import Image, ImageDraw, ImageFont
from nfl_data import *
import labels

width, height = 1920, 1028


class WeekPredictions():
    def __init__(self, week):
        data_frame = season_data(2021)
        team_dict = get_data(data_frame)
        preds = prediction(team_dict)
        self.image = Image.new('RGBA', (width, height))
        self.draw = ImageDraw.ImageDraw(self.image)
        self.draw.rectangle((0, 0, width, height), fill=(255, 255, 255, 255))
        title_font = ImageFont.truetype('Roboto-Regular.ttf', 70)
        sub_title_font = ImageFont.truetype('Roboto-Regular.ttf', 40)

        home_x, away_x, y, size = 1740, 960, 10, (height-20)//len(preds)
        half = ((away_x + size) + home_x) // 2
        print(size)
        for p in preds:
            self.home_l = Image.open(labels.logos[p[0]]).resize((70, 70))
            self.away_l = Image.open(labels.logos[p[1]]).resize((70, 70))

            self.color_correction(self.home_l)
            self.color_correction(self.away_l)

            self.image.paste(self.away_l, box=(away_x, y))
            self.image.paste(self.home_l, box=(home_x, y))
            adjust = 35
            if p[0] == p[2]:
                self.draw.line((half, y+adjust, home_x, y+adjust), fill=(0, 255, 0, 255), width=size-10)
            elif p[1] == p[2]:
                self.draw.line((half, y+adjust, away_x+size, y+adjust), fill=(0, 255, 0, 255), width=size-10)
            y += size
        self.draw.line((half, 10, half, height -10), fill=(0,0,0,255), width=10)

        title = 'Week ' + week + ' NFL Predictions'
        subtitle = 'data: nflfastr, twitter: @GraphingSports'
        tw, th = self.draw.textsize(title, font=title_font)
        self.draw.text(((70), (height / 2) - th), text=title, fill=(0, 0, 0, 255), font=title_font)
        self.draw.text(((70), (height / 2) + 10), text=subtitle, fill=(0, 0, 0, 255), font=sub_title_font)

        self.image.save('week10' '.png')

    def color_correction(self, img):
        home_logo = img.load()

        for i in range(img.size[0]):  # for every pixel:
            for j in range(img.size[1]):
                if home_logo[i, j] == (0, 0, 0, 0):
                    # change to black if not red
                    home_logo[i, j] = (255, 255, 255, 255)





WeekPredictions('10')