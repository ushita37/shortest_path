# © 2021 ushita37
# 失敗作

import sys
import numpy as np
import shortest_path_def as spd



ekimeiJB = open('JBekimei.csv') # 中央総武線各駅停車の駅名
ekimeiJY = open('JYekimei.csv') # 山手線の駅名
matrixJB = np.loadtxt('JBarray2.csv', delimiter=',', dtype='int64') # 中央総武線各駅停車の所要時間のマトリックス
matrixJY = np.loadtxt('JYarray2.csv', delimiter=',', dtype='int64') # 山手線の所要時間のマトリックス
trans_matrix = np.loadtxt('Transfer1.csv', delimiter=',', dtype='int64')
trans_stas = open('TransferSta1.csv')
trans_lines = open('TransferLines1.csv')


#keyboard_dep = input('出発駅を入力してください>')
#keyboard_arr = input('到着駅を入力してください>')

args = sys.argv
keyboard_dep = args[1] #出発駅
keyboard_arr = args[2] #到着駅

ekimeiListJB = ekimeiJB.readline().replace('\n', '').split(',')
checkDepJB = False
checkArrJB = False
checkListJB = [ekimeiListJB, checkDepJB, checkArrJB]
ekimeiListJY = ekimeiJY.readline().replace('\n', '').split(',')
checkDepJY = False
checkArrJY = False
checkListJY = [ekimeiListJY, checkDepJY, checkArrJY]
ekimeiListList = [ekimeiListJB, ekimeiListJY]


idxJB = [0] # ekimeiJB のインデックス
idxJY = [0] # ekimeiJY のインデックス
iJB = 1 # matrixJB の行の初期値
jJB = 0 # matrixJB の列の初期値
iJY = 1 # matrixJY の行の初期値
jJY = 0 # matrixJY の列の初期値
searching = True
searchJB = True
searchJY = True


for checkList in [checkListJB, checkListJY]:
    #checkする入力とekimeiListの路線を合わせたい
    print(f'checkList <{checkList}>')
    checkList[1], checkList[2] = spd.checkInput(keyboard_dep, keyboard_arr, checkList[0])
    print(f'checkList[1] <{checkList[1]}>, checkList[2] <{checkList[2]}>')
    print(f'id(checkList[1]){id(checkList[1])}')
    print(f'id(checkList[2]){id(checkList[2])}')
    print(f'checkDepJB<{checkDepJB}>, checkArrJB<{checkArrJB}>, checkDepJY<{checkDepJY}>, checkArrJY<{checkArrJY}>')
    print(f'id(checkDepJB)<{id(checkDepJB)}>, id(checkArrJB)<{id(checkArrJB)}>, id(checkDepJY)<{id(checkDepJY)}>, id(checkArrJY)<{id(checkArrJY)}>')
    
print(f'checkDepJB<{checkDepJB}>, checkArrJB<{checkArrJB}>, checkDepJY<{checkDepJY}>, checkArrJY<{checkArrJY}>')
print(f'id(checkListJB[1]){id(checkListJB[1])}')
print(f'id(checkList[1]){id(checkList[1])}')
# デバッグ

if keyboard_arr == keyboard_dep:
    print('出発駅と到着駅が同じです')
    exit()

#出発駅の入力チェックとインデックスの初期化を同時に行う
if checkDepJB == True:
    iJB = ekimeiListJB.index(keyboard_dep)#出発駅の所属路線に中央・総武線を含む
    if checkDepJY == True:
        iJY = ekimeiListJY.index(keyboard_dep)#出発駅の所属路線は山手線、中央・総武線
    else:#出発駅の所属路線は中央・総武線のみ
        searchJY = False
else:
    searchJB = False
    if checkDepJY == True:
        iJY = ekimeiListJY.index(keyboard_dep)#出発駅の所属路線は山手線のみ
    else:
        print(f'{keyboard_dep}駅は存在しません')
        exit()

#到着駅の入力チェックと所属路線の検索を同時に行う
if checkArrJB == False:
    if checkArrJY == False:
        print(f'{keyboard_arr}駅は存在しません')
        exit()


