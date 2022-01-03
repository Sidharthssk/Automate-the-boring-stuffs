from pathlib import Path
import os,shutil


p=Path('/Users/s/Desktop/Contents')

for folderName, subfolders, subfiles in os.walk(p):
    for subfilename in subfiles:
       if subfilename.endswith('.pdf') or subfilename.endswith('.jpg'):
           newPath = Path(p / subfilename)
           shutil.copy(newPath,'/Users/s/Desktop/Regex_Search')
           

