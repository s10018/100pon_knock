# -*- coding: utf-8 -*-
import gzip
import re
import pit

root = pit.Pit().get("100pon")["path"]

hidari = u'(?:ヾ|m|w|⊂|◯|o|Σ|\\|ゝ|「)?'
kakko_hidari = u'(?:\(|（)'
center = u'(?:\s|；|□|Φ|「|@|ゝ|#|q|⊃|≡|∩|⊂|T|o|∇|\^|￣|w|ω|>|<|\*|・|=|ε|μ|;|-|_|≧|≦|￣|ー|Д|゜|∀|´|｀|;|＞|＜){2,}'
kakko_migi = u'(?:\)|）)'
migi = u'(?:◯|o|/|⊃|m|=3|w|「|丿|σ|ﾉ|ｼ)?'
kaomoji = u'(' + kakko_hidari + hidari + center + migi + kakko_migi + u')'
kaomoji_re = re.compile(kaomoji)


kaomoji_set = set()
with gzip.open(root + "/tweets.txt.gz") as tweets:
    for tweet in tweets:
        tweet = unicode(tweet.rstrip(), "UTF-8")
        kaomoji_set.update(kaomoji_re.findall(tweet, re.U))

for s in kaomoji_set:
    print u"{}".format(s).encode("UTF-8")

'''
1行に抽出した顔文字っぽいものを出力します．
2962種類抽出(ノイズ含む)
'''
