# TODO: (20)

なんとなくやるせないので
http://apps.timwhitlock.info/emoji/tables/unicode
見ながら書き直す

# (20)の解釈

絵文字は顔文字として書いてます....`(´・ω・｀)`やなど
http://www.chokkan.org/publication/coding-for-researchers.pdf
を見る限り絵文字は絵文字？っぽいですね

# tweet.txt.gzの場所

`tweet.txt.gz`のサイズがでかいのでこのディレクトリとは場所に置きました．
でも毎回パスを引数で指定するのは面倒くさいです．なので場所はコードベタ書きにしました．

`root`には`tweet.txt.gz`の場所を書いてます．パスばれ嫌なのでpit使いました．
意味がわからない人はとりあえず
```
root = pit.Pit().get("path")
```
を
```
root = '.'
```
にして`tweet.txt.gz`はこのディレクトリに置いて下さい．

※ ディレクトリ ≒ フォルダ
