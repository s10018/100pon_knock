# -*- coding: utf-8 -*-
import sys
import kyotocabinet as kc

db = kc.DB()
if not db.open("ngram_db.kch", kc.DB.OWRITER | kc.DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

for line in sys.stdin:
    words = line.rstrip("\n").split(" ")
    all_prob = 1.0
    for i in range(len(words) - 1):
        prob = db.get(words[i] + " " + words[i + 1])
        if prob is None:
            prob = 0.0
        all_prob = all_prob * float(prob)
    print "{}\t{}".format(all_prob, line.rstrip("\n"))

db.close()

'''
実行例:
echo "this paper is organized as follows" | python ex40.py
2.54197614097e-11       this paper is organized as follows
'''
