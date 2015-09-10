# -*- coding: utf-8 -*-
import sys
import marshal
from collections import defaultdict


dic = defaultdict(lambda: [])

with open('inflection.table.txt') as data:
    for line in data:
        info = line.rstrip().split('|')
        dic[info[0]].append((info[1], info[3], info[6]))

with open('dict.marshal', 'wb') as d:
    marshal.dump(dict(dic), d)
print >> sys.stderr, "saved dict.marshal"
