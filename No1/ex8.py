# -*- coding: utf-8 -*-
import sys

lines = []
for line in sys.stdin:
    ll = line.rstrip().split("\t")
    if len(ll) == 1:
        ll.append("")  # 上記書き方だと["一列目"]ができる可能性がある
    lines.append(ll)

for line in sorted(lines, key=lambda x: x[1]):
    print "\t".join(line)

''' 確認の仕方
python ex8.py < address.txt > sort1.txt
sort -k 2 address.txt > sort2.txt # ??
diff sort1.txt sort2.txt # .....?
(一緒にならない...)
'''
