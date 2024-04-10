#!/bin/bash -x
eval "$(conda shell.bash hook)"
conda activate $1
cd ml
pip install -e .
# add other directories to install here