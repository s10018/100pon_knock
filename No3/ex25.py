# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    w = line.rstrip('\n')
    print "{}\t{}".format(w, w.lower())
