# -*- coding: utf-8 -*-
import sys

with sys.stdin as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        if tweet.endswith(u"なう"):
            print tweet

'''
なうが末尾に来るツイートをそのまま1行出力します．
'''
