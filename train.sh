#!/bin/bash

source ~htiteux/.bashrc
module load cuda/10.0 anaconda
#export CUDA_VISIBLE_DEVICES=1,0

conda activate unsup_seg
python main.py data=timit
