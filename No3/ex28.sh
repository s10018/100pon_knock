#!/bin/sh

python ex28.py < medline.txt.sent.tok | python ../No1/ex10.py | head -n 100

