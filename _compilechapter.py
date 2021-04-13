import sys
import os
import subprocess

args = sys.argv[1:]
subj = args[0]
os.chdir(subj)
ch = args[1]
os.chdir(ch)
print(os.curdir)
print(subprocess.run(f'pandoc --template tem -c https://bootswatch.com/4/sketchy/bootstrap.min.css -s ..\{ch}.md -o {ch}.md.pdf --pdf-engine wkhtmltopdf', capture_output=True))
