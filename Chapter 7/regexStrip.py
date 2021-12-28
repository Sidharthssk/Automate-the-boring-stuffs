import re

def stripString(text,char=None):
    if char == None:
        check1 = re.compile(r'^\s')
        check2 = re.compile(r'\s$')
        string1 = check1.sub('',text)
        string2 = check2.sub('',string1)
        return string2
    else:
        check3 = re.compile(rf"{char}+")
        string3 = check3.sub('',text)
        return string3

print(stripString(' Hello World ')) 
print(stripString('python','y'))