permanentJB = {999999 : 999999} #キー:JBのインデックス、値:永久ラベル
permanent_indexJB = {999999 : 999999}#キー:JBのインデックス、値:JBの前の駅のインデックス
temporaryJB = {999999 : 999999} #キー:JBのインデックス、値:仮ラベル
temporary_indexJB = {999999 : 999999} #キー:JBのインデックス、値:JBの前の駅のインデックス
permanentJY = {999999 : 999999}
permanent_indexJY = {999999 : 999999}
temporaryJY = {999999 : 999999}
temporary_indexJY = {999999 : 999999}
route_reverse = [f'{keyboard_arr}'] #経路を到着駅から遡っていくので、最初の要素は到着駅
temporary_min = 0 #現在見つかっている中で、ある駅への最短所要時間を代入
temporary_minJB = None
temporary_minJY = None
label = 0


while searching == True:

    while searchJB == True:
        [iJB, jJB, idx, label, previous_idx] = spd.searchNextSta(iJB, jJB, matrixJB, label)
        print(f'iJB<{iJB}>, jJB<{iJB}>, idx<{idx}>, label<{label}>, previous_idx<{previous_idx}>')#デバッグ
        if idx == None:
            None
        elif idx not in temporaryJB:
            for ekimeiList in ekimeiListList.remove(ekimeiListJB): #駅名リスト一覧から現在の路線を消す
                lineStr, searchAfter, iAfter, tempIndexAfter, temporary, tempIndex, temp_min = spd.labelTrans(temporaryJB, idx, label, temporary_indexJB, previous_idx, temporary_minJB, trans_matrix, trans_stas, trans_lines, ekimeiList, ekimeiListJB, spd.lines.keys(), spd.lines, spd.trans)
                #仮の変数~Afterに代入した後、路線が何であるかを調べてからその路線のアルファベットが付いてる変数に代入する
                if lineStr == 'JY':
                    searchJY = searchAfter
                    iJY = iAfter
                    temporary_indexJY = tempIndexAfter
                    temporaryJB = temporary
                    temporary_indexJB = tempIndex
                    temporary_minJB = temp_min


    while searchJY == True:
        [iJY, iJY, idx, label, previous_idx] = spd.searchNextSta(iJY, jJY, matrixJY, label)
        if idx == None:
            None
        elif idx in temporaryJY:
            None
        elif idx not in permanentJY:#(閉路が存在して)既に永久ラベルが貼られている駅にきた場合、何もしない
            for ekimeiList in ekimeiListList.remove(ekimeiListJB):
                lineStr, searchAfter, iAfter, tempIndexAfter, temporary, tempIndex, temp_min = spd.labelTrans(temporaryJY, idx, label, temporary_indexJY, previous_idx, temporary_minJB, trans_matrix, trans_stas, trans_lines, ekimeiList, ekimeiListJY, spd.lines.keys(), spd.lines, spd.trans)
                if lineStr == 'JB':
                    searchJB = searchAfter
                    iJB = iAfter
                    temporary_indexJYJB = tempIndexAfter
                    temporaryJY = temporary
                    temporary_indexJY = tempIndex
                    temporary_minJY = temp_min


    if temporary_minJB == None:
        temporary_min = temporary_minJY
        #JBの最小ラベルが存在しない場合は必ずJYの最小ラベルが存在する
    elif temporary_minJY == None:
        temporary_min = temporary_minJB
        #JYの最小ラベルが存在しない場合は必ずJBの最小ラベルが存在する
    elif temporary_minJY < temporary_minJB:
        temporary_min = temporary_minJY
    else:
        temporary_min = temporary_minJB


    temporaryJB, permanentJB, temporary_indexJB, permanent_indexJB = spd.tempParma (temporaryJB, permanentJB, temporary_minJB, temporary_indexJB, permanent_indexJB)
    temporaryJY, permanentJY, temporary_indexJY, permanent_indexJY = spd.tempParma (temporaryJY, permanentJY, temporary_minJY, temporary_indexJY, permanent_indexJY)


    searchJB, route, num = spd.arrival (checkArrJB, ekimeiListJB, permanentJB, permanent_indexJB, searching, keyboard_arr)
    if route != None:
        for station_name in route:
            print(f'{station_name}')
        print(f'所要時間は{permanentJY[num]}分です')
        
    searchJB, route, num = spd.arrival (checkArrJY, ekimeiListJY, permanentJY, permanent_indexJY, searching, keyboard_arr)
    if route != None:
        for station_name in route:
            print(f'{station_name}')
        print(f'所要時間は{permanentJY[num]}分です')