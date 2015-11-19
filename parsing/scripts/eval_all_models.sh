#! /usr/bin/bash
#  You must be in the virtualenv ($ workon pln-2015) to run this script
SCRIPT_DIR="$(dirname $0)"
mkdir $SCRIPT_DIR/../models
M=$SCRIPT_DIR/../models
# ORIGINAL_DIR="$(pwd)"


echo -n > $M/eval_output.txt
echo "Redirecting output to $M/eval_output.txt"
echo "Working..."

echo "Evaluate flat..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/flat >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate rbranch..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/rbranch >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate lbranch..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/lbranch >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate upcfg..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/upcfg >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate upcfg-horzM=0..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/upcfg-horzM=0 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate upcfg-horzM=1..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/upcfg-horzM=1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate upcfg-horzM=2..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/upcfg-horzM=2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate upcfg-horzM=3..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -m 20 -i $M/upcfg-horzM=3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt