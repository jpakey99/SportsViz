from matplotlib import pyplot as plt
import requests
from MLB.labels import MLBLabel
import pybaseball


def statcast_stats(url):
    # url + '//*[@id="btnCSV"]'
    r = requests.get(url, allow_redirects=True)
    open('statcast.txt', 'wb').write(r.content)
    f = open('statcast.txt', 'r')
    f.readline()
    names = MLBLabel().names
    labels, x, y, combined = [], [], [], []
    for l in f:
        line = l.split(',')
        if line[0] in names:
            labels.append(names[line[0]])
            x.append(float(line[-2]))
            y.append(float(line[-3]))
            combined.append((names[line[0]], float(line[-3]), float(line[-2])))
    return combined, x, y, labels


def statcast_stats_fielding(url):
    r = requests.get(url, allow_redirects=True)
    open('statcast.txt', 'wb').write(r.content)
    f = open('statcast.txt', 'r')
    fan = pybaseball.team_fielding(2022)
    names = MLBLabel().names
    drs = {}
    for t in range(len(fan['Team'])):
        id = fan.loc[t]
        for name in names.keys():
            if id['Team'] in name:
                drs[str(names[name])] = int(id['DRS'])
    f.readline()
    names = MLBLabel().id_abbr
    labels, x, y, combined = [], [], [], []
    for l in f:
        line = l.split(',')
        if int(line[1]) in names:
            labels.append(names[int(line[1])])
            x.append(int(line[4]))
            y.append(drs[names[int(line[1])]])
            combined.append((names[int(line[1])], int(line[4]), drs[names[int(line[1])]]))
    return combined, x, y, labels


def read_team_csv():
    info = [0] * 92
    file = open("Total_Team_Stats.csv", "r")

    file.readline()
    line_num = 0
    for line in file:
        line = line.strip("\n")
        values = line.split(",")
        info[line_num] = [float(i) for i in values]
        line_num += 1

    file.close()
    return info


def create_table(x_axis, y_axis, title, x_label, y_label, average):
    plt.plot(average[0], average[1] )
    plt.scatter(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('I did something.png')
    plt.show()


def main():
    info = read_team_csv()
    x_axis = [0] * (len(info) - 2)
    y_axis = [0] * (len(info) - 2)
    line = 0
    for team in info:
        if line == 0:
            average = [team[3], team[0]]
        elif line <= len(info) - 2 and line > 0:
            y_axis[(line-1)] = team[0]
            x_axis[(line-1)] = team[3]
        line = line + 1
    create_table(x_axis, y_axis, "Win % vs Walks", "Walks", "Win %", average)


# main()

# print(statcast_stats_fielding('https://baseballsavant.mlb.com/leaderboard/outs_above_average?type=Fielding_Team&startYear=2022&endYear=2022&split=no&team=&range=year&min=q&pos=&roles=&viz=hide&csv=true'))