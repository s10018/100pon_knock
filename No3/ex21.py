# -*- coding: utf-8 -*-
import sys


for line in sys.stdin:
    line = line.lstrip().rstrip('\n')
    tmp_line = ''
    for w in line:
        tmp_line += w
        if w == '.':
            print tmp_line
            tmp_line = ''
    if tmp_line != '':
        print tmp_line
