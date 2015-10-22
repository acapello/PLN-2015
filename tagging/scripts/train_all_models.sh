#!/bin/bash

mkdir models
time -p python3.4 train.py -m base -o models/base
time -p python3.4 train.py -m mlhmm -n 1 -o models/mlhmm-1
time -p python3.4 train.py -m mlhmm -n 2 -o models/mlhmm-2
time -p python3.4 train.py -m mlhmm -n 3 -o models/mlhmm-3
time -p python3.4 train.py -m mlhmm -n 4 -o models/mlhmm-4
time -p python3.4 train.py -m memm -n 1 -c logreg -o models/memm-logreg-1
time -p python3.4 train.py -m memm -n 2 -c logreg -o models/memm-logreg-2
time -p python3.4 train.py -m memm -n 3 -c logreg -o models/memm-logreg-3
time -p python3.4 train.py -m memm -n 4 -c logreg -o models/memm-logreg-4
time -p python3.4 train.py -m memm -n 1 -c nb -o models/memm-nb-1
time -p python3.4 train.py -m memm -n 2 -c nb -o models/memm-nb-2
time -p python3.4 train.py -m memm -n 3 -c nb -o models/memm-nb-3
time -p python3.4 train.py -m memm -n 4 -c nb -o models/memm-nb-4
time -p python3.4 train.py -m memm -n 1 -c svc -o models/memm-svc-1
time -p python3.4 train.py -m memm -n 2 -c svc -o models/memm-svc-2
time -p python3.4 train.py -m memm -n 3 -c svc -o models/memm-svc-3
time -p python3.4 train.py -m memm -n 4 -c svc -o models/memm-svc-4