# -*- coding: utf-8 -*-
import sys
from collections import defaultdict


dic = defaultdict(lambda: [])

with open('inflection.table.txt') as data:
    for line in data:
        info = line.rstrip().split('|')
        dic[info[0]].append((info[1], info[3], info[6]))

for word in sys.stdin:
    word = word.rstrip()
    if dic.get(word, 0) == 0:
        print "{} (counts: {})".format(word, 0)
        continue
    print "{} (counts: {})".format(word, )
    for info in dic[word]:
        print "\t{}\t{}\t{}".format(info[0], info[1], info[2])
