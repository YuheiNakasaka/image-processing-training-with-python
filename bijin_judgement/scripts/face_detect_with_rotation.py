# 画像を読み込んで顔認識
# top levelをパスに含める
import sys
sys.path.append('/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement')

import os
import re
import cv2
import numpy as np
import math
from math import ceil

# 顔画像用の生成先ディレクトリの作成
src_image_dir = '/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement/images'
face_image_dir = '/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement/images/faces'
if os.path.exists(face_image_dir) == False:
    os.mkdir(face_image_dir)

# 目・顔認識はhaarcascade
cascades_dir = '/Users/razokulover/.pyenv/versions/anaconda3-4.0.0/share/OpenCV/haarcascades'
face_cascade = cv2.CascadeClassifier(os.path.join(cascades_dir, 'haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(cascades_dir, 'haarcascade_eye.xml'))

# 全画像で顔検出していく
hit = 0
fail = 0
for f in os.listdir(src_image_dir):
    if hit > 5:
        break
    src_path = os.path.join(src_image_dir, f)
    if os.path.isfile(src_path) and re.match(r".+\.(jpg|jpeg|png|gif)$", src_path):
        # 画像読み込み
        base_img = cv2.imread(src_path)

        # 画像サイズの統一
        base_h, base_w = base_img.shape[:2]
        resize_h, resize_w = [int(500 * (base_h/base_w)), 500]
        resize_img = cv2.resize(base_img, (resize_w, resize_h))

        # スコアの初期化
        scores = {"score": 1000, "img": ""}
        # -50~+50度の傾きで実行
        for j in range(-50, 55, 5):
            # 拡大画像
            big_img = np.zeros((resize_h * 2, resize_w * 2, 3), np.uint8)
            big_img[ceil(resize_h/2.0):ceil(resize_h/2.0*3.0), ceil(resize_w/2.0):ceil(resize_w/2.0*3.0)] = resize_img

            # がぞうの中心
            center = tuple(np.array([big_img.shape[1] * 0.5, big_img.shape[0] * 0.5]))

            size = tuple(np.array([big_img.shape[1], big_img.shape[0]]))

            # 回転させたい角度
            angle = float(j)

            # 拡大比率
            scale = 1.0

            # 回転行列計算
            rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

            # アフィン変換
            img_rot = cv2.warpAffine(big_img, rotation_matrix, size, flags=cv2.INTER_CUBIC)

            # 顔判定
            faces = face_cascade.detectMultiScale(img_rot, scaleFactor=1.2, minNeighbors=2, minSize=(50, 50))
            if len(faces):
                for (x,y,w,h) in faces:
                    face_img = img_rot[y:y+h, x:x+w]
                    # 顔検出された部分からさらに目が2個検出されてかつ目の距離が顔の1/4の距離より大きい場合は書き出す
                    eyes = eye_cascade.detectMultiScale(face_img)
                    if len(eyes) == 2 and abs(eyes[0][0] - eyes[1][0]) > w/4:
                        # 目の水平度を算出してより水平(0に近い)ものが良い顔とする
                        score = math.atan2(abs(eyes[1][1] - eyes[0][1]), abs(eyes[1][0] - eyes[0][0]))
                        # スコアがより小さければ更新する
                        if score < scores["score"]:
                            scores["score"] = score
                            scores["img"] = face_img

        # スコアが一番高かった顔画像を書き出す
        if scores["img"] != "":
            hit += 1
            print("id: {f}, score: {score}".format(f=f, score=scores["score"]))
            cv2.imwrite(os.path.join(face_image_dir, f), scores["img"])
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
