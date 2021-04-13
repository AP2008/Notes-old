import sys
import os

args = sys.argv[1:]
subj = args[0]
os.chdir(subj)
ch = args[1]
os.mkdir(ch.split('.')[0])
