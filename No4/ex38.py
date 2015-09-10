# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

uni_count = defaultdict(lambda: 0)
bi_count = defaultdict(lambda: 0)

for line in sys.stdin:
    items = line.rstrip("\n").split("\t")
    hist = int(items[0])
    bi_count[(items[1], items[2])] = hist
    uni_count[items[1]] += hist

for words, hist in bi_count.items():
    print "{:07f}\t{}\t{}".format(
        float(hist) / uni_count[words[0]], words[0], words[1]
    )

'''
計算方法:

ある単語wに続く単語zの条件付き確率は

P(z|w) = count(w, z) / count(w)

で求める．count(w, z)はwにつづいてzが続いたものの頻度 ((37) で求める),
count(w) は wが出現した頻度 (丁度連接の「前にある時」の数の総和と一致) になる

実行例:
python ex36.py < ../No3/medline.txt.sent.tok | python ex37.py | python ex38.py

フォーマット:
(連接の確率)\t(現在の単語)\t(次の単語)
(連接の確率)\t(現在の単語)\t(次の単語)
...
...
'''
