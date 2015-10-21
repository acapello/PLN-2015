#!/bin/bash

echo '' > eval_output.txt
time -p python3.4 eval.py -i models/base >> eval_output.txt
time -p python3.4 eval.py -i models/mlhmm-1 >> eval_output.txt
time -p python3.4 eval.py -i models/mlhmm-2 >> eval_output.txt
time -p python3.4 eval.py -i models/mlhmm-3 >> eval_output.txt
time -p python3.4 eval.py -i models/mlhmm-4 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-logreg-1 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-logreg-2 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-logreg-3 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-logreg-4 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-nb-1 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-nb-2 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-nb-3 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-nb-4 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-svc-1 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-svc-2 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-svc-3 >> eval_output.txt
time -p python3.4 eval.py -i models/memm-svc-4 >> eval_output.txt