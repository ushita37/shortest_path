# © 2021 ushita37
# 失敗作

YAMANOTE = 2350
CHUOSOBU = 2315
lines = {'JB':CHUOSOBU, 'JY':YAMANOTE}


#入力をチェック
def checkInput(inputDep, inputArr, ekimeiList):
    #inputDepとinputArrに対して行う処理は同じだが、for文を減らすために同じ関数内で似たコードを2回かく
    if inputDep in ekimeiList:
        existDep = True
    else:
        existDep = False
    if inputArr in ekimeiList:
        existArr = True
    else:
        existArr = False
    return [existDep, existArr]


#行列を使って隣の駅を探す
def searchNextSta(i, j, matrix, label):
    plus_minute = 0
    index = None
    previous_index = None
    matrix_len = len(matrix[i])
    if matrix[i, j] == 9999:
        None
    elif matrix[i, j] == 999999:
        None
    elif matrix[i, j] > 0:
        plus_minute = matrix[i, j]
        index = j
        previous_index = i #1つ前の駅のインデックス
    elif matrix[i, j] < 0:
        plus_minute = abs(matrix[i, j])
        index = j
        previous_index = i
    else:
        None
    j = j + 1
    if j >= matrix_len:#最後の列まで調べたら次の行に移る
        i += 1
        j = 0
    label += plus_minute#その駅までの所要時間
    return [i, j, index, label, previous_index]


#乗換駅に接続してる路線と、その路線における乗換駅のインデックスを探す
def trans(transMatrix, transStas, transLines, current_sta):
    if current_sta in transStas:
        maybeTransNumberings = [999999]
        canTransNumberings = [999999]
        canTransLines = [999999]
        for line in transLines[1:]:#最初の要素は代入しない
            maybeTransNumberings += [transMatrix[transLines.index(line)][transStas.index(current_sta)]]
            #matrix上のcurrent_staが入っている行の要素をリストで代入
            #2次元配列の要素を指定
        for line in transLines[1:]:
            for numbering in maybeTransNumberings:
                if numbering != 0:
                    canTransNumberings += [numbering]
                    canTransLines += [line]
                    #canTransNumberingsとcanTransLinesの並び順は対応している
        del canTransLines[0]
        del canTransNumberings[0]
    else:
        canTransNumberings = [None]
        canTransLines = [None]
    return [canTransNumberings, canTransLines]


#経路を探す
def route(permanent_index, ekimeiList, num, keyboardDep, keyboardArr, ekimeiList1, permaIndex1, CONSTANT1, ekimeiList2, permaIndex2, CONSTANT2):
    route_reverse = [keyboardArr]
    routing = True
    while routing == True:
        for previous_index in permanent_index[num]:
            if previous_index == CONSTANT1:
                current_ekimei = ekimeiList[num]
                num = ekimeiList1.index(current_ekimei)
                permanent_index = permaIndex1
                break
            elif previous_index == CONSTANT2:
                current_ekimei = ekimeiList[num]
                num = ekimeiList2.index(current_ekimei)
                permanent_index = permaIndex2
                break
            else:
                route_reverse += ekimeiList[previous_index]
                if keyboardDep in route_reverse:
                    routing = False                
                num = permanent_index[num]
                break
    return [route_reverse]


#目的地に到着したか調べる
def arrival (checkArr, ekimeiList, permanent, permanent_index, search, keyboardArr):
    if checkArr == True:
        routeRev = None
    elif ekimeiList.index(keyboardArr) in permanent.keys():
        num = ekimeiList.index(keyboardArr)
        search = False
        routeRev = route(permanent_index, ekimeiList, num)
        return [search, routeRev.sort(reverse=True), num]


#仮ラベルを永久ラベルにする
def tempParma(temporary, permanent, temp_min, tempIndex, permaIndex):
    for rowColumn in temporary.items():
        if rowColumn[0] in permanent: #既に存在する永久ラベルの書き換え防止、キー(インデックス)の存在確認
            None
        elif rowColumn[1] == temp_min:
            permanent[rowColumn[0]] = rowColumn[1]
            del temporary[rowColumn[0]] #永久ラベルに格上げしたものは仮ラベルの辞書から削除
            permaIndex[rowColumn[0]] = tempIndex[rowColumn[0]]
            return [temporary, permanent, tempIndex, permaIndex]


#見つかった隣駅に仮ラベルを貼り、その隣駅が乗換駅かどうか調べる
def labelTrans(temporary, index, label, tempIndex, preIndex, temp_min, transMatrix, transStas, transLines, ekiListTrans, currentLine, linesKeys, linesdict, transfunc):
    #linekeys:辞書linesのキー(路線名を表すアルファベット2文字)
    temporary[index] = label
    print(f'temporary.values <{temporary.values}>') #デバッグ
    print(index) #デバッグ
    tempIndex[index] = preIndex
    temp_min = min(temporary.values()) #仮ラベルの中で最小のものを見つける
    [canTransNums, canTransLines] = transfunc(transMatrix, transStas, transLines, ekiListTrans[index])
    print(f'canTransNums <{canTransNums}>, canTransLines <{canTransLines}>') #デバッグ
    if canTransLines[0] == None:
        return[None, None, None, None, temporary, tempIndex, temp_min]
    else:
        for lineStr in linesKeys.remove(currentLine): #自身を除く路線一覧を代入
            if lineStr in canTransLines: #それぞれの路線が、乗り換え可能な路線を表すstrに含まれているか否か
                searchAfter = True
                iAfter = canTransNums[canTransLines.index(lineStr)]
                tempIndexAfter = {iAfter: linesdict[lineStr]}
                return [lineStr, searchAfter, iAfter, tempIndexAfter, temporary, tempIndex, temp_min]

            else:
                return[None, None, None, None, temporary, tempIndex, temp_min]

                



