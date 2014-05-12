# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

counter = defaultdict(lambda: 0)
for line in sys.stdin:
    line = line.rstrip()
    counter[line] = counter[line] + 1

try:
    for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        print("{:4d} {}".format(v, k))
        sys.stdout.flush()
except:
    exit(1)

''' 確認の仕方
python ex10.py < col2.txt | sort > hist1.txt
sort col2.txt | uniq -c | sort -k 2,1 -n -r > hist2.txt
diff hist1.txt hist2.txt
(同じ頻度のソートでうまくいかない可能性あり)
'''
