# © 2021 ushita37

class Graph:
    def __init__(self, vSet, eSet) -> None:
        #アトリビュートを隠蔽
        self.__vertexSet = vSet
        self.__edgeSet = eSet

    # vertexSetのゲッター
    def getVertexSet(self):
        return self.__vertexSet

    # edgeSetのゲッター
    def getEdgeSet(self):
        return self.__edgeSet

    # vertexSetのセッター
    def setVertexSet(self, vs):
        self.__vertexSet = vs

    # edgeSetのセッター
    def setEdgeSet(self, es):
        self.__edgeSet = es

    vs = property(getVertexSet, setVertexSet)
    es = property(getEdgeSet, setEdgeSet)


    # ある点currentVに接続している辺edgeを全て探す
    def edgeJoinedToVertex(self, currentV):
        # 空リストを使い、print文で返す文字のリストを定義
        printList = []
        # edgeに辺集合の要素を次々代入
        for edge in self.es:
            if edge.includeCurrentVertex(currentV) == None:
                None
            # nvlアトリビュートは要素数が2のリストだから、どちらか片方が始点でもう片方は始点に隣接している点
            elif edge.nvl[0] != currentV:
                # printする文字列を追加
                printList.append(f"{currentV.vn}--->{edge.includeCurrentVertex(currentV).en}--->{edge.nvl[0].vn}")
            else:
                printList.append(f"{currentV.vn}--->{edge.includeCurrentVertex(currentV).en}--->{edge.nvl[1].vn}")
        return printList
            
    # 全ての点について、各々に接続している辺を全て探す
    def allEdgeJoinedToVertex(self):
        # 要素Noneを代入して、edgeJoinedToVertex()メソッドで得たprintListのリストを定義
        printListList = []
        for currentV in self.vs:
            printListList.append(self.edgeJoinedToVertex(currentV))
        return printListList






class Vertex:
    def __init__(self, vName) -> None:
        # 初期化で点の名前と仮/永久ラベルを代入するアトリビュートを定義
        self.__vertexName = vName
        self.__label = 0
        self.__permanentFlag = False
        self.__previousVertexName = ""
        
    # vertexNameのゲッター
    def getVertexName(self):
        return self.__vertexName

    # labelのゲッター
    def getLabel(self):
        return self.__label

    # permanentFlagのゲッター
    def getPermanentFlag(self):
        return self.__permanentFlag

    # previousVertexNameのゲッター
    def getPreviousVertexName(self):
        return self.__previousVertexName

    # vertexNameのセッター
    def setVertexName(self, vn):
        self.__vertexName = vn

    # labelのセッター
    # label = lb、出発地からの所要時間
    def setLabel(self, lb):
        self.__label = lb

    # permanentFlagのセッター
    # permanentFlagがTrueならばLabelは永久ラベル、Falseならば仮ラベル
    def setPermanentFlag(self, pf):
        self.__permanentFlag = pf

    # previousVertexNameのセッター
    def setPreviousVertexName(self, pvn):
        self.__previousVertexName = pvn

    vn = property(getVertexName, setVertexName)
    lb = property(getLabel, setLabel)
    pf = property(getPermanentFlag, setPermanentFlag)
    pvn = property(getPreviousVertexName, setPreviousVertexName)







class Edge:
    # 初期化で辺の名前と辺の重み、接続している点を代入するアトリビュートを定義
    def __init__(self, eName, eWeight, vList) -> None:
        # アトリビュートを隠蔽
        self.__edgeName = eName
        self.__edgeWeight = eWeight
        self.__nextVertexList = vList

    # edgeNameのゲッター
    def getEdgeName(self):
        return self.__edgeName

    # edgeWeightのゲッター
    def getEdgeWeight(self):
        return self.__edgeWeight

    # nextVertexListのゲッター
    def getNextVertexList(self):
        return self.__nextVertexList

    # edgeNameのセッター
    def setEdgeName(self, en):
        self.__edgeName = en

    # edgeWeightのセッター
    def setEdgeWeight(self, ew):
        self.__edgeWeight = ew

    # nextVertexのセッター
    def setNextVertexList(self, nvl):
        self.__nextVertexList = nvl


    en = property(getEdgeName, setEdgeName)
    ew = property(getEdgeWeight, setEdgeWeight)
    nvl = property(getNextVertexList, setNextVertexList)


    # 基点currentVを入力したらその辺に接続されているか判定し、接続されている場合はその辺自身を返すメソッド
    def includeCurrentVertex(self, currentV):
        if currentV in self.nvl:
            return self
        else:
            return None   






