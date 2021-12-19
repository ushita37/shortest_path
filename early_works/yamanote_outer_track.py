# © 2021 ushita37

import numpy as np
# import pandas as pd

# ekimei = pd.read_csv('stationName.csv', header=None, encoding='Shift-JIS').values.tolist()
# ekimeiList = ekimei[0]

# pandasを使うと正常に動作しないことがあるので、上記の4・6・7行目をコメントアウトし、以下の10・11行目を実行している
F = open('stationName.csv')
ekimeiList = F.readline().replace('\n', '').split(',')

a = np.loadtxt('rinnsetsuValueOnly2.csv',delimiter=',',dtype='int64')

finish_rounding = False
i = 0
j = 0

print(ekimeiList[0])
while finish_rounding != True:
    if a[i,j] == -1:
        print(f'次は{ekimeiList[j]}')
        i = j
        j = 0
    else:
        j = j + 1
        if j > 29:
            print(f'aの{i}行目には隣駅の情報がありません')
            break
    if (i,j) == (0,0):
        print('一周しました')
        finish_rounding = True