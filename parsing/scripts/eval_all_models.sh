#! /usr/bin/bash

mkdir models
echo -n > models/eval_output.txt
echo "Redirecting output to models/eval_output.txt"
echo "Working..."
{ time -p python3.4 eval.py -m 20 -i models/flat >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/rbranch >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/lbranch >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/upcfg >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/upcfg-horzM=0 >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/upcfg-horzM=1 >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/upcfg-horzM=2 >> models/eval_output.txt ;} 2>> models/eval_output.txt
{ time -p python3.4 eval.py -m 20 -i models/upcfg-horzM=3 >> models/eval_output.txt ;} 2>> models/eval_output.txt