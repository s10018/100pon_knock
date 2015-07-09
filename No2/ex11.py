# -*- coding: utf-8 -*-
import sys

with sys.stdin as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        if u"拡散希望" in tweet:
            print tweet.encode("UTF-8")


'''
拡散希望含むツイートをそのまま1行出力します．
'''
