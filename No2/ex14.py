# -*- coding: utf-8 -*-
import gzip
import re
import pit

root = pit.Pit().get("100pon")["path"]

with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        obj = re.findall(r"@\w+", tweet)
        for o in obj:
            print o

'''
抽出の仕方は適当です．
---
@abc @cde ！！！
@aaa ほげほげ
@cde ふがふが
---
なら
---
@abc
@cde
@aaa
@cde
---
になります．つまり，ツイート中の@は全部抽出して並べます．重複あります．
...
'''
