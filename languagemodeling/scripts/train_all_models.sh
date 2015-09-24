#!/bin/bash

python3.4 train.py -m ngram -n 1 -o n1
python3.4 train.py -m ngram -n 2 -o n2
python3.4 train.py -m ngram -n 3 -o n3
python3.4 train.py -m ngram -n 4 -o n4
python3.4 train.py -m addone -n 1 -o a1
python3.4 train.py -m addone -n 2 -o a2
python3.4 train.py -m addone -n 3 -o a3
python3.4 train.py -m addone -n 4 -o a4
python3.4 train.py -m interpolated -n 1 -o i1
python3.4 train.py -m interpolated -n 2 -o i2
python3.4 train.py -m interpolated -n 3 -o i3
python3.4 train.py -m interpolated -n 4 -o i4
python3.4 train.py -m backoff -n 1 -o b1
python3.4 train.py -m backoff -n 2 -o b2
python3.4 train.py -m backoff -n 3 -o b3
python3.4 train.py -m backoff -n 4 -o b4