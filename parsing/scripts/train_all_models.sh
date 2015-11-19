#! /usr/bin/bash
#  You must be in the virtualenv ($ workon pln-2015) to run this script
SCRIPT_DIR="$(dirname $0)"
mkdir $SCRIPT_DIR/../models
M=$SCRIPT_DIR/../models
# ORIGINAL_DIR="$(pwd)"


echo -n > $M/train_output.txt
echo "Redirecting output to $M/train_output.txt"
echo "Working..."

echo "Training flat..."
{ time -p python $SCRIPT_DIR/train.py -m flat -o $M/flat >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training rbranch..."
{ time -p python $SCRIPT_DIR/train.py -m rbranch -o $M/rbranch >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training lbranch..."
{ time -p python $SCRIPT_DIR/train.py -m lbranch -o $M/lbranch >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training upcfg..."
{ time -p python $SCRIPT_DIR/train.py -m upcfg -o $M/upcfg >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training upcfg-horzM=0..."
{ time -p python $SCRIPT_DIR/train.py -m upcfg -n 0 -o $M/upcfg-horzM=0 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training upcfg-horzM=1..."
{ time -p python $SCRIPT_DIR/train.py -m upcfg -n 1 -o $M/upcfg-horzM=1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training upcfg-horzM=2..."
{ time -p python $SCRIPT_DIR/train.py -m upcfg -n 2 -o $M/upcfg-horzM=2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training upcfg-horzM=3..."
{ time -p python $SCRIPT_DIR/train.py -m upcfg -n 3 -o $M/upcfg-horzM=3 >> $M/train_output.txt ;} 2>> $M/train_output.txt