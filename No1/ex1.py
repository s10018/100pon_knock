# -*- coding: utf-8 -*-
import sys

count = 0
for line in sys.stdin:
    count += 1
print count

''' 補足
標準入力:
一般的にLinuxではキーボード入力のことを指す
「標準入力から標準入力からタブ区切り形式のテキストを読み込み」というのは
プログラム < テキスト
という風にして読み込みましょうという意味である．このプログラムなら
python ex1.py < address.txt
という風にする．
「<」によって「キーボード入力」から「ファイル」に標準入力を切り替えてください，という意味になる
'''
''' 確認の仕方
python ex1.py < address.txt
wc -l adress.txt
(出力が一緒 = OK)
'''
