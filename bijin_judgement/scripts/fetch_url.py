# top levelをパスに含める
import sys
sys.path.append('/Users/razokulover/src/github.com/image-processing-training-with-python/bijin_judgement')

import urllib.request
import json
import re
import time
import mysql.connector
from db import DB

print('===[{current_time}] Start fetch_url ==='.format(current_time=time.strftime('%Y-%m-%d %H:%M:%S')))

# db接続
dbh = DB()
stmt = dbh.cursor()

# APIで100件ずつ取得して重複を無視してDBにバルクインサートする
for i in range(10):
    # 画像を取得する
    url = "http://bjin.me/api/?type=rand&count=100&format=json"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

    # レスポンスに改行とかゴミが含まれてるので取り除く
    json_string = response.read().strip().decode('utf-8')
    pat = re.compile('^b')
    pat.sub('', json_string)
    data = json.loads(json_string)

    # insertする値をまとめる
    values = []
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    for d in data:
        value = "({id}, '{link}', '{category}', '{thumb}', '{modified}', '{created}')".format(id=int(d['id']), link=d['link'], category=d['category'], thumb=d['thumb'], modified=timestamp, created=timestamp)
        values.append(value)

    # 挿入
    joined_values = ','.join(values)
    sql = "insert ignore into bijins(bijin_id, link, category, thumb, modified, created) values" + joined_values # bijin_idの重複時は無視(mysql独自拡張)
    stmt.execute(sql)

    time.sleep(3)

stmt.close()
dbh.close()
