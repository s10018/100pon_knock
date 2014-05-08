# -*- coding: utf-8 -*-
import sys

s = set([])
for line in sys.stdin:
    s.add(line.rstrip().split("\t")[0])
print len(s)


''' 補足(蛇足)
Linuxとかのコマンドは入力と出力を繋げることができる
「|」でコマンドを繋げることでで可能になる
cut -f 1 address.txt | sort | uniq | wc -l
'''

''' 確認の仕方
python ex7.py < address.txt | sort > uniq1.txt  # ソートしないと一致しない
cut -f 1 address.txt | sort | uniq

'''
