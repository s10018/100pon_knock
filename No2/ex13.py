# -*- coding: utf-8 -*-
import gzip
import pit

root = pit.Pit().get("100pon")["path"]

with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        if u"RT" in tweet and not tweet.startswith("RT"):
            comment = tweet[:tweet.index(u"RT")]
            print comment

'''
1行1ツイートそのまま出力します．
'''
