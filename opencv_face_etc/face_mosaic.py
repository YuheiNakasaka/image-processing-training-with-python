# モザイクかけるぞい
# 参考) http://blanktar.jp/blog/2015/02/python-opencv-pillow-facemosaic.html

import cv2

# 学習済みデータ
face_cascade = cv2.CascadeClassifier('/Users/razokulover/.pyenv/versions/anaconda3-4.0.0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

# 画像読み込み
base_img = cv2.imread('../images/rgb_people.jpg')

# グレースケール変換
gray = cv2.cvtColor(base_img, cv2.COLOR_BGR2GRAY)

# 物体検出する
# 戻り値は(x座標, y座標, 横幅, 縦幅)のリスト。numpyのarrayなので注意。
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

# 各顔検出部分ごとに処理
if len(faces) > 0
    for face in faces:
        # 検出結果を取得
        face_x = face[0]
        face_y = face[1]
        face_w = face[2]
        face_h = face[3]

        # 顔部分を抜き出してモザイク処理を施す
        face_img = base_img[face_y:face_y+face_h, face_x:face_x+face_w]
        face_img = cv2.resize(face_img, (int(face_w / 20), int(face_h / 20)))
        face_img = cv2.resize(face_img, (face_w, face_h), interpolation=cv2.INTER_NEAREST)

        # 元画像の顔部分を生成したモザイク画像で更新する
        base_img[face_y:face_y+face_h, face_x:face_x+face_w] = face_img

cv2.imwrite('../images/face_mosaic.jpg', base_img)
