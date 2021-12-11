from NFL.nfl_data import draft_data
from Graph import Graph2DScatter


class OverallDrafts():
    def __init__(self):
        pick_years = []
        years = range(1951, 2020)
        y=0
        for year in years:
            # print(year)
            draft_data(str(year))
            data = open('nfltest.csv')
            data.readline()
            picks = []
            i = 0
            for line in data:
                # print('hi', line)
                splitline = line.split(',')
                if splitline[1] != 'Rnd':
                    try:
                        if y == 0:
                            picks.append(17*(int(splitline[11])/int(splitline[13])))
                        else:
                            picks[i] += int(splitline[11])
                    except:
                        picks.append(0)
                    i+= 1

            pick_years.append(picks)

        weighted_p = []
        for pick in range(len(picks)):
            picks[pick] = picks[pick]/(2020-1951)
            if pick == 0:
                weighted_p.append((picks[pick] + picks[pick+1])/2)
            elif pick == len(picks)-1:
                weighted_p.append((picks[pick] + picks[pick - 1]) / 2)
            else:
                weighted_p.append((picks[pick] + picks[pick + 1]+ picks[pick - 1]) / 3)
            print(pick, picks[pick])
        print(picks)
        ticks = range(1,255, 31)
        g = Graph2DScatter(range(1,len(picks)+1), picks, axis_labels=['', ''], labels=[], average_lines=False, diag_lines=False, x_ticks=ticks)
        g.graph().show()



OverallDrafts()