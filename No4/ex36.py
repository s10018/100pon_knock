# -*- coding: utf-8 -*-
import sys

words = []
for line in sys.stdin:
    word = line.rstrip()
    if word == "":
        for i in range(len(words) - 1):
            print "{}\t{}".format(words[i], words[i + 1])
        words = []
    else:
        words.append(word)

'''
フォーマット:
(現在の単語)\t(次の単語)
(現在の単語)\t(次の単語)
...
   # 文の終わりに空行
(現在の単語)\t(次の単語)
(現在の単語)\t(次の単語)
...
'''
