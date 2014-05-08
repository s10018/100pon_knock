# -*- coding: utf-8 -*-
import sys

with open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
    for line in sys.stdin:
        col = line.rstrip("\n").split("\t")
        col1.write(col[0] + "\n")
        col2.write(col[1] + "\n")

''' 確認の仕方
python ex3.py < address.txt
cut -f 1 address.txt > cut1.txt
cut -f 2 address.txt > cut2.txt
diff col1.txt cut1.txt
diff col2.txt cut2.txt
(何も出力がない -> 答えが一緒)
'''
