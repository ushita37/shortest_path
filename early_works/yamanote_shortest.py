# © 2021 ushita37

import numpy as np


F = open('stationName.csv')
ekimeiList = F.readline().replace('\n', '').split(',')

a = np.loadtxt('JYarray1.csv',delimiter=',',dtype='int64')

UCHIMAWARI = 1
SOTOMAWARI = -1


def yamanote_search(k, l, direction):
    plus_min = 0
    n = 0
    if direction == UCHIMAWARI: #内回り
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
    else: #外回り
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

def ini_inner(keyboard_dep):
    i = ekimeiList.index(keyboard_dep) #キーボードで入力された出発駅に対応するekimeiListのインデックスで行iを初期化
    j = 0
    finish_inner = False
    inner_idx = [i] #ekimeiListのインデックスを保存
    inner_min = 0
    return [i, j, finish_inner, inner_idx, inner_min]


def ini_outer(keyboard_dep):
    i = ekimeiList.index(keyboard_dep)
    j = 0
    finish_outer = False
    outer_idx = [i]
    outer_min = 0
    return [i, j, finish_outer, outer_idx, outer_min]



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

[i, j, finish_inner, inner_idx, inner_min] = ini_inner(keyboard_dep)
while finish_inner == False:
    [i, j, idx, plus_min] = yamanote_search(i, j, UCHIMAWARI)
    if idx[0] != None:
        inner_idx += idx #元々あるインデックスのリストに、新しく見つかった隣駅のインデックスを含むリストを連結
        inner_min += plus_min
        if idx[0] == ekimeiList.index(keyboard_arr):
            finish_inner =True

[i, j, finish_outer, outer_idx, outer_min] = ini_outer(keyboard_dep)
while finish_outer == False:
    #print('外回り')#デバッグ
    [i, j, idx, plus_min] = yamanote_search(i, j, SOTOMAWARI)
    if idx[0] != None:
        outer_idx += idx
        outer_min += plus_min
        if idx[0] == ekimeiList.index(keyboard_arr):
            finish_outer =True

if inner_min < outer_min:
    print(f'内回りが外回りより{outer_min - inner_min}分早い')
    for ekimei_index in inner_idx:
        print(ekimeiList[ekimei_index])
    print(f'所要時間は{inner_min}分です')
    print('到着しました')
elif inner_min > outer_min:
    print(f'外回りが内回りより{inner_min - outer_min}分早い')
    for ekimei_index in outer_idx:
        print(ekimeiList[ekimei_index])
    print(f'所要時間は{outer_min}分です')
    print('到着しました')
else:
    print('内回りと外回りの所要時間が同じなので内回りの経路を表示')
    for ekimei_index in inner_idx:
        print(ekimeiList[ekimei_index])
    print(f'所要時間は{inner_min}分です')
    print('到着しました')