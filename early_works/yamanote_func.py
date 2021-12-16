# © 2021 ushita37

import numpy as np
import pandas as pd

# 定数定義
UCHIMAWARI = 1
SOTOMAWARI = -1

ekimei = pd.read_csv('stationName.csv', header=None, encoding='Shift-JIS').values.tolist()
ekimeiList = ekimei[0]

a = np.loadtxt('rinnsetsuValueOnly2.csv',delimiter=',',dtype='int64')

finish_rounding = False
i = 0
j = 0
station_name = ekimeiList[j]

print(station_name)


def yamanote(direction, k, l):
    n = ""
    if a[k,l] == direction:
        k = l
        n = ekimeiList[l]
        l = 0
    else:
        l = l + 1
        n = None # 隣の駅が見つからない場合
    return [k, l, n]


while finish_rounding != True:
    [i, j, station_name] = yamanote(UCHIMAWARI, i, j)
    if station_name != None:
        print(station_name)
    if j > 29:
        print(f'aの{j}行目には隣駅の情報がありません')
        break
    if (i,j) == (0,0):
        print ('一周しました')
        finish_rounding = True