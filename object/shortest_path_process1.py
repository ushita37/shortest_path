# © 2021 ushita37

import shortest_path_class1 as spc1

initialVertexInput = input("始点を入力してください>")
finalVertexInput = input("終点を入力してください>")


g3vA = spc1.Vertex("g3vA")
g3vB = spc1.Vertex("g3vB")
g3vC = spc1.Vertex("g3vC")
g3vD = spc1.Vertex("g3vD")
g3vE = spc1.Vertex("g3vE")

g4vA = spc1.Vertex("g4vA")
g4vB = spc1.Vertex("g4vB")
g4vC = spc1.Vertex("g4vC")
g4vD = spc1.Vertex("g4vD")
g4vE = spc1.Vertex("g4vE")
g4vF = spc1.Vertex("g4vF")

g3e1 = spc1.Edge("g3e1", 3, [g3vA, g3vE])
g3e2 = spc1.Edge("g3e2", 18, [g3vB, g3vE])
g3e3 = spc1.Edge("g3e3", 7, [g3vB, g3vC])
g3e4 = spc1.Edge("g3e4", 6, [g3vC, g3vD])
g3e5 = spc1.Edge("g3e5", 4, [g3vD, g3vE])

g4e1 = spc1.Edge("g4e1", 4, [g4vA, g4vA])
g4e2 = spc1.Edge("g4e2", 4, [g4vA, g4vB])
g4e3 = spc1.Edge("g4e3", 3, [g4vB, g4vC])
g4e4 = spc1.Edge("g4e4", 8, [g4vC, g4vD])
g4e5 = spc1.Edge("g4e5", 8, [g4vC, g4vD])
g4e6 = spc1.Edge("g4e6", 1, [g4vD, g4vE])
g4e7 = spc1.Edge("g4e7", 5, [g4vE, g4vF])
g4e8 = spc1.Edge("g4e8", 6, [g4vB, g4vF])


# 全ての点と辺を定義してから点集合と辺集合とグラフを作る
g3vSet = {g3vA, g3vB, g3vC, g3vD, g3vE}
g4vSet = {g4vA, g4vB, g4vC, g4vD, g4vE, g4vF}

g3eSet = {g3e1, g3e2, g3e3, g3e4, g3e5}
g4eSet = {g4e1, g4e2, g4e3, g4e4, g4e5, g4e6, g4e7, g4e8}

g3 = spc1.Graph(g3vSet, g3eSet)
g4 = spc1.Graph(g4vSet, g4eSet)




# inputされた文字列からVertexインスタンスへの変換
initialVertexInstance, finalVertexInstance = spc1.searchInstanceFunc(initialVertexInput, finalVertexInput, g4)
# inputチェック
if initialVertexInstance == None:
    print("始点の入力が不正です")
    exit
elif finalVertexInstance == None:
    print("終点の入力が不正です")
    exit




initialVertexInstance.lb = 0
initialVertexInstance.pf = True
print(f"{initialVertexInstance.vn}には永久ラベル{initialVertexInstance.lb}が貼られています")


# 仮ラベルの値を入れるリストを定義
temporaryLabels = []
# 経路を探していく途中で現在地の点のインスタンスを保存する
currentVertexInstance = initialVertexInstance



while currentVertexInstance != finalVertexInstance:
    currentVertexInstance, temporaryLabels = spc1.pasteNextLabel(g4, currentVertexInstance,temporaryLabels)



if finalVertexInstance.pf == True:
    print(f"所要時間は{finalVertexInstance.lb}です")