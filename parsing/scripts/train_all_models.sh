#! /usr/bin/bash

mkdir models
echo -n > models/train_output.txt
echo "Redirecting output to models/train_output.txt"
echo "Working..."
{ time -p python3.4 train.py -m flat -o models/flat >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m rbranch -o models/rbranch >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m lbranch -o models/lbranch >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m upcfg -o models/upcfg >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m upcfg -n 0 -o models/upcfg-horzM=0 >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m upcfg -n 1 -o models/upcfg-horzM=1 >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m upcfg -n 2 -o models/upcfg-horzM=2 >> models/train_output.txt ;} 2>> models/train_output.txt
{ time -p python3.4 train.py -m upcfg -n 3 -o models/upcfg-horzM=3 >> models/train_output.txt ;} 2>> models/train_output.txt