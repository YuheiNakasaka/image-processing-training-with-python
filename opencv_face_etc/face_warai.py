# 顔認識して透過画像を重ねるぞい
# 元サイトはopencvの返り値とかnumpyの行列の認識間違ってたのでその辺修正した
# 参考) http://blog.adjust-work.com/212/
import cv2

# 学習済みデータ
face_cascade = cv2.CascadeClassifier('/Users/razokulover/.pyenv/versions/anaconda3-4.0.0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

# 画像読み込み
base_img = cv2.imread('../images/rgb_people.jpg')
warai_img = cv2.imread('../images/warai_layer_f.png', cv2.IMREAD_UNCHANGED)

# グレースケール変換
gray = cv2.cvtColor(base_img, cv2.COLOR_BGR2GRAY)

# 物体検出する
# 戻り値は(x座標, y座標, 横幅, 縦幅)のリスト。numpyのarrayなので注意。
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

mask = warai_img[:,:,3] # 3次元のRGBAのからAのみ抜きだし、アルファチャンネルのみ抽出(2次元になる)
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) # (3次元)
mask = mask / 255.0 # 範囲を0~1に変更
warai_img = warai_img[:,:,:3] # アルファチャンネルは必要ない

if len(faces) > 0:
    for rect in faces:
        # 顔部分の縦横サイズ
        rect_w = rect[2]
        rect_h = rect[3]

        # 笑い画像を顔部分の縦横にリサイズ
        resized_overlay_image = cv2.resize(warai_img, (rect_w, rect_h))
        resized_overlay_image_h, resized_overlay_image_w = resized_overlay_image.shape[:2]

        # マスクを笑い画像に合わせてリサイズ
        resized_mask = cv2.resize(mask, (rect_w, rect_h))

        # 笑い画像からマスクで顔部分だけ抽出して元画像に描画する
        base_img[rect[1]:(rect[1] + resized_overlay_image_h), rect[0]:(rect[0]+resized_overlay_image_w)] *= (1-resized_mask).astype(base_img.dtype);
        base_img[rect[1]:(rect[1] + resized_overlay_image_h), rect[0]:(rect[0]+resized_overlay_image_w)] += (resized_overlay_image*resized_mask).astype(base_img.dtype);

    cv2.imwrite("../images/warai_on_image.jpg", base_img)
