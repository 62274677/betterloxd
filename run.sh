#!/bin/bash
#* This script runs our bot 
#TODO make script run error-handling script in case the process goes down for whatever reason
# pwd
# ls 
# while true; do sleep 1000; done
git clone $1
pip install -r $2/requirements.txt

python3 $2/betterloxd.py 