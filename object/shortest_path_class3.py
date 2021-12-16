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


    # inputされた点の文字列を点のインスタンスに変換
    def searchInstance(self, vName):
        v = None
        for vertex in self.vs:
            if vertex.vn == vName:
                v = vertex
        return v

    # 仮ラベル最小の点に永久ラベルを貼り、その点を新たな起点とするメソッドの定義
    def findMin(self, previousV, tempLabels):
        for edge in self.es:
            # その辺edgeに起点previousVが接続しているかどうか
            if edge.includePreviousVertex(previousV) == None:
                pass
            # nvlアトリビュートは要素数が2のリストだから、どちらか片方がpermanentFlag=Trueとなっている起点Vpで、
            # もう片方はVpに隣接していてpermanentFlag=Falseとなっている点
            # 仮ラベルの値一覧tempLabelsを更新
            elif edge.nvl[0] != previousV:
                tempLabels = edge.pasteTemporary(0, previousV, tempLabels)
            else:
                tempLabels = edge.pasteTemporary(1, previousV, tempLabels)
        tempLabels.sort()

        # ある点の仮ラベルがtempLabelsの最小であるか判定する
        for vertex in self.vs:
            # tempLabelsの最小と比較、tempLabelの最小値に等しく既に永久ラベルが貼られた点は除外する
            if vertex.lb == tempLabels[0] and vertex.pf == False:
                vertex.pf = True
                tempLabels.remove(vertex.lb)
                previousV = vertex
                # 1セットのループで見つける永久ラベルは1個まで、永久ラベルが見つかったら以降のforループは中止して、
                # 永久ラベルを貼った点を起点に、その起点に隣接している点とその仮ラベルを探す
                break

        return previousV, tempLabels




class Vertex:
    def __init__(self, vName) -> None:
        # 初期化で点の名前と仮/永久ラベルを代入するアトリビュートを定義
        self.__vertexName = vName
        self.__label = 0
        self.__permanentFlag = False
        self.__previousVertexName = ""
        self.__previousEdgeName = ""
        
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

    # previousEdgeNameのゲッター
    def getPreviousEdgeName(self):
        return self.__previousEdgeName

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
    # previousVertexはある点Vの起点Vpの名前
    def setPreviousVertexName(self, pvn):
        self.__previousVertexName = pvn

    # previousEdgeNameのセッター
    # previousEdgeNameはVとVpをつなぐ辺Epの名前
    def setPreviousEdgeName(self, pen):
        self.__previousEdgeName = pen

    vn = property(getVertexName, setVertexName)
    lb = property(getLabel, setLabel)
    pf = property(getPermanentFlag, setPermanentFlag)
    pvn = property(getPreviousVertexName, setPreviousVertexName)
    pen = property(getPreviousEdgeName, setPreviousEdgeName)




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


    # 起点previousVを入力したらその辺に接続されているか判定し、接続されている場合はその辺自身を返すメソッド
    def includePreviousVertex(self, previousV):
        if previousV in self.nvl:
            return self
        else:
            return None   

    # 仮ラベルを貼るメソッド
    def pasteTemporary(self, nvlIdx, previousV, tempLabels):
        if self.nvl[nvlIdx].pf == True:
            pass
        # まだラベルが貼られていない点に、新たにラベルself.ew + previousV.lbを貼る
        elif self.nvl[nvlIdx].lb == 0:
            self.nvl[nvlIdx].lb = self.ew + previousV.lb
            self.nvl[nvlIdx].pvn = previousV.vn
            self.nvl[nvlIdx].pen = self.en
            tempLabels.append(self.nvl[nvlIdx].lb)
        # 新たに貼ろうとしてるラベルが、既に貼られているラベルself.nvl[nvlIdx].lb未満なら、ラベルを張り替える
        elif self.nvl[nvlIdx].lb > self.ew + previousV.lb:
            tempLabels.remove(self.nvl[nvlIdx].lb)
            self.nvl[nvlIdx].lb = self.ew + previousV.lb
            self.nvl[nvlIdx].pvn = previousV.vn
            self.nvl[nvlIdx].pen = self.en
            tempLabels.append(self.nvl[nvlIdx].lb)
        # 新たに貼ろうとしてるラベルが、既に貼られているラベル以上なら、何もしない
        return tempLabels









