# © 2021 ushita37

initialVertexInput = input("始点を入力してください>")
finalVertexInput = input("終点を入力してください>")


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

    # inputされた始点の文字列、終点の文字列をそれぞれ始点のインスタンス、終点のインスタンスに変換
    def searchInstanceFromInput(self):
        initialVInstance = None
        finalVInstance = None
        for vertex in self.vs:
            if vertex.vn == initialVertexInput:
                initialVInstance = vertex
            elif vertex.vn == finalVertexInput:
                finalVInstance = vertex
        # inputが正しければ、forループを回した後はinitialVInstance,finalVInstance共にNone以外の値になっている
        # inputが不正ならば、forループを回した後もinitialVinstance,finalVInstanceの少なくとも一方はNoneになっている
        return initialVInstance, finalVInstance
            





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





vA = Vertex("vA")
# 点の名前をプリント
# print (vA.vn)
vB = Vertex("vB")
vC = Vertex("vC")
vD = Vertex("vD")
vE = Vertex("vE")
vF = Vertex("vF")
vG = Vertex("vG")
vH = Vertex("vH")
vI = Vertex("vI")
vJ = Vertex("vJ")
vK = Vertex("vK")
vL = Vertex("vL")


e1 = Edge("e1", 3, [vA, vB])
e2 = Edge("e2", 9, [vA, vE])
e3 = Edge("e3", 2, [vA, vC])
e4 = Edge("e4", 2, [vB, vD])
e5 = Edge("e5", 4, [vB, vE])
e6 = Edge("e6", 6, [vC, vE])
e7 = Edge("e7", 9, [vC, vF])
e8 = Edge("e8", 3, [vD, vG])
e9 = Edge("e9", 1, [vE, vG])
e10 = Edge("e10", 2, [vE, vH])
e11 = Edge("e11", 1, [vF, vH]) 
e12 = Edge("e12", 2, [vF, vI])
e13 = Edge("e13", 5, [vG, vJ])
e14 = Edge("e14", 5, [vH, vJ])
e15 = Edge("e15", 9, [vH, vL])
e16 = Edge("e16", 6, [vH, vK])
e17 = Edge("e17", 2, [vI, vK])
e18 = Edge("e18", 5, [vJ, vL])
e19 = Edge("e19", 3, [vK, vL])





# 全ての点と辺を定義してから点集合と辺集合とグラフを作る
vSet = {vA, vB, vC, vD, vE, vF, vG, vH, vI, vJ, vK, vL}
eSet = {e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19}

gGraph = Graph(vSet, eSet)



# 全ての点について、接続している辺をプリント
#for list in gGraph.allEdgeJoinedToVertex():
#    for printStr in list:
#        print(printStr)




# inputされた文字列からVertexインスタンスへの変換
initialVertexInstance, finalVertexInstance = gGraph.searchInstanceFromInput()
# inputチェック
if initialVertexInstance == None:
    print("始点の入力が不正です")
    exit
elif finalVertexInstance == None:
    print("終点の入力が不正です")
    exit


# 仮ラベルの値を入れるリストを定義
temporaryLabels = []
# 経路を探していく途中で現在地の点のインスタンスを保存する
currentVertexInstance = None


initialVertexInstance.lb = 0
initialVertexInstance.pf = True
print(f"{initialVertexInstance.vn}には永久ラベル{initialVertexInstance.lb}が貼られています")







print(f"{gGraph.edgeJoinedToVertex(initialVertexInstance)}")

for edge in gGraph.es:
    if edge.includeCurrentVertex(initialVertexInstance) != None:
        print(f"{initialVertexInstance.vn}に接続している辺は{edge.includeCurrentVertex(initialVertexInstance).en}")
        # nvlアトリビュートは要素数が2のリストだから、どちらか片方が始点でもう片方は始点に隣接している点
        if edge.nvl[0] != initialVertexInstance:
            print(f"{initialVertexInstance.vn}に隣接している点は{edge.nvl[0].vn}")
            # 隣接している点にラベルを貼る
            edge.nvl[0].lb = edge.ew
            print(f"{edge.nvl[0].vn}の仮ラベルは{edge.nvl[0].lb}")
            # 始点に隣接している点で.pf == Trueとなっているか、既にtemporaryLabelsに値が追加されている点は存在しないので、
            # temporaryLabelsの重複とpfのチェックは省略
            temporaryLabels.append(edge.nvl[0].lb)
        else:
            print(f"{initialVertexInstance.vn}に隣接している点は{edge.nvl[1].vn}")
            edge.nvl[1].lb = edge.ew
            print(f"{edge.nvl[1].vn}の仮ラベルは{edge.nvl[1].lb}")
            temporaryLabels.append(edge.nvl[1].lb)
            
temporaryLabels.sort()
print(temporaryLabels)

