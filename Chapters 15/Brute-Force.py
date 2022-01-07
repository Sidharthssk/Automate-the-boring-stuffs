import PyPDF2

file = open('dictionary.txt')
contents = file.readlines()


pdfFile = open('encrypted_combinedminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

for lines in contents :
    lines = lines.strip()
    lower = lines.lower()
    upper = lines.upper()
   
    if pdfReader.decrypt(lower) == 1:
        print('Password hacked')
        print('Password is: '+lines)
        break

    elif pdfReader.decrypt(upper) == 1:
        print('Password hacked')
        print('Password is: '+lines)
        break
    