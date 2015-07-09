# -*- coding: utf-8 -*-
import sys
from stemming.porter2 import stem


for line in sys.stdin:
    line = line.rstrip('\n')
    words = line.split('\t')
    if len(words) < 2:
        print line
        continue
    print line + "\t" + stem(words[1])
