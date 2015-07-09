# -*- coding: utf-8 -*-
import sys
import string

alphabet = string.ascii_uppercase

for line in sys.stdin:
    line = line.rstrip('\n').decode('utf-8')
    prev_pos = 0
    for i, w in enumerate(line):
        if (i == 0 or i + 1 == len(line)):
            continue
        if (
            line[i - 1] == '.' and
            line[i] == ' ' and line[i + 1] in alphabet
        ):
            print line[prev_pos:i].encode('utf-8')
            prev_pos = i + 1
    if prev_pos != len(line):
        print line[prev_pos:].encode('utf-8')
