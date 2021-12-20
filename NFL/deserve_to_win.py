from PIL import Image, ImageDraw, ImageFont
from nfl_data import *
import random
import labels

width, height = 1920, 1028

TD_PROB, SAFETY_PROB, FG_PROB, OPP_TD_PROB, OPP_SAFETY_PROB, OPP_FG_PROB = 70, 69, 68, 67, 66, 65
SIMS = 10000

class DeserveToWinMeter():
    def __init__(self, week):
        self.week = week
        data_frame = season_data(2021)
        self.game_data = get_indiv_game_data(data_frame)
        self.deserve_to_win = {}
        self.probabilities = {}
        self.get_probabilities()
        self.get_deserve_to_win()

        self.image = Image.new('RGBA', (width, height))
        self.draw = ImageDraw.ImageDraw(self.image)
        self.draw.rectangle((0, 0, width, height), fill=(255, 255, 255, 255))
        title_font = ImageFont.truetype('Roboto-Regular.ttf', 70)
        sub_title_font = ImageFont.truetype('Roboto-Regular.ttf', 40)

        home_x, away_x, y, size = 1740, 960, 10, (height-20)//len(self.deserve_to_win)
        half = ((away_x + size) + home_x) // 2
        print(size)
        for p in self.deserve_to_win:
            self.home_l = Image.open(labels.logos[self.deserve_to_win[p]['home_team']]).resize((70, 70))
            self.away_l = Image.open(labels.logos[self.deserve_to_win[p]['away_team']]).resize((70, 70))

            self.color_correction(self.home_l)
            self.color_correction(self.away_l)

            self.image.paste(self.away_l, box=(away_x, y))
            self.image.paste(self.home_l, box=(home_x, y))
            adjust = 35
            dec = round(self.deserve_to_win[p]['home_team_wins']/SIMS, 2)
            percent = round(100*(dec))
            print(percent, dec)
            text_adjust = adjust/2
            if percent < 50:
                edge = int(((half - away_x+size) * dec) + away_x+size)
                self.draw.line((half, y + adjust, edge, y + adjust), fill=(0, 255, 0, 255), width=size - 10)
                tw, th = self.draw.textsize(str(100-percent), font=sub_title_font)
                print(half - (2*tw))
                self.draw.text((1298, y+text_adjust), text=str(100-percent), fill=(0, 0, 0, 255), font=sub_title_font)
            else:
                edge = int(((home_x - half) * dec) + half)
                self.draw.line((half, y + adjust, edge, y + adjust), fill=(0, 255, 0, 255), width=size - 10)
                tw, th = self.draw.textsize(str(percent), font=sub_title_font)
                self.draw.text((half + tw, y+text_adjust), text=str(percent), fill=(0, 0, 0, 255), font=sub_title_font)
            y += size
        self.draw.line((half, 10, half, height -10), fill=(0,0,0,255), width=10)

        title = 'Week ' + str(week) + ' Deserve To Win'
        subtitle = 'data: nflfastr, twitter: @GraphingSports'
        tw, th = self.draw.textsize(title, font=title_font)
        self.draw.text(((70), (height / 2) - th), text=title, fill=(0, 0, 0, 255), font=title_font)
        self.draw.text(((70), (height / 2) + 10), text=subtitle, fill=(0, 0, 0, 255), font=sub_title_font)

        self.image.save('deserve'+str(week)+ '.png')

    def get_probabilities(self):
        for game in self.game_data:
            for play in game:
                # print(play)
                if play[6] == self.week:
                    if play[1] not in self.probabilities:
                        self.probabilities[play[1]] = {"plays" : []}
                    home_team, away_team = play[4], play[5]
                    drive = play[19]
                    if play[9] == home_team:
                        td_for, fg_for, safety_for = play[TD_PROB], play[FG_PROB], play[SAFETY_PROB]
                        td_opp, fg_opp, safety_opp = play[OPP_TD_PROB], play[OPP_FG_PROB], play[OPP_SAFETY_PROB]
                        self.probabilities[play[1]]['plays'].append((td_for, fg_for, safety_for, td_opp, fg_opp, safety_opp, drive))
                    else:
                        td_for, fg_for, safety_for = play[TD_PROB], play[FG_PROB], play[SAFETY_PROB]
                        td_opp, fg_opp, safety_opp = play[OPP_TD_PROB], play[OPP_FG_PROB], play[OPP_SAFETY_PROB]
                        self.probabilities[play[1]]['plays'].append((td_opp, fg_opp, safety_opp, td_for, fg_for, safety_for, drive))

    def sim_play(self, play, away_score, home_score):
        scored_on_drive = False
        rand = random.random()
        if rand <= play[0]:
            home_score += 6
            scored_on_drive = True
        elif rand <= play[0] + play[1]:
            home_score += 3
            scored_on_drive = True
        elif rand <= play[0] + play[1] + play[2]:
            home_score += 2
            scored_on_drive = True
        elif rand <= play[0] + play[1] + play[2] + play[3]:
            away_score += 6
            scored_on_drive = True
        elif rand <= play[0] + play[1] + play[2] + play[3] + play[4]:
            away_score += 3
            scored_on_drive = True
        elif rand <= play[0] + play[1] + play[2] + play[3] + play[4] + play[5]:
            away_score += 2
            scored_on_drive = True
        return away_score, home_score, scored_on_drive

    def get_deserve_to_win(self):
        for game in self.probabilities:
            # print(self.probabilities[game])
            key = game.split("_")
            self.deserve_to_win[game] = {
                'home_team' : key[-1],
                'away_team' : key[-2],
                'home_team_wins': 0
            }
            for _ in range(SIMS):
                home_score, away_score = 0,0
                scored_on_drive, current_drive_number = False, 0
                for play in self.probabilities[game]['plays']:
                    if scored_on_drive and current_drive_number == play[-1]:
                        pass
                    elif scored_on_drive and current_drive_number != play[-1]:
                        scored_on_drive = False
                        current_drive_number = play[-1]
                        away_score, home_score, scored_on_drive = self.sim_play(play, away_score, home_score)
                    else:
                        current_drive_number = play[-1]
                        away_score, home_score, scored_on_drive = self.sim_play(play, away_score, home_score)
                if home_score > away_score:
                    self.deserve_to_win[game]['home_team_wins'] += 1

    def color_correction(self, img):
        home_logo = img.load()

        for i in range(img.size[0]):  # for every pixel:
            for j in range(img.size[1]):
                if home_logo[i, j] == (0, 0, 0, 0):
                    # change to black if not red
                    home_logo[i, j] = (255, 255, 255, 255)


DeserveToWinMeter(13)