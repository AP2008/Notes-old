import sys
import os

args = sys.argv[1:]
subj = args[0]

f = open(f"{subj}.md", "w+")
f.write(f"---\ntitle: {subj} Notes\nlayout: page\nsearch: true\n---\n\n")

os.chdir(subj)
k = os.listdir()
n = [i for i in k if i.split('.')[-1] == 'md']
print(n)

for h in n:
    i = open(h).readlines()
    for l in i:
        if l[:5] == 'namet':
            r = l[8:-1]
            f.write(f"* [{r[:-1]}](/Notes/{subj}/{r.split(':')[0].replace(' ', '')})\n")
            break

f.close()
