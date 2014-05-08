# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 2:
    print "ERROR: python ex6.py N"
    exit(1)

n = int(sys.argv[1])
stack_line = []
for line in sys.stdin:
    stack_line.append(line.rstrip())

for line in stack_line[len(stack_line) - n:]:
    print line

''' 確認の仕方
python ex6.py 5 < address.txt > tail1.txt
tail -n 5 address.txt > tail2.txt
diff tail1.txt tail2.txt
(何も出力がない -> 答えが一緒)
'''
