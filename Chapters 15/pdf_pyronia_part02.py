import os,sys,PyPDF2



file_list = []
encrypted_files = []

for foldername, filename, subfolder in os.walk('.'):

    for files in filename:
        if files.endswith('.pdf') :
            file_list.append(files)
    
    for files in subfolder:
        if files.endswith('.pdf'):
            file_list.append(files)
print(file_list)

if len(sys.argv)==len(file_list)+1:
    for files in file_list:
        
        pdfFile = open(files,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        if pdfReader.isEncrypted:
            encrypted_files.append(files)

    for i,files in enumerate(encrypted_files):
        pdfFile = open(files,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        if pdfReader.decrypt(sys.argv[i+1]) == 1:
            pdfWritter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWritter.addPage(pdfReader.getPage(pageNum))
            resultpdf = open(f'{files}_decrypted.pdf','wb')
            pdfWritter.write(resultpdf)
            resultpdf.close()
            pdfFile.close()
        else:
            print('Incorrect password!!')
            continue
