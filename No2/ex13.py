# -*- coding: utf-8 -*-
import sys

with sys.stdin as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        if u"RT" in tweet and not tweet.startswith("RT"):
            comment = tweet[:tweet.index(u"RT")]
            print comment

'''
RT含むツイートの内容をそのまま1行に出力します

ほげ RT @huga: うおお
うわぁ RT @huga: ？？？？

は

ほげ
うわぁ

になります
'''
