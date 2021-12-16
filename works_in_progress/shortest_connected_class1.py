# © 2021 ushita37
# 開発中

class Graph:
    def __init__(self, subgSet, bSet) -> None:
        # アトリビュートを隠蔽
        self.__subGraphSet = subgSet
        self.__bridgeSet = bSet

    # subGraphSetのゲッター
    def getSubGraphSet(self):
        return self.__subGraphSet

    # bridgeSetのゲッター
    def getBridgeSet(self):
        return self.__bridgeSet

    # subGraphSetのセッター
    def setSubGraphSet(self, subgs):
        self.__subGraphSet = subgs

    # bridgeSetのセッター
    def setBridgeSet(self, bs):
        self.__bridgeSet = bs

    subgs = property(getSubGraphSet, setSubGraphSet)
    bs = property(getBridgeSet, setBridgeSet)

    # inputされた点の文字列からグラフと点のインスタンスをそれぞれ返す
    def searchInstance(self, inputVertexName):
        subg, v = None, None
        for subGraph in self.subgs:
            if subGraph.searchInstance(inputVertexName) != None:
                subg = subGraph
                v = subGraph.searchInstance(inputVertexName)
        return subg, v

    # 現在の点がグラフの接続点かどうか判定して、接続点ならば部分グラフを移す
    def junction(self, currentSubG):
        currentSubG = None
        for bridge in self.subgs:
            if currentV == bridge.jl[0]:
                # 接続している部分グラフのインスタンスを代入
                currentSubG = bridge.sgl[1]
                # 接続先での部分グラフにおける接続点のインスタンスを代入
                currentV = bridge.jl[1]
        



class Bridge:
    # bridgeNameはグラフとグラフをつなぐ橋の名前
    # bridgeWeightは将来路線ごとにグラフを作った際、グラフを移るのに必要な乗り換え時間として使うかもしれないが今は保留
    # gListは互いにつながっている2つのグラフのリスト
    # jListは所属する部分グラフが異なるが同じ接続点を表す2点のリスト
    def __init__(self, igName, igWeight, subgList, jList) -> None:
        # アトリビュートを隠蔽
        self.__bridgeName = igName
        self.__bridgeWeight = igWeight
        self.__subGraphList = subgList
        self.__junctionList = jList
    
    # bridgeNameのゲッター
    def getBridgeName(self):
        return self.__bridgeName

    # bridgeSetのゲッター
    def getBridgeWeight(self):
        return self.__bridgeWeight

    # subGraphListのゲッター
    def getSubGraphList(self):
        return self.__subGraphList

    # jinctionListのゲッター
    def getJunctionList(self):
        return self.__junctionList

    # bridgeNameのセッター
    def setBridgeName(self, ign):
        self.__bridgeName = ign

    # bridgeWeightのセッター
    def setBridgeWeight(self, igw):
        self.__bridgeWeight = igw

    # subGraphListのセッター
    def setSubGraphList(self, sgl):
        self.__subGraphList = sgl

    # jnctionListのセッター
    def setJunctionList(self, jl):
        self.__junctionList = jl

    ign = property(getBridgeName, setBridgeName)
    igw = property(getBridgeWeight, setBridgeWeight)
    sgl = property(getSubGraphList, setSubGraphList)
    jl = property(getJunctionList, setJunctionList)





# 一つの大きなGraphの中の要素SubGraphを定義
class SubGraph:
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

    # inputされた点の文字列を点のインスタンスに変換
    def searchInstance(self, vName):
        v = None
        for vertex in self.vs:
            if vertex.vn == vName:
                v = vertex
        return v

    # 仮ラベル最小の点に永久ラベルを貼り、その点にcurrentVを移すメソッドの定義
    def pasteNext(self, currentV, tempLabels):
        print(f"{self.edgeJoinedToVertex(currentV)}")

        for edge in self.es:
            if edge.includeCurrentVertex(currentV) != None:
                print(f"{currentV.vn}に接続している辺は{edge.includeCurrentVertex(currentV).en}")
                # nvlアトリビュートは要素数が2のリストだから、どちらか片方がpermanentFlagが立っている基点で、
                # もう片方はpermanentFlagが立っていない基点に隣接している点
                if edge.nvl[0] != currentV:
                    tempLabels = edge.pasteTemporary(0, currentV, tempLabels)
                else:
                    tempLabels = edge.pasteTemporary(1, currentV, tempLabels)
            
        tempLabels.sort()
        print(tempLabels)

        # ある点の仮ラベルがtempLabelsの最小であるか判定する
        for vertex in self.vs:
            # tempLabelsの最小と比較、tempLabelの最小値に等しく既に永久ラベルが貼られた点は除外する
            if vertex.lb == tempLabels[0] and vertex.pf == False:
                vertex.pf = True
                tempLabels.remove(vertex.lb)
                print(f"{vertex.vn}には永久ラベル{vertex.lb}が貼られています")
                #vertex.pvn = currentV.vn
                print(f"vertex={vertex.vn}, previousVertex={currentV.vn}")
                currentV = vertex
                # 1セットのループで見つける永久ラベルは1個まで、永久ラベルが見つかったら以降のforループは中止して、
                # 永久ラベルを貼った点を基点に、その基点に隣接している点とその仮ラベルを探す
                break

        return currentV, tempLabels







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

    # nextVertexListのセッター
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

    # 仮ラベルを貼るメソッド
    def pasteTemporary(self, nvlIdx, currentV, tempLabels):
        if self.nvl[nvlIdx].pf == True:
            print(f"【{self.nvl[nvlIdx].vn}のpermanentFlag = {self.nvl[nvlIdx].pf}")
        elif self.nvl[nvlIdx].lb == 0:
            print(f"{currentV.vn}に隣接している点は{self.nvl[nvlIdx].vn}")
            self.nvl[nvlIdx].lb = self.ew + currentV.lb
            self.nvl[nvlIdx].pvn = currentV.vn
            tempLabels.append(self.nvl[nvlIdx].lb)
            print(f"{self.nvl[nvlIdx].vn}の仮ラベルは{self.nvl[nvlIdx].lb}")
        # 既にラベルが貼られている点のラベルを貼り替える
        elif self.nvl[nvlIdx].lb > self.ew + currentV.lb:
            print(f"{currentV.vn}に隣接している点は{self.nvl[nvlIdx].vn}")
            tempLabels.remove(self.nvl[nvlIdx].lb)
            self.nvl[nvlIdx].lb = self.ew + currentV.lb
            self.nvl[nvlIdx].pvn = currentV.vn
            tempLabels.append(self.nvl[nvlIdx].lb)
            print(f"{self.nvl[nvlIdx].vn}の仮ラベルは{self.nvl[nvlIdx].lb}")
        # すでにラベルが貼ってあって、新たに貼ろうとしてるラベルがそれ以上ならラベルを上書きしない
        else:
            print(f"【{self.nvl[nvlIdx].vn} ≦ {self.ew + currentV.lb}である】")
        return tempLabels