# inputされた点の文字列を点のインスタンスに変換
def searchInstanceFunc2(g, vName):
    v = None
    for vertex in g.vs:
        if vertex.vn == vName:
            v = vertex
    return v





def pasteTempLabel(edge, nvlIdx, currentVInstance, tempLabels):
    # 既にpermanentFlagが立っている点にはこれ以上ラベルを貼らない
    if edge.nvl[nvlIdx].pf == True:
        print(f"【{edge.nvl[nvlIdx].vn}のpermanentFlag = {edge.nvl[nvlIdx].pf}】")
    # まだラベルが貼られていない点にラベルを貼る
    elif edge.nvl[nvlIdx].lb == 0:
        print(f"{currentVInstance.vn}に隣接している点は{edge.nvl[nvlIdx].vn}")
        edge.nvl[nvlIdx].lb = edge.ew + currentVInstance.lb
        edge.nvl[nvlIdx].pvn = currentVInstance.vn
        tempLabels.append(edge.nvl[nvlIdx].lb)
        print(f"{edge.nvl[nvlIdx].vn}の仮ラベルは{edge.nvl[nvlIdx].lb}")
    # 既にラベルが貼られている点のラベルを貼り替える
    elif edge.nvl[nvlIdx].lb > edge.ew + currentVInstance.lb:
        print(f"{currentVInstance.vn}に隣接している点は{edge.nvl[nvlIdx].vn}")
        tempLabels.remove(edge.nvl[nvlIdx].lb)
        edge.nvl[nvlIdx].lb = edge.ew + currentVInstance.lb
        edge.nvl[nvlIdx].pvn = currentVInstance.vn
        tempLabels.append(edge.nvl[nvlIdx].lb)
        print(f"{edge.nvl[nvlIdx].vn}の仮ラベルは{edge.nvl[nvlIdx].lb}")
    # すでにラベルが貼ってあって、新たに貼ろうとしてるラベルがそれ以上ならラベルを上書きしない
    else:
        print(f"【{edge.nvl[nvlIdx].vn} ≦ {edge.ew + currentVInstance.lb}である】")
    return tempLabels






# 仮ラベル最小の点に永久ラベルを貼り、その点にcurrentVInstanceを変える関数の定義
def pasteNextLabel(g, currentVInstance, tempLabels):
    print(f"{g.edgeJoinedToVertex(currentVInstance)}")

    for edge in g.es:
        if edge.includeCurrentVertex(currentVInstance) != None:
            print(f"{currentVInstance.vn}に接続している辺は{edge.includeCurrentVertex(currentVInstance).en}")
            # nvlアトリビュートは要素数が2のリストだから、どちらか片方がpermanentFlagが立っている基点で、
            # もう片方はpermanentFlagが立っていない基点に隣接している点
            if edge.nvl[0] != currentVInstance:
                tempLabels = pasteTempLabel(edge, 0, currentVInstance, tempLabels)
            else:
                tempLabels = pasteTempLabel(edge, 1, currentVInstance, tempLabels)
    
    tempLabels.sort()
    print(tempLabels)

    # ある点の仮ラベルがtempLabelsの最小であるか判定する
    for vertex in g.vs:
        # tempLabelsの最小と比較、tempLabelの最小値に等しく既に永久ラベルが貼られた点は除外する
        if vertex.lb == tempLabels[0] and vertex.pf == False:
            vertex.pf = True
            tempLabels.remove(vertex.lb)
            print(f"{vertex.vn}には永久ラベル{vertex.lb}が貼られています")
            #vertex.pvn = currentVInstance.vn
            print(f"vertex={vertex.vn}, previousVertex={currentVInstance.vn}")
            currentVInstance = vertex
            # 1セットのループで見つける永久ラベルは1個まで、永久ラベルが見つかったら以降のforループは中止して、
            # 永久ラベルを貼った点を基点に、その基点に隣接している点とその仮ラベルを探す
            break

    return currentVInstance, tempLabels



