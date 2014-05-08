# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    line = line.rstrip("\n")  # 末尾の改行「だけ」除く
    print line.replace("\t", " ")


''' 補足(蛇足)
「標準出力」は画面に表示させるのが一般的となっている
「>」はこの「標準入力」を「>」の先に切り替えて書き込んでね．という意味になる
'''

''' 確認の仕方
python ex2.py < address.txt > address_sp.txt
tr "\t" " " < address.txt > address_sp1.txt
diff address_sp.txt address_sp1.txt
(何も出力がない -> 答えが一緒)
'''
