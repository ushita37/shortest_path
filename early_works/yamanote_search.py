# © 2021 ushita37

import numpy as np


F = open('stationName.csv')
ekimeiList = F.readline().replace('\n', '').split(',')

uchimawaList = ['uchimawari', '内回り', 'inner', 'inner_track', 'inner-track', 'innertrack','うちまわり','ウチマワリ','ｳﾁﾏﾜﾘ']
sotomawaList = ['sotomawari', '外回り', 'outer', 'outer_track', 'outer-track', 'outertrack','そとまわり','ソトマワリ','ｿﾄﾏﾜﾘ']

a = np.loadtxt('JYarray1.csv',delimiter=',',dtype='int64')


def yamanote_search(k, l, direction):
    plus_min = 0
    n = ""
    if direction == 1:
        if a[k, l] == 9999:
            l = l + 1
            n = None
        elif a[k, l] > 0:
            plus_min = a[k, l]
            k = l
            n = ekimeiList[l]
            l = 0
        else:
            l = l + 1
            n = None
    else:
        if a[k, l] < 0:
            plus_min = abs(a[k, l])
            k = l
            n = ekimeiList[l]
            l = 0
        else:
            l = l + 1
            n = None
    return [k, l, n, plus_min]


def check_input(input1, input2, input3):
    ret1 = False
    ret2 = False
    ret3 = 0
    if input1 in ekimeiList:
        ret1 = True
    if input2 in ekimeiList:
        ret2 = True
    if input3 in uchimawaList:
        ret3 = 1
    elif input3 in sotomawaList:
        ret3 = -1
    else:
        ret3 = None 
    return [ret1, ret2, ret3]
    

keyboard_dep = input('出発駅を入力してください>')
keyboard_arr = input('到着駅を入力してください>')
keyboard_direction = input('方向を入力してください>').lower()


def initialize(keyboard_dep):
    i = ekimeiList.index(keyboard_dep) #キーボードで入力された出発駅に対応するekimeiListのインデックスで行iを初期化
    j = 0
    finish_route = False
    station_name = ekimeiList[i]
    min = 0
    return [i, j, finish_route, station_name, min]


[check1, check2, check3] = check_input(keyboard_dep, keyboard_arr, keyboard_direction)
if check1 == False:
    print(f'{keyboard_dep}駅は存在しません')
    exit()
if check2 == False:
    print(f'{keyboard_arr}駅は存在しません')
    exit()
if check3 == None:
    print('方向の入力が間違っています')
    exit()
if keyboard_arr == keyboard_dep:
    print('出発駅と到着駅が同じです')
    exit()
[i, j, finish_route, station_name, min] = initialize(keyboard_dep)
print(station_name)
while finish_route == False:
    [i, j, station_name, plus_min] = yamanote_search(i, j, check3)
    if station_name != None:
        print(station_name)
        min += plus_min
        if j > 29:
            print(f'aの{j}行目には隣駅の情報がありません')
            break
        if station_name == keyboard_arr:
            print (f'累計所要時間は{min}分です')
            print('到着しました')
            finish_route =True