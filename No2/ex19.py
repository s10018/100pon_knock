# -*- coding: utf-8 -*-
import gzip
import re
import pit

root = pit.Pit().get("100pon")["path"]

with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        data = re.findall(
            u'(〒[0-9]+-[0-9]+)\s*(\w{2,}?)(都|道|府|県)\s*(\w+)(市|町|村|区)',
            tweet, re.U)
        if len(data) > 0:
            for a, b, c, d, e in data:
                print u"{} {}{} {}{}".format(
                    a, b, c, d, e
                ).encode("UTF-8")

'''
1行に抽出した住所を
郵便番号 都道府県名 市町村区名
のフォーマットで出力します．区を入れたのはなんとなくです

\w{2,}? は "京都府京都市"を上手くマッチさせるために下限2にしました...
\w+  京都府京都 市〜 ×
\w+? 京都 府京都市〜 ×
\w{2,}? 京都府 京都市〜 ◯
'''
