# Beautiful Soup と urllibで画像クロールしてダウンロード
# BeautifulSoupの絞込参考) http://qiita.com/itkr/items/513318a9b5b92bd56185

from bs4 import BeautifulSoup
import urllib.request
import os.path

# 画像をダウンロードする場所を作る
image_dir = './images'
if os.path.exists(image_dir) == False:
    os.mkdir(image_dir)

# 画像を取得する
url = 'http://gifmagazine.net/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml") # lxmlを付けないとwarningでる

# 画像urlを取得
urls = []
images = soup.select('.home20160502-wrap-list-top-link img')
for image in images:
    urls.append(image.get('src'))

# 画像をダウンロードする
for url in urls:
    try:
        ulist = url.split("/")
        output_file_path = image_dir + '/' + ulist[len(ulist)-1]
        response = urllib.request.urlopen(url)
        f = open(output_file_path, 'wb')
        f.write(response.read())
        f.close()
    except Exception:
        print('error')
