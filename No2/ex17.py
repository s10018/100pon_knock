# -*- coding: utf-8 -*-
import gzip
import re
import pit

root = pit.Pit().get("100pon")["path"]

with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        data = re.findall(u'([一-龠ぁ-んァ-ヴ]+)(ちゃん|さん|くん|君|氏)', tweet)
        if len(data) > 0:
            for a, b in data:
                print u"{}{}".format(a, b).encode("UTF-8")

'''
1行に抽出した名前っぽいものをそのまま出力します．
'''
