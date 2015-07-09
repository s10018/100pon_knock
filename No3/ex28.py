# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    words = line.rstrip('\n').split('\t')
    if len(words) < 2:
        continue
    word = words[1].decode('utf-8')
    for i in range(len(word) - 1):
        print(word[i:i + 2].encode('utf-8'))
        sys.stdout.flush()
