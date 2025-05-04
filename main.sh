#! /usr/bin/env bash

python3 src/main.py
python3 -m http.server -d docs 8888
