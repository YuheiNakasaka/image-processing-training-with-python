# Image Processing Training with Python

Pythonで画像処理のコードを書いていくレポジトリ

# 環境

- PC: MacBook Pro(Retina 13-inch、Early 2015)
- メモリ: 16 GB
- Python 3.5.2 :: Anaconda custom (x86_64)
- OpenCV 3.1.0

# 環境構築

Homebrew環境は整っている前提で。

### 1) pyenv入れる

Pythonのバージョンを切り替えるやつ。XXenv系のPython版。

```
$ brew install pyenv
$ echo 'export PYENV_ROOT="${HOME}/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="${PYENV_ROOT}/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile # zshの人は各自やる
$ exec $SHELL -l
```

### 2) Anacondaのインストール

Pythonを含め、データ解析や機械学習に関するライブラリの全部詰め合わせパッケージ。

Pythonは3系を使う(最近の書籍はだいたい3系前提で書かれてる事多いので)

```
pyenv install anaconda3-4.0.0
pyenv global anaconda3-4.0.0
```

### 3) インストールできたか確認

Python 3.5.2 :: Anaconda custom (x86_64)が出ればOK。

```
python --version
```

### 4) OpenCV3を入れる

```
conda install -c https://conda.anaconda.org/menpo opencv3
```

### 参考
- [HomebrewのインストールからpyenvでPythonのAnaconda環境構築までメモ](http://qiita.com/oct_itmt/items/2d066801a7464a676994)



# ハマりどころ

## OpenCV3を使おうとするとエラーが出る

import cv2したコードを実行すると以下のようなエラーを吐く。

```
〜Library not loaded: @rpath/libhdf5.10.dylib
Reason: Incompatible library version: libopencv_hdf.3.1.dylib requires version 12.0.0 or later, but libhdf5.10.dylib provides version 11.0.0
```

hdf5をアップデートする。

```
conda update hdf5
```

- [https://github.com/ContinuumIO/anaconda-issues/issues/826](https://github.com/ContinuumIO/anaconda-issues/issues/826)
