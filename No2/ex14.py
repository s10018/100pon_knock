# -*- coding: utf-8 -*-
import sys
import re

with sys.stdin as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        obj = re.findall(r"(@\w+)", tweet)  # 頑張らない
        # obj = re.findall(r"@(?!RT\s|RT$)\w+", tweet) # ちょっと頑張る
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
