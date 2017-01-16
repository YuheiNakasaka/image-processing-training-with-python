# numpyで画素処理するぞい
# numpyの行・列をx・yに勘違いしてたので最初イミフだった...
# 行は縦(y)で列は横(x)を描画していくので覚えとけ
# 参考) http://takamints.hatenablog.jp/entry/2015/03/04/223059
import random
import numpy as np
import cv2

# 基本画像。正方形。黒。3チャンネル
rows = 400
cols = 400
image = np.zeros((rows, cols, 3), np.uint8)

# 染色する位置と画素値
row = 64
col = 40
r, g, b = [255, 255, 0]

# 1) itemsetで画素アクセス
# 各チャンネルごとに画素値をセットする
image.itemset((row, col, 0), b)
image.itemset((row, col, 1), g)
image.itemset((row, col, 2), r)

# 2) 配列で更新

## image[0:row, 0:col]と同じ。row x col の面積部分が更新されるイメージ。
image[:row, :col] = [b, g, r]

## これも上と同じ。各チャネル毎
image[:row, :col, 0], image[:row, :col, 1], image[:row, :col, 2] = [b, g, r]

# 3) 複雑なやつ

## 画像全体
image[:,:] = [0, 0, 0]

# [縦(row), 横(column)]の範囲を4画素ごと画素更新する
r, g, b = [255, 255, 255]
image[260:300, 80:360:20]  = [r, g, b]
image[120:240:4, 80:160]  = [r, g, b]
image[120:240, 80:160:4]  = [r, g, b]

# 画像表示
cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
