# -*- coding: utf-8 -*-
import sys
import kyotocabinet as kc

db = kc.DB()
if not db.open("ngram_db.kch", kc.DB.OWRITER | kc.DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

for line in sys.stdin:
    line = line.rstrip("\n")
    items = line.split("\t")
    words, prob = items[1] + " " + items[2], float(items[0])
    db.set(words, prob)
db.close()

'''
実行例:
python ex36.py < ../No3/medline.txt.sent.tok | python ex37.py | python ex38.py | python ex39.py

確認:
kcpolymgr get ngram_db.kch "and glulisine"

'''
