

# medline.txtの作り方

## 地道な方法

以下のように実行するとmedline.txt 完成 (`extract_medline_abstract.sh` はディレクトリ内のを用いる)

1. ひたすら `http://www.ncbi.nlm.nih.gov/pubmed`でformat(XML)をコピペで手に入れる
2. 以下を実行

```
cat あつめたデータ | ./extract_medline_abstract.sh > medline.txt
```

## 楽な方法
1. [@s10018](https://twitter.com/s_10018 )に問い詰めてmedline.txtを手に入れる

15/09/11: `get_medline_abstract.sh`動かなかったから削除...

## 必要ツール

- nkf

# (27), (28)

```
chmod u+x ex27.sh
./ex27.sh
```

```
chmod u+x ex28.sh
./ex28.sh
```

# (29)

- stemmingのインストール

```
pip install stemming
```


# medline.txt.sentの作り方

```
python ex22.py < medline.txt > medline.txt.sent
```
# medline.txt.sent.tokの作り方

```
python ex24.py < medline.txt.sent > medline.txt.sent.tok
```

# medline.txt.sent.tok.stemの作り方

```
python ex30.py < medline.txt.sent.tok > medline.txt.sent.tok.stem
```
