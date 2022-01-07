import os,sys,PyPDF2


os.chdir('/Users/sidharth/Desktop/pdf Folders')
file_list = []

for foldername, filename, subfolder in os.walk('.'):

    for files in filename:
        if files.endswith('.pdf'):
            file_list.append(files)
    
    for files in subfolder:
        if files.endswith('.pdf'):
            file_list.append(files)
print(file_list)

if len(sys.argv)==len(file_list)+1:
    for i,files in enumerate(file_list):
       
        pdfFile = open(files,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWritter = PyPDF2.PdfFileWriter()
        for pageNum in range(1,pdfReader.numPages):
            pdfWritter.addPage(pdfReader.getPage(pageNum))
        pdfWritter.encrypt(sys.argv[i+1])
        resultpdf = open(f'{str(files)}_encrypted.pdf','wb')
        pdfWritter.write(resultpdf)
        resultpdf.close()
        pdfReader1 = PyPDF2.PdfFileReader(open(f'{files}_encrypted.pdf','rb'))
        if pdfReader1.decrypt(sys.argv[i+1]) == 1:
            print(f'{files}encrypted successfully')
            os.remove(f'{files}')
        resultpdf.close()
        pdfFile.close()
