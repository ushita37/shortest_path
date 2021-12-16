# © 2021 ushita37

import numpy as np


F = open('ChuoSobuEkimei.csv')
ekimeiList = F.readline().replace('\n', '').split(',')

a = np.loadtxt('JBarray1.csv',delimiter=',',dtype='int64')

HIGASHIIKI = 1
NISHIIKI = -1

def chuosobu_search(k, l, direction):
    plus_min = 0
    n = 0
    if direction == HIGASHIIKI: #東行(千葉方面)
        if a[k, l] == 9999:
            l = l + 1
            n = None
        elif a[k, l] > 0:
            plus_min = a[k, l]
            k = l
            n = l
            l = 0
        else:
            l = l + 1
            n = None
    else: #西行(三鷹方面)
        if a[k, l] < 0:
            plus_min = abs(a[k, l])
            k = l
            n = l
            l = 0
        else:
            l = l + 1
            n = None
    return [k, l, [n], plus_min]

def check_input(input1, input2):
    ret1 = False
    ret2 = False
    if input1 in ekimeiList:
        ret1 = True
    if input2 in ekimeiList:
        ret2 = True 
    return [ret1, ret2]
    

keyboard_dep = input('出発駅を入力してください>')
keyboard_arr = input('到着駅を入力してください>')


def ini_eastern(keyboard_dep):
    i = ekimeiList.index(keyboard_dep) #キーボードで入力された出発駅に対応するekimeiListのインデックスで行iを初期化
    j = 0
    finish_eastern = False
    eastern_idx = [i] #ekimeiListのインデックスを保存
    eastern_min = 0
    finish_western = False
    western_idx = [i]
    western_min = 0
    return [i, j, finish_eastern, eastern_idx, eastern_min, finish_western, western_idx, western_min]


def ini_western(keyboard_dep):
    i = ekimeiList.index(keyboard_dep)
    j = 0
    return [i, j]


[check1, check2] = check_input(keyboard_dep, keyboard_arr)
if check1 == False:
    print(f'{keyboard_dep}駅は存在しません')
    exit()
if check2 == False:
    print(f'{keyboard_arr}駅は存在しません')
    exit()
if keyboard_arr == keyboard_dep:
    print('出発駅と到着駅が同じです')
    exit()

[i, j, finish_eastern, eastern_idx, eastern_min, finish_western, western_idx, western_min] = ini_eastern(keyboard_dep)
while finish_eastern == False:
    [i, j, idx, plus_min] = chuosobu_search(i, j, HIGASHIIKI)
    if j > 38: #終着駅の行で39列目以降を参照しようとした場合
        print('東行には到着駅がありません')
        finish_eastern = True #東行でリストの最後まで調べたが目的地が見つからず西行に必ず目的地が存在するので、西行の処理を実行
    if idx[0] != None:
        eastern_idx += idx #元々あるインデックスのリストに、新しく見つかった隣駅のインデックスを含むリストを連結
        eastern_min += plus_min
        if idx[0] == ekimeiList.index(keyboard_arr):
            finish_eastern = True
            finish_western = True #東行で目的地が見つかったら西行で目的地は絶対に見つからないので、西行の処理は省略

[i, j] = ini_western(keyboard_dep)
while finish_western == False:
    [i, j, idx, plus_min] = chuosobu_search(i, j, NISHIIKI)
    if idx[0] != None:
        western_idx += idx
        western_min += plus_min
        if idx[0] == ekimeiList.index(keyboard_arr):
            finish_western =True
#東行で目的地が見つからなかった場合にのみ西行を実行し、その場合は i行目 → 1行目 のどこかで必ず目的地が見つかるので、0行目を参照することは絶対にない
#従って0行目のみがとり得る39列目以降を参照することも絶対にない

if eastern_idx[-1] == ekimeiList.index(keyboard_arr): #東行のループで最後に見つかった隣駅のインデックスが到着駅のインデックスに等しいか
    print('「東行・千葉方面」')
    for ekimei_index in eastern_idx:
        print(ekimeiList[ekimei_index])
    print(f'所要時間は{eastern_min}分です')
    print('到着しました')
else:
    print('「西行・三鷹方面」')
    for ekimei_index in western_idx:
        print(ekimeiList[ekimei_index])
    print(f'所要時間は{western_min}分です')
    print('到着しました')
