import draft_database


def fv_normalized(fv):
    fv = fv.strip('"')
    if fv == '"30"' or fv == '':
        return 2
    elif fv == '35+':
        return 3
    elif fv == '40':
        return 4
    elif fv == '40+':
        return 5
    elif fv == '45':
        return 6
    elif fv == '45+':
        return 7
    elif fv == '50':
        return 8
    elif fv == '55+':
        return 9
    elif fv == '60':
        return 10
    elif fv == '65+':
        return 11
    elif fv == '70':
        return 12


def read_file(year, player_list):
    file = open('draft//rankings//'+str(year)+'_draft.csv')
    file.readline()
    # name = 3, fv=12
    value_added = {}
    for line in file:
        player = line.split(',')
        fv = fv_normalized(player[12])
        found = False
        for draftee in player_list:
            name = player[3].strip('"')
            f_name, l_name = name.split(' ')
            df, dl = draftee[0].strip("'"), draftee[1].strip("'")
            # print(f_name, draftee, l_name, draftee)
            if f_name in df and l_name in dl:
                print(value_added.keys(), draftee[2], draftee[2] in value_added.keys())
                if draftee[2] in value_added.keys():
                    value_added[draftee[2]] +=fv
                else:
                    value_added[draftee[2]] = fv
                found = True
        if not found:
            pass
    print(value_added)



if __name__ == '__main__':
    player_list = draft_database.get_player_drafted_year(2015)
    read_file(2015, player_list)