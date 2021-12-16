# © 2021 ushita37

import sys
import shortest_path_class3 as spc3

initialVertexInput = input("始点を入力してください>")
finalVertexInput = input("終点を入力してください>")

# まず点を定義
vA = spc3.Vertex("vA")
vB = spc3.Vertex("vB")
vC = spc3.Vertex("vC")
vD = spc3.Vertex("vD")
vE = spc3.Vertex("vE")
vF = spc3.Vertex("vF")
vG = spc3.Vertex("vG")
vH = spc3.Vertex("vH")
vI = spc3.Vertex("vI")
vJ = spc3.Vertex("vJ")
vSet = {vA, vB, vC, vD, vE, vF, vG, vH, vI, vJ} # 点集合を定義

# 定義済みの点を使って辺を定義
e1 = spc3.Edge("e1", 5, [vI, vF])
e2 = spc3.Edge("e2", 8, [vF, vJ])
e3 = spc3.Edge("e3", 3, [vJ, vE])
e4 = spc3.Edge("e4", 3, [vE, vD])
e5 = spc3.Edge("e5", 5, [vD, vC])
e6 = spc3.Edge("e6", 1, [vC, vA])
e7 = spc3.Edge("e7", 3, [vA, vB])
e8 = spc3.Edge("e8", 6, [vB, vC])
e9 = spc3.Edge("e9", 8, [vC, vD])
e10 = spc3.Edge("e10", 2, [vD, vF])
e11 = spc3.Edge("e11", 9, [vF, vB])
e12 = spc3.Edge("e12", 2, [vB, vG])
e13 = spc3.Edge("e13", 5, [vG, vH])
e14 = spc3.Edge("e14", 1, [vH, vF])
eSet = {e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14} # 辺集合を定義

# 点集合と辺集合を使ってグラフを定義
g = spc3.Graph(vSet, eSet)


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