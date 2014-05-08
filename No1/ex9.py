# -*- coding: utf-8 -*-
import sys

lines = []
for line in sys.stdin:
    ll = line.rstrip().split("\t")
    if len(ll) == 1:
        ll.append("")
    lines.append(ll)

for line in sorted(lines, key=lambda x: (x[1], x[0]), reverse=True):
    print "\t".join(line)

''' 確認の仕方
python ex9.py < address.txt > sort1.txt
sort -r -k 2,1 address.txt > sort2.txt
diff sort1.txt sort2.txt
(一緒にならない...)
'''
