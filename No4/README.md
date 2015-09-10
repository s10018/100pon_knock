
# 使用ファイル

- `infrection.table.txt`
  - http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lexicon/current/web/release/2015.html にあるもの (inflection.table(ASCII))
  ```
  wget http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lexicon/2015/release/LEX/ASCII/inflection.table.ascii -O inflection.table.txt
  ```

- `../No3/medline.txt.sent.tok.stem`
  - 第四セット前半(33)で使う (使えなくてもいい..)
  - 第三セット(30)より出力

- `../No3/medline.txt.sent.tok`
- 第四セット後半(36)で使う
  - 第三セット(25)より出力


# 使用ライブラリ

- Kyoto Cabinet (http://fallabs.com/kyotocabinet/index.ja.html)
  - 別途kyotocabinetはインストール済みであること (Macなら以下でインストール可能)
  ```
  brew install kyoto-cabinet
  ```
  - pythonのライブラリは以下でインストール可能
  ```
  pip install http://fallabs.com/kyotocabinet/pythonlegacypkg/kyotocabinet-python-legacy-1.18.tar.gz
  ```
