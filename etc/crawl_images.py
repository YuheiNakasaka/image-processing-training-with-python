# 画像をクローリングする

# 単純なやつ
# 画像urlのマッチすらむずい
import re
import urllib.request as ulibreq
import urllib.error as uliberr

url = "http://gifmagazine.net/"
response = ulibreq.urlopen(url)

pattern = re.compile('<img src=(.+?)>')
html = response.read().decode('utf-8')
matches = pattern.findall(html)

for m in matches:
    print(m)
