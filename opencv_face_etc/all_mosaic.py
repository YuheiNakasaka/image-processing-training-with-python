# モザイクかけるぞい
# 参考) http://blanktar.jp/blog/2015/02/python-opencv-mosaic.html

import cv2

img = cv2.imread('../images/lena.jpg') # 画像読み込む

# ステップ数にマイナスの値を指定すると後ろからそのステップ数ずつ取得するようになる
# ex) src = numpy.array([0,1,2,3,4,5])
#     src[::-1] #=> [5,4,3,2,1,0]
#     src[::-2] #=> [5,3,1]
# 読んだ) http://qiita.com/supersaiakujin/items/d63c73bb7b5aac43898a
orgsize = img.shape[:2][::-1]

# 画像を縮小したあとそれをニアレストネイバー法で拡大することでモザイクを実現する
img = cv2.resize(img, ( int(orgsize[0]/20), int(orgsize[1]/20) ))
img = cv2.resize(img, orgsize, interpolation=cv2.INTER_NEAREST)

cv2.imwrite('../images/mosaic_lena.jpg', img)
