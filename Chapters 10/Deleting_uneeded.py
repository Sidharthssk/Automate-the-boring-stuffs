from pathlib import Path
import os


p=Path('/Users/s/Desktop/Contents')

for Foldername, SubFolders, SubFiles in os.walk(p):
    for folders in SubFolders:
       newPath = p / Path(folders)
       if os.path.getsize(newPath)/(1024*1024) > 100:
           print(os.path.abspath(newPath))
    for files in SubFiles:
       newPath = p / Path(files)
       if os.path.getsize(newPath)/(1024*1024) > 100:
           print(os.path.abspath(newPath))
       
