

# medline.txtの作り方

以下のように実行するとmedline.txt 完成 (`extract_medline_abstract.sh` はディレクトリ内のを用いる)

```
chmod u+x extract_medline_abstract.sh
./extract_medline_abstract.sh > medline.txt
```

※ 短時間で頻繁に実行しないこと

## 必要ツール

- curl (だいたいあると思う)
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
python ex24.py < medline.txt.sent | python ex25.py > medline.txt.sent.tok
```

# medline.txt.sent.tok.stemの作り方

```
python ex30.py < medline.txt.sent.tok > medline.txt.sent.tok.stem
```
