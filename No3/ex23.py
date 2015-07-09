# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    for w in line.split(' '):
        print w
    print
