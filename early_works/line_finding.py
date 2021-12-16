# © 2021 ushita37

F = open('ChuoSobuEkimei.csv')
G = open('stationName.csv')

keyboard_dep = input('出発駅を入力してください>')
keyboard_arr = input('到着駅を入力してください>')

ekimeiListF = F.readline().replace('\n', '').split(',')
ekimeiListG = G.readline().replace('\n', '').split(',')

if keyboard_dep in ekimeiListF:
    if keyboard_dep in ekimeiListG:
        print(f'出発駅は＜山手線、中央・総武線＞{keyboard_dep}')
    else:
        print(f'出発駅は＜中央・総武線＞{keyboard_dep}')
elif keyboard_dep in ekimeiListG:
    print(f'出発駅は＜山手線＞{keyboard_dep}')
else:
    print(f'{keyboard_dep}駅は存在しません')

if keyboard_arr in ekimeiListF:
    if keyboard_arr in ekimeiListG:
        print(f'到着駅は＜山手線、中央・総武線＞{keyboard_arr}')
    else:
        print(f'到着駅は＜中央・総武線＞{keyboard_arr}')
elif keyboard_arr in ekimeiListG:
    print(f'到着駅は<山手線＞{keyboard_arr}')
else:
    print(f'{keyboard_arr}駅は存在しません')

