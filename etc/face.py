import cv2

# 学習済みデータ
face_cascade = cv2.CascadeClassifier('/Users/razokulover/.pyenv/versions/anaconda3-4.0.0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

# 画像読み込み
img = cv2.imread('../images/rgb_people.jpg')

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 物体検出する
faces = face_cascade.detectMultiScale(gray)

# 検出部分を四角形で囲む
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

# 顔検出した画像を表示
cv2.imshow('example', img)

# windowにfocusしてるときに何かkeyを押すと閉じる
cv2.waitKey(0) # key入力を待ち続ける
cv2.destroyAllWindows()
