# -*- coding: utf-8 -*-
import sys
import string

alphabet = string.ascii_letters + string.digits

for line in sys.stdin:
    line = line.rstrip('\n').decode('utf-8')
    for word in line.split(' '):
        if len(word) == 0:
            print word
            continue
        w, symbols = word[-1], []
        while len(word) > 1 and w not in alphabet:
            symbols.insert(0, w)
            word = word[:-1]
            w = word[-1]
        print word.encode('utf-8')
        for s in symbols:
            print s.encode('utf-8')
    print