# ある点のラベルがtemporaryLabelsの最小であるか判定する
for vertex in gGraph.vs:
    # temporaryLabelsの最小と比較
    if vertex.lb == temporaryLabels[0]:
        vertex.pf = True
        temporaryLabels.remove(vertex.lb)
        print(f"{vertex.vn}には永久ラベル{vertex.lb}が貼られています")
        # 1セットのループで見つける永久ラベルは1個まで、永久ラベルが見つかったら以降のforループは中止して、
        # 永久ラベルを貼った点を基点に、その基点に隣接している点とその仮ラベルを探す
        currentVertexInstance = vertex
        break









while currentVertexInstance != finalVertexInstance:
    print(f"{gGraph.edgeJoinedToVertex(currentVertexInstance)}")

    for edge in gGraph.es:
        if edge.includeCurrentVertex(currentVertexInstance) != None:
            print(f"{currentVertexInstance.vn}に接続している辺は{edge.includeCurrentVertex(currentVertexInstance).en}")
            # nvlアトリビュートは要素数が2のリストだから、どちらか片方がpermanentFlagが立っている基点で、
            # もう片方はpermanentFlagが立っていない基点に隣接している点

            if edge.nvl[0] != currentVertexInstance:
                # 既にpermanentFlagが立っている点にはこれ以上ラベルを貼らない
                if edge.nvl[0].pf == True:
                    print(f"【{edge.nvl[0].vn}のpermanentFlag = {edge.nvl[0].pf}】")
                # まだラベルが貼られていない点にラベルを貼る
                elif edge.nvl[0].lb == 0:
                    print(f"{currentVertexInstance.vn}に隣接している点は{edge.nvl[0].vn}")
                    edge.nvl[0].lb = edge.ew + currentVertexInstance.lb
                    temporaryLabels.append(edge.nvl[0].lb)
                    print(f"{edge.nvl[0].vn}の仮ラベルは{edge.nvl[0].lb}")
                # 既にラベルが貼られている点のラベルを貼り替える
                elif edge.nvl[0].lb > edge.ew + currentVertexInstance.lb:
                    print(f"{currentVertexInstance.vn}に隣接している点は{edge.nvl[0].vn}")
                    temporaryLabels.remove(edge.nvl[0].lb)
                    edge.nvl[0].lb = edge.ew + currentVertexInstance.lb
                    temporaryLabels.append(edge.nvl[0].lb)
                    print(f"{edge.nvl[0].vn}の仮ラベルは{edge.nvl[0].lb}")
                # すでにラベルが貼ってあって、新たに貼ろうとしてるラベルがそれ以上ならラベルを上書きしない
                else:
                    print(f"【{edge.nvl[0].vn} ≦ {edge.ew + currentVertexInstance.lb}である】")

            else:
                # 既にpermanentFlagが立っている点にはこれ以上ラベルを貼らない
                if edge.nvl[1].pf == True: 
                    print(f"【{edge.nvl[1].vn}のpermanentFlag = {edge.nvl[1].pf}】")
                # まだラベルが貼られていない点にラベルを貼る
                elif edge.nvl[1].lb == 0:
                    print(f"{currentVertexInstance.vn}に隣接している点は{edge.nvl[1].vn}")
                    edge.nvl[1].lb = edge.ew + currentVertexInstance.lb
                    temporaryLabels.append(edge.nvl[1].lb)
                    print(f"{edge.nvl[1].vn}の仮ラベルは{edge.nvl[1].lb}")
                # 既にラベルが貼られている点のラベルを貼り替える
                elif edge.nvl[1].lb > edge.ew + currentVertexInstance.lb:
                    print(f"{currentVertexInstance.vn}に隣接している点は{edge.nvl[1].vn}")
                    temporaryLabels.remove(edge.nvl[1].lb)
                    edge.nvl[1].lb = edge.ew + currentVertexInstance.lb
                    temporaryLabels.append(edge.nvl[1].lb)
                    print(f"{edge.nvl[1].vn}の仮ラベルは{edge.nvl[1].lb}")
                # すでにラベルが貼ってあって、新たに貼ろうとしてるラベルがそれ以上ならラベルを上書きしない
                else:
                    print(f"【{edge.nvl[1].vn} ≦ {edge.ew + currentVertexInstance.lb}である】")
        
    
    temporaryLabels.sort()
    print(temporaryLabels)

    # ある点のラベルがtemporaryLabelsの最小であるか判定する
    for vertex in gGraph.vs:
        # temporaryLabelsの最小と比較
        if vertex.lb == temporaryLabels[0]:
            vertex.pf = True
            temporaryLabels.remove(vertex.lb)
            print(f"{vertex.vn}には永久ラベル{vertex.lb}が貼られています")
            # 1セットのループで見つける永久ラベルは1個まで、永久ラベルが見つかったら以降のforループは中止して、
            # 永久ラベルを貼った点を基点に、その基点に隣接している点とその仮ラベルを探す
            currentVertexInstance = vertex
            break





if finalVertexInstance.pf == True:
    print(f"所要時間は{finalVertexInstance.lb}です")