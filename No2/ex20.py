# -*- coding: utf-8 -*-
import re
import sys


# refer to https://vazor.com/unicode/index.html

msap = r'\xF0\x9F[\x8c-\x9b][\x00-\xff]'
emoji_re = re.compile(r'(' + r'|'.join([msap]) + r')')


emoji_set = set()
with sys.stdin as tweets:
    for tweet in tweets:
        emoji_set.update(emoji_re.findall(tweet))

for s in emoji_set:
    print "{}".format(s)

'''
1行に抽出した絵文字っぽいものを出力します．
'''
