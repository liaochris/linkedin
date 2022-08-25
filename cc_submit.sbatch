#!/bin/bash

#SBATCH --partition=broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem-per-cpu=2000


# of cores to use on the machine. Using 16 will allow us to use all
# cores on a sandyb node
module load python

python cc_submit.py
