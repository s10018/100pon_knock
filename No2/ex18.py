# -*- coding: utf-8 -*-
import sys
import re

with sys.stdin as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        data = re.findall(u'(仙台市[一-龠]+?区[一-龠]+?町)', tweet)
        if len(data) > 0:
            for a in data:
                print u"{}".format(a).encode("UTF-8")

'''
1行に抽出した住所をそのまま出力します．
'''
