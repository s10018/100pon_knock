# -*- coding: utf-8 -*-
import gzip
import re
import pit

root = pit.Pit().get("100pon")["path"]

with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        data = re.findall(u'([一-龠]+)\(([A-Z]+)\)', tweet)
        if len(data) > 0:
            for a, b in data:
                print u"{}\t{}".format(a, b).encode("UTF-8")

'''
厨二病(タブ)笑
無(タブ)´・ω・｀
...
みたいに抽出した「漢字\t括弧の中身」というフォーマットで出力します．
'''
