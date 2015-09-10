#!/bin/sh

cat | python -c "import sys, HTMLParser; print HTMLParser.HTMLParser().unescape(sys.stdin.read().decode('utf-8')).encode('utf-8')" | grep '<AbstractText' | perl -npe 's#.*<AbstractText.*?>(.*?)</AbstractText>.*#\1#g' | nkf -w
