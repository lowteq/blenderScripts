自作のBlenderアドオンやスクリプトを公開しています  
主にアバター制作向け  
- [AsymmetrizeShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/AsymmetrizeShapekey.py)  
左右対称に作られたシェイプキーから左右に分けたシェイプキーを作成します。
- [FaceEXShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/faceexshapekey.py)  
選択したメッシュをシェイプキーが100のときにその位置にくるようなメッシュとしてシェイプキーを作ります。
- [SortShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/sortshapekey.py)  
シェイプキーの順序をソートします。
---

# AsymmetrizeShapekey
[AsymmetrizeShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/AsymmetrizeShapekey.py)  
## LICENSE
MIT License
## 使いかた
https://github.com/Taremin/ApplyModifier
こちらのアドオンなどで作った左右対称なシェイプキーに対して使います。
左右非対称化したいシェイプキーを選択した状態でシェイプキーのスペシャルメニュー▼をクリックしてAsymmetrizeShapekeyをクリックし作成することができます。

![p](https://github.com/lowteq/blenderScripts/blob/master/readmeimages/20200211045408_383x354.png)

![s](https://github.com/lowteq/blenderScripts/blob/master/readmeimages/20200211113539_1468x888.png)
## HowToUse
https://github.com/Taremin/ApplyModifier

run to symmetry shapekey created by this add-on.

you can find property > shapekey > specials

![p](https://github.com/lowteq/blenderScripts/blob/master/readmeimages/20200211045408_383x354.png)

Click to create a new asymmetric shape keys


---

# FaceEXShapekey 
[FaceEXShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/faceexshapekey.py)  
## LICENSE
MIT License
## 使いかた
キャラの顔の中に埋め込んだメッシュを出し入れするシェイプキーを簡単につくることができます。ex.ハート目、頬染め、漫符
編集モード時3DビューのツールシェルフのFaceEXShapekeyパネルから使います

duplicate : 選択したメッシュを複製します。ハート目や頬染めシェイプキーを作るときはONにします

innerOffset : シェイプキーの値が0のときのメッシュの相対位置です。ハート目などを顔に埋め込む場合は(0cm,5cm,0cm)くらいがよいです。  
innerScale : シェイプキーの値が0のときのメッシュのScaleです。0.5くらいがよいです。  
surfOffset : シェイプキーの値が1のときのメッシュの相対位置です。ハート目や頬染めシェイプキーは元のメッシュより手前で必要があるので(0,-1mm,0)くらいがよいです。  
surfScale : シェイプキーの値が1のときのメッシュのScaleです。頬染めシェイプキーの場合は単純にOffsetで手前に出しただけではうまくいかないのでこの値を1.01などにします。  

create : スクリプト実行ボタン


---

# SortShapekey
## LICENSE
MIT License
## 使いかた
[![howtouse]](https://user-images.githubusercontent.com/5676316/131511705-57495c7d-615d-45a9-978d-ddccd795fb2f.mp4)

# AdjustEdgesLength
[AdjustEdgesLength](https://github.com/lowteq/blenderScripts/blob/master/scripts/adjustedges.py)
## LICENSE
MIT License
#　使い方
編集モードで辺を選択した状態でWキーもしくは右クリックからコンテキストメニュー>Adjust Edges Lengthをクリック

