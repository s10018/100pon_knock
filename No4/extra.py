# -*- coding: utf-8 -*-
import marshal
import sys

'''
簡易辞書検索システム
'''

sys.stdout.write("Loading dict.....")
sys.stdout.flush()
dic = marshal.load(open('dict.marshal', 'rb'))
sys.stdout.write("done.\n")
sys.stdout.flush()

print("SYS: input any word, 'q' or break line quit.")
while True:
    word = raw_input(">>> ")
    if word == "" or word == "q":
        break
    if word in dic:
        for inf in dic[word]:
            print "\t" + "\t".join(inf)
    else:
        print "SYS: no word"
