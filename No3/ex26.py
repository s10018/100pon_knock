# -*- coding: utf-8 -*-
import sys

ly_set, ness_set, origin_set = set(), set(), set()

for line in sys.stdin:
    word = line.rstrip('\n')
    if word.endswith('ly'):
        ly_set.add(word[:-2])
        origin_set.add(word[:-2])
    elif word.endswith('ness'):
        ness_set.add(word[:-4])
        origin_set.add(word[:-4])


for word in origin_set:
    if word in ly_set and word in ness_set:
        print word
