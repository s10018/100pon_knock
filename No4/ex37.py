# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

count_dict = defaultdict(lambda: 0)
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        continue
    count_dict[line] += 1

for words, hist in count_dict.items():
    print "{}\t{}".format(hist, words)

'''
実行例:
python ex36.py < ../No3/medline.txt.sent.tok | python ex37.py

フォーマット:
(連接の頻度)\t(現在の単語)\t(次の単語)
(連接の頻度)\t(現在の単語)\t(次の単語)
...
...
'''
