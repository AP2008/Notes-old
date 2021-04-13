import sys
import os

subj = sys.argv[1]
f = open("index.md", "a")
f.write(f"## {subj}: [{subj}](/Notes/{subj} \"{subj}\")")
os.mkdir(subj)
os.chdir(subj)
os.mkdir("images")
