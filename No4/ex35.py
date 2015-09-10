# -*- coding: utf-8 -*-
import sys
import marshal

dic = marshal.load(open('dict.marshal', 'rb'))
for word in sys.stdin:
    word = word.rstrip().split("\t")[0]
    if dic.get(word, 0) == 0 or len(dic[word]) < 3:
        continue
    print "{} (counts: {})".format(word, len(dic[word]))
    for info in dic[word]:
        print "\t{}\t{}\t{}".format(info[0], info[1], info[2])
