import re,os,shutil
from pathlib import Path

filePattern = re.compile(r'(.*)\s(\..*)')


os.chdir('./FilesFolder')


for filenames in os.listdir(Path.cwd()):
    files = filePattern.search(filenames)
    if files == None:
        continue
    
    first_part=files.group(1)
    last_part = files.group(2)
    
    newFileName = first_part+last_part
    
    workingDir = os.path.abspath('.')
    oldPath = os.path.join(workingDir,filenames)
    newPath = os.path.join(workingDir,newFileName)

    shutil.move(oldPath,newPath)
    
