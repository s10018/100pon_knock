# -*- coding: utf-8 -*-
import sys
import marshal

dic = marshal.load(open('dict.marshal', 'rb'))

no_conteined_words = set()

for word in sys.stdin:
    word = word.rstrip().split("\t")[0]
    if dic.get(word, 0) != 0:
        continue
    no_conteined_words.add(word)

for word in no_conteined_words:
    print word
