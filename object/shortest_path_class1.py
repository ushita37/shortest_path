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
        
    # vertexNameのゲッター
    def getVertexName(self):
        return self.__vertexName

    # labelのゲッター
    def getLabel(self):
        return self.__label

    # permanentFlagのゲッター
    def getPermanentFlag(self):
        return self.__permanentFlag

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

    vn = property(getVertexName, setVertexName)
    lb = property(getLabel, setLabel)
    pf = property(getPermanentFlag, setPermanentFlag)






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






# inputされた始点の文字列、終点の文字列をそれぞれ始点のインスタンス、終点のインスタンスに変換
def searchInstanceFunc(initialVInput, finalVInput, g):
    initialVInstance = None
    finalVInstance = None
    for vertex in g.vs:
        if vertex.vn == initialVInput:
            initialVInstance = vertex
        elif vertex.vn == finalVInput:
            finalVInstance = vertex
    # inputが正しければ、forループを回した後はinitialVInstance,finalVInstance共にNone以外の値になっている
    # inputが不正ならば、forループを回した後もinitialVinstance,finalVInstanceの少なくとも一方はNoneになっている
    return initialVInstance, finalVInstance






# 仮ラベル最小の点に永久ラベルを貼り、その点にcurrentVInstanceを変える関数の定義
def pasteNextLabel(g, currentVInstance, tempLabels):
    print(f"{g.edgeJoinedToVertex(currentVInstance)}")

    for edge in g.es:
        if edge.includeCurrentVertex(currentVInstance) != None:
            print(f"{currentVInstance.vn}に接続している辺は{edge.includeCurrentVertex(currentVInstance).en}")
            # nvlアトリビュートは要素数が2のリストだから、どちらか片方がpermanentFlagが立っている基点で、
            # もう片方はpermanentFlagが立っていない基点に隣接している点

            if edge.nvl[0] != currentVInstance:
                # 既にpermanentFlagが立っている点にはこれ以上ラベルを貼らない
                if edge.nvl[0].pf == True:
                    print(f"【{edge.nvl[0].vn}のpermanentFlag = {edge.nvl[0].pf}】")
                # まだラベルが貼られていない点にラベルを貼る
                elif edge.nvl[0].lb == 0:
                    print(f"{currentVInstance.vn}に隣接している点は{edge.nvl[0].vn}")
                    edge.nvl[0].lb = edge.ew + currentVInstance.lb
                    tempLabels.append(edge.nvl[0].lb)
                    print(f"{edge.nvl[0].vn}の仮ラベルは{edge.nvl[0].lb}")
                # 既にラベルが貼られている点のラベルを貼り替える
                elif edge.nvl[0].lb > edge.ew + currentVInstance.lb:
                    print(f"{currentVInstance.vn}に隣接している点は{edge.nvl[0].vn}")
                    tempLabels.remove(edge.nvl[0].lb)
                    edge.nvl[0].lb = edge.ew + currentVInstance.lb
                    tempLabels.append(edge.nvl[0].lb)
                    print(f"{edge.nvl[0].vn}の仮ラベルは{edge.nvl[0].lb}")
                # すでにラベルが貼ってあって、新たに貼ろうとしてるラベルがそれ以上ならラベルを上書きしない
                else:
                    print(f"【{edge.nvl[0].vn} ≦ {edge.ew + currentVInstance.lb}である】")

            else:
                # 既にpermanentFlagが立っている点にはこれ以上ラベルを貼らない
                if edge.nvl[1].pf == True: 
                    print(f"【{edge.nvl[1].vn}のpermanentFlag = {edge.nvl[1].pf}】")
                # まだラベルが貼られていない点にラベルを貼る
                elif edge.nvl[1].lb == 0:
                    print(f"{currentVInstance.vn}に隣接している点は{edge.nvl[1].vn}")
                    edge.nvl[1].lb = edge.ew + currentVInstance.lb
                    tempLabels.append(edge.nvl[1].lb)
                    print(f"{edge.nvl[1].vn}の仮ラベルは{edge.nvl[1].lb}")
                # 既にラベルが貼られている点のラベルを貼り替える
                elif edge.nvl[1].lb > edge.ew + currentVInstance.lb:
                    print(f"{currentVInstance.vn}に隣接している点は{edge.nvl[1].vn}")
                    tempLabels.remove(edge.nvl[1].lb)
                    edge.nvl[1].lb = edge.ew + currentVInstance.lb
                    tempLabels.append(edge.nvl[1].lb)
                    print(f"{edge.nvl[1].vn}の仮ラベルは{edge.nvl[1].lb}")
                # すでにラベルが貼ってあって、新たに貼ろうとしてるラベルがそれ以上ならラベルを上書きしない
                else:
                    print(f"【{edge.nvl[1].vn} ≦ {edge.ew + currentVInstance.lb}である】")
        
    
    tempLabels.sort()
    print(tempLabels)

    # ある点のラベルがtempLabelsの最小であるか判定する
    for vertex in g.vs:
        # tempLabelsの最小と比較
        if vertex.lb == tempLabels[0]:
            vertex.pf = True
            tempLabels.remove(vertex.lb)
            print(f"{vertex.vn}には永久ラベル{vertex.lb}が貼られています")
            # 1セットのループで見つける永久ラベルは1個まで、永久ラベルが見つかったら以降のforループは中止して、
            # 永久ラベルを貼った点を基点に、その基点に隣接している点とその仮ラベルを探す
            currentVInstance = vertex
            break

    return currentVInstance, tempLabels
            