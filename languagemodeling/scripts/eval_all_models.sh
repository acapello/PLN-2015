#! /usr/bin/bash
#  You must be in the virtualenv ($ workon pln-2015) to run this script
SCRIPT_DIR="$(dirname $0)"
mkdir $SCRIPT_DIR/../models
M=$SCRIPT_DIR/../models
# ORIGINAL_DIR="$(pwd)"


echo -n > $M/eval_output.txt
echo "Redirecting output to $M/eval_output.txt"
echo "Working..."

echo "Evaluate ngram n=1..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/n1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate ngram n=2..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/n2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate ngram n=3..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/n3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate ngram n=4..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/n4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate addone n=1..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/a1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate addone n=2..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/a2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate addone n=3..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/a3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate addone n=4..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/a4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate interpolated n=1..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/i1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate interpolated n=2..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/i2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate interpolated n=3..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/i3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate interpolated n=4..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/i4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate backoff n=1..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/b1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate backoff n=2..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/b2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate backoff n=3..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/b3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Evaluate backoff n=4..."
{ time -p python3.4 $SCRIPT_DIR/eval.py -i $M/b4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt