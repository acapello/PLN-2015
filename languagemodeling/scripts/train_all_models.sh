#! /usr/bin/bash
#  You must be in the virtualenv ($ workon pln-2015) to run this script
SCRIPT_DIR="$(dirname $0)"
mkdir $SCRIPT_DIR/../models
M=$SCRIPT_DIR/../models
# ORIGINAL_DIR="$(pwd)"


echo -n > $M/train_output.txt
echo "Redirecting output to $M/train_output.txt"
echo "Working..."

echo "Training ngram n=1..."
{ time -p python $SCRIPT_DIR/train.py -m ngram -n 1 -o $M/n1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training ngram n=2..."
{ time -p python $SCRIPT_DIR/train.py -m ngram -n 2 -o $M/n2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training ngram n=3..."
{ time -p python $SCRIPT_DIR/train.py -m ngram -n 3 -o $M/n3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training ngram n=4..."
{ time -p python $SCRIPT_DIR/train.py -m ngram -n 4 -o $M/n4 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training addone n=1..."
{ time -p python $SCRIPT_DIR/train.py -m addone -n 1 -o $M/a1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training addone n=2..."
{ time -p python $SCRIPT_DIR/train.py -m addone -n 2 -o $M/a2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training addone n=3..."
{ time -p python $SCRIPT_DIR/train.py -m addone -n 3 -o $M/a3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training addone n=4..."
{ time -p python $SCRIPT_DIR/train.py -m addone -n 4 -o $M/a4 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training interpolated n=1..."
{ time -p python $SCRIPT_DIR/train.py -m interpolated -n 1 -o $M/i1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training interpolated n=2..."
{ time -p python $SCRIPT_DIR/train.py -m interpolated -n 2 -o $M/i2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training interpolated n=3..."
{ time -p python $SCRIPT_DIR/train.py -m interpolated -n 3 -o $M/i3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training interpolated n=4..."
{ time -p python $SCRIPT_DIR/train.py -m interpolated -n 4 -o $M/i4 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training backoff n=1..."
{ time -p python $SCRIPT_DIR/train.py -m backoff -n 1 -o $M/b1 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training backoff n=2..."
{ time -p python $SCRIPT_DIR/train.py -m backoff -n 2 -o $M/b2 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training backoff n=3..."
{ time -p python $SCRIPT_DIR/train.py -m backoff -n 3 -o $M/b3 >> $M/train_output.txt ;} 2>> $M/train_output.txt
echo "Training backoff n=4..."
{ time -p python $SCRIPT_DIR/train.py -m backoff -n 4 -o $M/b4 >> $M/train_output.txt ;} 2>> $M/train_output.txt