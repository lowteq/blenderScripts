自作のBlenderアドオンやスクリプトを公開しています
- [AsymmetrizeShapekey](https://github.com/lowteq/blenderScripts#asymmetrizeshapekey)
- [FaceEXShapekey](https://github.com/lowteq/blenderScripts#faceexshapekey)

---

# 寄付(Donate)
[paypal.me](https://paypal.me/qukumulowteq?locale.x=ja_JP)  
このリポジトリのアドオンはモデリング・Blender・VRChat界隈の発展のために無償で公開しているものです。  
寄付をしていただけると今後の開発の支援になります。

---

# AsymmetrizeShapekey
[AsymmetrizeShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/AsymmetrizeShapekey.py)  
[AsymmetrizeShapekey 2.8対応](https://github.com/lowteq/blenderScripts/blob/master/scripts/AsymmetrizeShapekey28.py)

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
## LICENSE
MIT License

---

# FaceEXShapekey 
[FaceEXShapekey](https://github.com/lowteq/blenderScripts/blob/master/scripts/faceexshapekey.py)  
[FaceEXShapekey 2.8対応](https://github.com/lowteq/blenderScripts/blob/master/scripts/faceexshapekey28.py)

## 使いかた
キャラの顔の中に埋め込んだメッシュを出し入れするシェイプキーを簡単につくることができます。ex.ハート目、頬染め、漫符
編集モード時3DビューのツールシェルフのFaceEXShapekeyパネルから使います

duplicate : 選択したメッシュを複製します。ハート目や頬染めシェイプキーを作るときはONにします

innerOffset : シェイプキーの値が0のときのメッシュの相対位置です。ハート目などを顔に埋め込む場合は(0cm,5cm,0cm)くらいがよいです。
innerScale : シェイプキーの値が0のときのメッシュのScaleです。0.5くらいがよいです。
surfOffset : シェイプキーの値が1のときのメッシュの相対位置です。ハート目や頬染めシェイプキーは元のメッシュより手前で必要があるので(0,-1mm,0)くらいがよいです。
surfScale : シェイプキーの値が1のときのメッシュのScaleです。頬染めシェイプキーの場合は単純にOffsetで手前に出しただけではうまくいかないのでこの値を1.01などにします。

create : スクリプト実行ボタン
## LICENSE
MIT License

