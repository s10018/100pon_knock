#!/bin/sh

cut -f 2 < medline.txt.sent.tok | python ../No1/ex10.py | head -n 100
