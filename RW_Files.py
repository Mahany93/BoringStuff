from pathlib import Path
import os

# ## Write to file 
os.chdir(r'C:\Users\Mahmoud\Evernote\test')
parent= Path.cwd()
p = Path('spam.txt')

with open(Path(parent / p), 'a') as f:
    f.write('Appended line \n')


## Read file content
with open(Path(parent / p), "r") as f:
    for line in f:
        print(line, end='')
