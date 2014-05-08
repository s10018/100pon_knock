# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 2:
    print "ERROR: python ex6.py N"
    exit(1)

n = int(sys.argv[1])
for i, line in enumerate(sys.stdin):
    if i == n:
        break
    print line.rstrip()   # print は 改行が はいる

''' 補足
コマンドライン引数:
コマンドを実行するときに指定するもの．
例えば`ls hoge`としたときの`hoge`，`cd hoge` の`hoge`は引数．
コマンドライン引数は import sys を書いて sys.argv で取得可能
sys.argv[0] は プログラム名，sys.argv[1] から 実際の引数になる
'''
''' 確認の仕方
python ex5.py 5 < address.txt > head1.txt
head -n 5 address.txt > head2.txt
diff head1.txt head2.txt
(何も出力がない -> 答えが一緒)
'''
