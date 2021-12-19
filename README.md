# 鉄道の路線図を元にした最短路の探索

ushita37  

## 1. これは何か

これは路線図を元にしたグラフで始点から終点までの最短路を求めるプログラムである  

## 2. shortest_path_process3.pyの動かし方
shortest_path_process3.pyで使用したグラフの図はprocess3_graph.PNGを参照  
図中のvA～vJは点の名前を、①～⑭は辺の名前を、○の隣の数字は辺の重みを、それぞれ表している  

- shortest_path_process3.pyを実行する

```
C:\Python>python shortest_path_process3.py 
```
- `始点を入力してください>`と表示が出たら、グラフ上の点のうち1つを選んで半角英数で入力する
- `終点を入力してください>`　と表示が出たら、先に入力した点とは異なる点を1つ選んで半角英数で入力する
- そうすると始点から終点までの最短路が表示される

## 3. 実行例

```
C:\object>python shortest_path_process3.py 
始点を入力してください>vJ
終点を入力してください>vB
vJ
↓（e3）
vE
↓（e4）
vD
↓（e5）
vC
↓（e6）
vA
↓（e7）
vB
所要時間は15です
```



## 4. ファイルの説明

以下では、主プログラムを（主）、副プログラムを（副）と略記する  

### （1）新宿駅を出発駅に山手線内回りを1周するプログラム（early_works）

（主）yamanote_inner_track.py：内回り1周分の処理をするもの  
（副）stationName.csv：山手線の駅名を内回りの順に並べたリスト  
（副）rinnsetsuValueOnly2.csv：拡張した隣接行列で山手線の路線図を表現したもの  

### （2）新宿駅を出発駅に山手線外回りを1周するプログラム（early_works）

（主）yamanote_outer_track.py：外回り1周分の処理をするもの  
（副）stationName.csv  
（副）rinnsetsuValueOnly2.csv  

### （3）新宿駅を出発駅に山手線内回りor外回りを1周するプログラム（early_works）

（主）yamanote_func.py：内回りor外回り1周分の処理をするもの  
（副）stationName.csv  
（副）rinnsetsuValueOnly2.csv  

### （4）出発駅、到着駅、方向を入力して山手線に沿って経路を探すプログラム（early_works）

（主）yamanote_search.py：山手線で経路を探し、経路に沿って駅間所要時間を合計するもの  
（副）stationName.csv  
（副）JYarray1.csv：rinnsetsuValueOnly2.csvのij要素のうち、1と-1を駅間所要時間に交換した行列  

### （5）出発駅、到着駅を入力して山手線で最短路を探すプログラム（early_works）

（主）yamanote_shortest.py：内回りと外回りの駅間所要時間を合計し、小さい方の経路と累計所要時間を表示するもの  
（副）stationName.csv  
（副）JYarray1.csv  

### （6）出発駅、到着駅を入力して中央・総武線で経路を探すプログラム（early_works）

（主）chuosobu_shortest.py：東行きと西行きのうち正しい経路が存在する方を表示するもの  
（副）ChuoSobuEkimei.csv：中央・総武線の駅名を三鷹駅から千葉駅まで並べたリスト  
（副）JBarray1.csv：駅間所要時間を反映して中央・総武線の路線図を表現した行列  

### （7）入力された出発駅、到着駅がどの路線に所属しているか調べるプログラム（early_works）

（主）line_finding.py：山手線、中央・総武線、山手線と中央・総武線のうちどれに属するか、あるいは存在しないかを表示するもの  
（副）stationName.csv  
（副）ChuoSobuEkimei.csv  

### （8）出発駅、到着駅を入力して山手線、中央・総武線で最短路を探すプログラム（failure）

（主）shortest_path_problem.py：中央・総武線と山手線で最短路を探し、その経路と累計所要時間をを表示するもの  
（副）shortest_path_def.py：shortest_path_problem.pyで使う関数を定義するもの  
（副）JBekimei.csv：中央・総武線の駅ナンバリングに対応するように駅名を並べたリスト  
（副）JYekimei.csv:山手線の駅ナンバリングに対応するように駅名を並べたリスト  
（副）JBarray2.csv：実際の駅ナンバリングに行と列を対応させて、中央・総武線の路線図を表現した行列  
（副）JYarray2.csv：実際の駅ナンバリングに行と列を対応させて、山手線の路線図を表現した行列  
（副）TransferLines1.csv：路線名を並べたリスト  
（副）TransferSta1.csv：乗換駅の名前を並べたリスト  
（副）Transfer1.csv：路線名を行i、乗換駅の名前を列jに対応させて、ij要素を駅ナンバリングとした行列  

### （9）始点、終点を入力して1つの連結グラフに対して最短路の重みの合計を求めるプログラム（object）

（主）shortest_path_object2.py：最短路の重みの合計を表示するもの  

### （10）始点、終点を入力して1つの連結グラフに対して最短路の重みの合計を求めるプログラム（object）

（主）shortest_path_process1.py：shoetest_path_objgct2.pyから主要な処理を抜き出したもの  
（副）shortest_path_class1.py：shortest_path_process1.pyで使うメソッドやクラスを定義したもの  

### （11）始点、終点を入力して1つの連結グラフに対して最短路自体と最短路の重みの合計を求めるプログラム（object）

（主）shortest_path_process2.py：最短路自体と最短路の重みの合計を表示するもの  
（副）shortest_path_class2.py：shortest_path_process2.pyで使うメソッドやクラス、関数を定義したもの  

### （12）（11）の出力を改良したプログラム（object）
（主）shortest_path_process3.py：最短路自体と最短路の重みの合計を表示するもの  
（副）shortest_path_class3.py：shortest_path_process2.pyの中の関数をメソッドに変え、shortest_path_process3.pyで使えるようにしたもの  

### （13）始点、終点を入力して、複数のグラフを連結して最短路自体と最短路の重みの合計を求めるプログラム（Work_In_Progress）

（主）shortest_connected_process1.py：相異なるグラフに属する始点と終点を結ぶ最短路自体と最短路の重みの合計を表示するもの  
（副）shortest_connected_class1.py：shortest_connected_process1.py：shortest_connected_process1で使うメソッドやクラスを定義したもの  




