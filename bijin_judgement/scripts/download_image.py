# top levelをパスに含める
import sys
sys.path.append('/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement')

import urllib.request
import time
import os
import mysql.connector
from db import DB

print('===[{current_time}] Start download_image ==='.format(current_time=time.strftime('%Y-%m-%d %H:%M:%S')))

# db接続
dbh = DB()
stmt = dbh.cursor()

# 画像をダウンロードする場所を作る
image_dir = '/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement/images'
if os.path.exists(image_dir) == False:
    os.mkdir(image_dir)

# dbから画像urlを取得してダウンロードする
sql = "select id, bijin_id from bijins where status = 0 order by id asc"
stmt.execute(sql)
for row in stmt.fetchall():
    id = row[0]
    bijin_id = row[1]
    url = "http://bjin.me/images/pic{bijin_id}.jpg".format(bijin_id=bijin_id)
    filename = "{bijin_id}.jpg".format(bijin_id=bijin_id)
    image_path = image_dir + '/' + filename
    print("id: {id}, bijin_id: {bijin_id}".format(id=id, bijin_id=bijin_id))

    # ダウンロード処理
    try:
        response = urllib.request.urlopen(url)
        f = open(image_path, 'wb')
        f.write(response.read())
        f.close()

        # download済みは更新
        sql = "update bijins set status = {status} where bijin_id = {bijin_id}".format(status=1, bijin_id=bijin_id)
        stmt.execute(sql)
    except Exception:
        print('error')

    time.sleep(2)

stmt.close()
dbh.close()
