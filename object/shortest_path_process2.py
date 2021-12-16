# © 2021 ushita37

import sys
import shortest_path_class2 as spc2

initialVertexInput = input("始点を入力してください>")
finalVertexInput = input("終点を入力してください>")


g3vA = spc2.Vertex("g3vA")
g3vB = spc2.Vertex("g3vB")
g3vC = spc2.Vertex("g3vC")
g3vD = spc2.Vertex("g3vD")
g3vE = spc2.Vertex("g3vE")

g4vA = spc2.Vertex("g4vA")
g4vB = spc2.Vertex("g4vB")
g4vC = spc2.Vertex("g4vC")
g4vD = spc2.Vertex("g4vD")
g4vE = spc2.Vertex("g4vE")
g4vF = spc2.Vertex("g4vF")

g5vA = spc2.Vertex("g5vA")
g5vB = spc2.Vertex("g5vB")
g5vC = spc2.Vertex("g5vC")
g5vD = spc2.Vertex("g5vD")
g5vE = spc2.Vertex("g5vE")
g5vF = spc2.Vertex("g5vF")
g5vG = spc2.Vertex("g5vG")
g5vH = spc2.Vertex("g5vH")
g5vI = spc2.Vertex("g5vI")
g5vJ = spc2.Vertex("g5vJ") 


g3e1 = spc2.Edge("g3e1", 3, [g3vA, g3vE])
g3e2 = spc2.Edge("g3e2", 18, [g3vB, g3vE])
g3e3 = spc2.Edge("g3e3", 7, [g3vB, g3vC])
g3e4 = spc2.Edge("g3e4", 6, [g3vC, g3vD])
g3e5 = spc2.Edge("g3e5", 4, [g3vD, g3vE])

g4e1 = spc2.Edge("g4e1", 4, [g4vA, g4vA]) # ループ
g4e2 = spc2.Edge("g4e2", 4, [g4vA, g4vB])
g4e3 = spc2.Edge("g4e3", 3, [g4vB, g4vC])
g4e4 = spc2.Edge("g4e4", 8, [g4vC, g4vD])
g4e5 = spc2.Edge("g4e5", 8, [g4vC, g4vD])
g4e6 = spc2.Edge("g4e6", 1, [g4vD, g4vE])
g4e7 = spc2.Edge("g4e7", 5, [g4vE, g4vF])
g4e8 = spc2.Edge("g4e8", 6, [g4vB, g4vF])

g5e1 = spc2.Edge("g5e1", 5, [g5vA, g5vC])
g5e2 = spc2.Edge("g5e2", 4, [g5vB, g5vC])
g5e3 = spc2.Edge("g5e3", 6, [g5vC, g5vD])
g5e4 = spc2.Edge("g5e4", 6, [g5vC, g5vD])
g5e5 = spc2.Edge("g5e5", 2, [g5vD, g5vE])
g5e6 = spc2.Edge("g5e6", 8, [g5vE, g5vF])
g5e7 = spc2.Edge("g5e7", 5, [g5vF, g5vG])
g5e8 = spc2.Edge("g5e8", 7, [g5vG, g5vH])
g5e9 = spc2.Edge("g5e9", 13, [g5vB, g5vH])
g5e10 = spc2.Edge("g5e10", 9, [g5vD,g5vH])
g5e11 = spc2.Edge("g5e11", 12, [g5vD, g5vG])
g5e12 = spc2.Edge("g5e12", 8, [g5vF, g5vJ])
g5e13 = spc2.Edge("g5e13", 7, [g5vG, g5vI])
g5e14 = spc2.Edge("g5e14", 3, [g5vI, g5vI]) # ループ


# 全ての点と辺を定義してから点集合と辺集合とグラフを作る
g3vSet = {g3vA, g3vB, g3vC, g3vD, g3vE}
g4vSet = {g4vA, g4vB, g4vC, g4vD, g4vE, g4vF}
g5vSet = {g5vA, g5vB, g5vC, g5vD, g5vE, g5vF, g5vG, g5vH, g5vI, g5vJ}

g3eSet = {g3e1, g3e2, g3e3, g3e4, g3e5}
g4eSet = {g4e1, g4e2, g4e3, g4e4, g4e5, g4e6, g4e7, g4e8}
g5eSet = {g5e1, g5e2, g5e3, g5e4, g5e5, g5e6, g5e7, g5e8, g5e9, g5e10, g5e11, g5e12, g5e13, g5e14}

g3 = spc2.Graph(g3vSet, g3eSet)
g4 = spc2.Graph(g4vSet, g4eSet)
g5 = spc2.Graph(g5vSet, g5eSet)



# inputされた文字列からVertexインスタンスへの変換
initialVertexInstance = spc2.searchInstanceFunc2(g5, initialVertexInput)
finalVertexInstance = spc2.searchInstanceFunc2(g5, finalVertexInput)
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


while currentVertexInstance != finalVertexInstance:
    currentVertexInstance, temporaryLabels = spc2.pasteNextLabel(g5, currentVertexInstance, temporaryLabels)

if finalVertexInstance.pf == True:
    vertex = finalVertexInstance
    # 経路の逆順に点の名前を保存するリストrouteListを定義    
    routeList = [vertex.vn]
    while vertex != initialVertexInstance:
        # 現在いる点から一つ前の点のインスタンスを探す
        vertex = spc2.searchInstanceFunc2(g5, vertex.pvn)
        routeList.append(vertex.vn)
    routeList.reverse()
    print(routeList)
    for vName in routeList:
        print(vName)
    print(f"所要時間は{finalVertexInstance.lb}です")

