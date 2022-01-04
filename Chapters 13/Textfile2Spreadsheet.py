import openpyxl,os
from pathlib import Path



wb = openpyxl.Workbook()
sheet = wb.active
colNo=1
rowNo=1
for i in os.listdir('.'):
    if i.endswith('.txt'):
        p = Path(f'./{i}')
        file = open(p)
        fileContent = file.readlines()

        for lines in fileContent:
            c=sheet.cell(row=rowNo,column=colNo)
            c.value=lines
            rowNo+=1
            print(lines)
        colNo+=1

print('Data entered successfully....')
wb.save('test.xlsx')

        
