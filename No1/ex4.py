# -*- coding: utf-8 -*-

with open("col1.txt") as col1, open("col2.txt") as col2:
    for c1, c2 in zip(col1, col2):
        c1 = c1.rstrip()
        c2 = c2.rstrip()
        print "{}\t{}".format(c1, c2)

''' 補足
zip http://docs.python.jp/2/library/functions.html#zip
zip(['a', 'b', 'c'], ['d', 'e', 'f']) -> [('a', 'd'), ('b', 'e'), ('c', 'f')]
str.format http://docs.python.jp/2/library/stdtypes.html#str.format
'''

''' 確認の仕方
python ex4.py > col_merge1.txt
paste col1.txt col2.txt > col_merge2.txt
diff col_merge1.txt col_merge2.txt
(何も出力がない -> 答えが一緒)
'''
