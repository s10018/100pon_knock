# -*- coding: utf-8 -*-
import gzip
import re
import pit

root = pit.Pit().get("100pon")["path"]

with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        print re.sub(
            r"@(\w+)",
            r'<a href="https://twitter.com/#!/\1">@\1</a>',
            tweet
        ).encode("UTF-8")

'''
1行1ツイートで置換した結果を出力します．
--
@hoge やぁ
を
<a href="https://twitter.com/#!/hoge">@hoge</a> やぁ
にします
'''
