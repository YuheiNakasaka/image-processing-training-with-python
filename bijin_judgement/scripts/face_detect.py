# 画像を読み込んで顔認識
# top levelをパスに含める
import sys
sys.path.append('/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement')

import os
import re
import cv2

# 顔画像用の生成先ディレクトリの作成
src_image_dir = '/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement/images'
face_image_dir = '/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement/images/faces'
if os.path.exists(face_image_dir) == False:
    os.mkdir(face_image_dir)

# とりあえず顔認識はhaarcascadeで
face_cascade = cv2.CascadeClassifier('/Users/razokulover/.pyenv/versions/anaconda3-4.0.0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

# 全画像で顔検出していく
hit = 0
fail = 0
for f in os.listdir(src_image_dir):
    src_path = os.path.join(src_image_dir, f)
    if os.path.isfile(src_path) and re.match(r".+\.(jpg|jpeg|png|gif)$", src_path):
        # 顔認識
        base_img = cv2.imread(src_path)
        # 精度向上のため画像のスケールをあわせる
        if base_img is not None:
            height = base_img.shape[0]
            width = base_img.shape[1]
            resized_img = cv2.resize(base_img, (500, int(500*(height / width))))
            gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

            # 検出した顔を全て切り出してローカルに保存する
            if len(faces) > 0:
                hit += 1
                for face in faces:
                    face_x = face[0]
                    face_y = face[1]
                    face_w = face[2]
                    face_h = face[3]

                    face_img = resized_img[face_y:face_y+face_h, face_x:face_x+face_w]
                    cv2.imwrite(os.path.join(face_image_dir, f), face_img)
            else:
                fail += 1


# 検出率を算出する
hit_rate = (hit / (hit+fail)) * 100
print("Hit count: {hit}".format(hit=hit))
print("Fail count: {fail}".format(fail=fail))
print("Hit rate: {hit_rate}%".format(hit_rate=hit_rate))

# 1回目
# it count: 1633
# Fail count: 340
# Hit rate: 82.76735935124177%
