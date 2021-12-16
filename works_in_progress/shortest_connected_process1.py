# © 2021 ushita37
# 開発中

import sys
import shortest_connected_class1 as scc1

initialVertexInput = input("始点を入力してください>")
finalVertexInput = input("終点を入力してください>")

g6vA = scc1.Vertex("g6vA")
g6vB = scc1.Vertex("g6vB")
g6vC = scc1.Vertex("g6vC")
g6vD = scc1.Vertex("g6vD")
g6vE = scc1.Vertex("g6vE")
g6vF = scc1.Vertex("g6vF")

g7vA = scc1.Vertex("g7vA")
g7vB = scc1.Vertex("g7vB")
g7vC = scc1.Vertex("g7vc")
g7vD = scc1.Vertex("g7vD")
g7vE = scc1.Vertex("g7vE")
g7vF = scc1.Vertex("g7vF")

g6e1 = scc1.Edge("g6e1", 2, [g6vA, g6vB])
g6e2 = scc1.Edge("g6e2", 2, [g6vB, g6vC])
g6e3 = scc1.Edge("g6e3", 3, [g6vC, g6vD])
g6e4 = scc1.Edge("g6e4", 1, [g6vD, g6vE])
g6e5 = scc1.Edge("g6e5", 7, [g6vB, g6vE])
g6e6 = scc1.Edge("g6e6", 6, [g6vE, g6vF])
g6e7 = scc1.Edge("g6e7", 6, [g6vD, g6vF])

g7e1 = scc1.Edge("g7e1", 7, [g7vA, g7vB])
g7e2 = scc1.Edge("g7e2", 3, [g7vB, g7vC])
g7e3 = scc1.Edge("g7e3", 2, [g7vC, g7vD])
g7e4 = scc1.Edge("g7e4", 5, [g7vB, g7vE])
g7e5 = scc1.Edge("g7v5", 8, [g7vC, g7vE])
g7e6 = scc1.Edge("g7e6", 1, [g7vE, g7vF])




# 全ての点と辺を定義してから点集合と辺集合とグラフを作り、
# その後グラフの接続に関する情報Bridgeを作る
g6vSet = {g6vA, g6vB, g6vC, g6vD, g6vE, g6vF}
g7vSet = {g7vA, g7vB, g7vC, g7vD, g7vE, g7vF}

g6eSet = {g6e1, g6e2, g6e3, g6e4, g6e5, g6e6, g6e7}
g7eSet = {g7e1, g7e2, g7e3, g7e4, g7e5, g7e6}

g6 = scc1.SubGraph(g6vSet, g6eSet)
g7 = scc1.SubGraph(g7vSet, g7eSet)
subgSet = {g6, g7}
bg6g7 = scc1.Bridge("bg6g7", 0, [g6, g7], [g6vF, g7vA])
bSet = {bg6g7}

g = scc1.Graph(subgSet,bSet)


# 始点と終点が入ってる部分グラフとそれぞれの点のインスタンスを探す
initialSubGraphInstance, initialVertexInstance = g.searchInstance(initialVertexInput)
finalSubGraphInstance, finalVertexInstance = g.searchInstance(finalVertexInput)
# inputチェック
if initialVertexInstance == None:
    print("始点の入力が不正です")
    sys.exit()
elif finalVertexInstance == None:
    print("終点の入力が不正です")
    sys.exit()



initialVertexInstance.lb = 0
initialVertexInstance.pf = True
print(f"{initialVertexInstance.vn}には永久ラベル{initialVertexInstance.lb}が貼られています")


# 仮ラベルの値を入れるリストを定義
temporaryLabels = []
# 経路を探していく途中で現在地の点のインスタンスを保存する
currentVertexInstance = initialVertexInstance
currentSubGraphInstace = initialSubGraphInstance


while currentVertexInstance != finalVertexInstance:
    currentVertexInstance, temporaryLabels = g6.pasteNext(currentVertexInstance, temporaryLabels)

if finalVertexInstance.pf == True:
    vertex = finalVertexInstance
    # 経路の逆順に点の名前を保存するリストrouteListを定義    
    routeList = [vertex.vn]
    while vertex != initialVertexInstance:
        # 現在いる点から一つ前の点のインスタンスを探す
        vertex = g6.searchInstance(vertex.pvn)
        routeList.append(vertex.vn)
    routeList.reverse()
    print(routeList)
    for vName in routeList:
        print(vName)
    print(f"所要時間は{finalVertexInstance.lb}です")

