#! /usr/bin/bash
#  You must be in the virtualenv ($ workon pln-2015) to run this script
SCRIPT_DIR="$(dirname $0)"
mkdir $SCRIPT_DIR/../models
M=$SCRIPT_DIR/../models
# ORIGINAL_DIR="$(pwd)"


echo -n > $M/train_output.txt
echo "Redirecting output to $M/train_output.txt"
echo "Working..."

echo "Training base..."
{ time -p python $SCRIPT_DIR/train.py -m base -o $M/base >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training mlhmm n=1..."
{ time -p python $SCRIPT_DIR/train.py -m mlhmm -n 1 -o $M/mlhmm-1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training mlhmm n=2..."
{ time -p python $SCRIPT_DIR/train.py -m mlhmm -n 2 -o $M/mlhmm-2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training mlhmm n=3..."
{ time -p python $SCRIPT_DIR/train.py -m mlhmm -n 3 -o $M/mlhmm-3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training mlhmm n=4..."
{ time -p python $SCRIPT_DIR/train.py -m mlhmm -n 4 -o $M/mlhmm-4 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm logreg n=1..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 1 -c logreg -o $M/memm-logreg-1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm logreg n=2..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 2 -c logreg -o $M/memm-logreg-2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm logreg n=3..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 3 -c logreg -o $M/memm-logreg-3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm logreg n=4..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 4 -c logreg -o $M/memm-logreg-4 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm nb n=1..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 1 -c nb -o $M/memm-nb-1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm nb n=2..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 2 -c nb -o $M/memm-nb-2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm nb n=3..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 3 -c nb -o $M/memm-nb-3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm nb n=4..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 4 -c nb -o $M/memm-nb-4 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm svc n=1..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 1 -c svc -o $M/memm-svc-1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm svc n=2..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 2 -c svc -o $M/memm-svc-2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm svc n=3..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 3 -c svc -o $M/memm-svc-3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training memm svc n=4..."
{ time -p python $SCRIPT_DIR/train.py -m memm -n 4 -c svc -o $M/memm-svc-4 >> $M/train_output.txt ;} 2>> $M/train_output.txt