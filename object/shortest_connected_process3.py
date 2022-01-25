# © 2022 ushita37

import sys
import shortest_connected_class3 as scc3

initialVertexInput = input("始点を入力してください>")
finalVertexInput = input("終点を入力してください>")


g8vA = scc3.Vertex("g8vA")
g8vB = scc3.Vertex("g8vB")
g8vC = scc3.Vertex("g8vC")
g8vD = scc3.Vertex("g8vD")
g8vE = scc3.Vertex("g8vE")
g8vF = scc3.Vertex("g8vF")
g8vG = scc3.Vertex("g8vG")

g9vA = scc3.Vertex("g9vA")
g9vB = scc3.Vertex("g9vB")
g9vC = scc3.Vertex("g9vC")
g9vD = scc3.Vertex("g9vD")
g9vE = scc3.Vertex("g9vE")
g9vF = scc3.Vertex("g9vF")
g9vG = scc3.Vertex("g9vG")

g10vA = scc3.Vertex("g10vA")
g10vB = scc3.Vertex("g10vB")
g10vC = scc3.Vertex("g10vC")
g10vD = scc3.Vertex("g10vD")

g8e1 = scc3.Edge("g8e1", 3, [g8vA, g8vD])
g8e2 = scc3.Edge("g8e2", 5, [g8vA, g8vB])
g8e3 = scc3.Edge("g8e3", 6, [g8vB, g8vC])
g8e4 = scc3.Edge("g8e4", 7, [g8vD, g8vE])
g8e5 = scc3.Edge("g8e5", 12, [g8vE, g8vF])
g8e6 = scc3.Edge("g8e6", 1, [g8vF, g8vG])

g9e1 = scc3.Edge("g9e1", 2, [g9vA, g9vB])
g9e2 = scc3.Edge("g9e2", 3, [g9vB, g9vC])
g9e3 = scc3.Edge("g9e3", 5, [g9vC, g9vD])
g9e4 = scc3.Edge("g9e4", 7, [g9vB, g9vE])
g9e5 = scc3.Edge("g9e5", 11, [g9vE, g9vF])
g9e6 = scc3.Edge("g9e6", 1, [g9vF, g9vG])
g9e7 = scc3.Edge("g9e7", 4, [g9vG, g9vA])

g10e1 = scc3.Edge("g10e1", 8, [g10vA, g10vB])
g10e2 = scc3.Edge("g10e2", 16, [g10vB, g10vC])
g10e3 = scc3.Edge("g10e3", 6, [g10vC, g10vD])

b8D10C = scc3.Edge("b8D10C", 0, [g8vD, g10vC]) # グラフ8の点D(g8vD)とグラフ10の点C(g10vC)をつなぐ橋
b8B9G = scc3.Edge("b8B9G", 0, [g8vB, g9vG])
b9F10B = scc3.Edge("b9F10B", 0, [g9vF, g10vB])
b8E9E = scc3.Edge("b8E9E", 0, [g8vE, g9vE])
b8C9A = scc3.Edge("b8C9A", 0, [g8vC, g9vA])
b8C10A = scc3.Edge("b8A10A", 0, [g8vC, g10vA])
b9A10A = scc3.Edge("b9A10A", 0, [g9vA, g10vA])
b8G9D = scc3.Edge("b8G9D", 0, [g8vG, g9vD])
b8G10D = scc3.Edge("b8G10D", 0, [g8vG, g10vD])
b9D10D = scc3.Edge("b9D10D", 0, [g9vD, g10vD])


# 全ての点と辺を定義してから点集合と辺集合とグラフを作る
g8vSet = {g8vA, g8vB, g8vC, g8vD, g8vE, g8vF, g8vG}
g9vSet = {g9vA, g9vB, g9vC, g9vD, g9vE, g9vF, g9vG}
g10vSet = {g10vA, g10vB, g10vC, g10vD}

g8eSet = {g8e1, g8e2, g8e3, g8e4, g8e5, g8e6}
g9eSet = {g9e1, g9e2, g9e3, g9e4, g9e5, g9e6, g9e7}
g10eSet = {g10e1, g10e2, g10e3}

bSet = {b8D10C, b8B9G, b9F10B, b8E9E, b8C9A, b8C10A, b9A10A, b8G9D, b8G10D, b9D10D} #橋集合

g8g9g10vSet = g8vSet | g9vSet | g10vSet # g8とg9、g10の点集合の和集合
g8g9g10eSet = g8eSet | g9eSet | g10eSet | bSet # g8とg9、g10の辺集合と橋集合の和集合

g = scc3.Graph(g8g9g10vSet,g8g9g10eSet)


# inputされた文字列からVertexインスタンスへの変換
initialVertexInstance = g.searchInstance(initialVertexInput)
finalVertexInstance = g.searchInstance(finalVertexInput)
# inputチェック
if initialVertexInstance == None:
    print("始点の入力が不正です")
    sys.exit()
elif finalVertexInstance == None:
    print("終点の入力が不正です")
    sys.exit()
elif initialVertexInstance == finalVertexInstance:
    print("始点と終点が同じです")
    sys.exit()


initialVertexInstance.lb = 0
initialVertexInstance.pf = True
# 仮ラベルの値を入れるリストを定義
temporaryLabels = []
# 経路を探していく際に起点とする点を、始点で初期化
previousVertexInstance = initialVertexInstance

while previousVertexInstance != finalVertexInstance:
    previousVertexInstance, temporaryLabels = g.findMin(previousVertexInstance, temporaryLabels)

vertex = finalVertexInstance
# 経路の逆順（終点→始点の順）に点の名前を保存するリストrouteListを定義    
routeList = [vertex.vn]
while vertex != initialVertexInstance:
    # 起点のインスタンスを探す
    vertex = g.searchInstance(vertex.pvn)
    routeList.append(vertex.vn)
# routeListを反転させて正しい順番（始点→終点）に直す
routeList.reverse()


# 始点をprint
print(routeList[0])
# 途中通る辺と始点以外の点をprint
for vName in routeList[1:]:
    vertex = g.searchInstance(vName)
    print(f"↓（{vertex.pen}）")
    print(vName)
print(f"所要時間は{finalVertexInstance.lb}です")