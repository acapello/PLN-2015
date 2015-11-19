#! /usr/bin/bash
#  You must be in the virtualenv ($ workon pln-2015) to run this script
SCRIPT_DIR="$(dirname $0)"
mkdir $SCRIPT_DIR/../models
M=$SCRIPT_DIR/../models
# ORIGINAL_DIR="$(pwd)"


echo -n > $M/eval_output.txt
echo "Redirecting output to $M/eval_output.txt"
echo "Working..."

echo "Eval base..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/base >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval mlhmm n=1..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/mlhmm-1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval mlhmm n=2..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/mlhmm-2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval mlhmm n=3..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/mlhmm-3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval mlhmm n=4..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/mlhmm-4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm logreg n=1..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-logreg-1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm logreg n=2..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-logreg-2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm logreg n=3..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-logreg-3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm logreg n=4..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-logreg-4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm nb n=1..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-nb-1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm nb n=2..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-nb-2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm nb n=3..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-nb-3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm nb n=4..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-nb-4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm svc n=1..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-svc-1 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm svc n=2..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-svc-2 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm svc n=3..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-svc-3 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt
echo "Eval memm svc n=4..."
{ time -p python $SCRIPT_DIR/eval.py -i $M/memm-svc-4 >> $M/eval_output.txt ;} 2>> $M/eval_output.txt