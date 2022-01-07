import os,openpyxl,csv
from pathlib import Path

for file in os.listdir('.'):
    if file.endswith('.xlsx'):
        wb = openpyxl.load_workbook(file)
        for sheets in wb.sheetnames:
            sheet = wb[sheets]
            csvObj = open(Path(file).stem+'_'+sheets+'.csv','w',newline='')
            csvWritter = csv.writer(csvObj)
            for rowNum in range(1,sheet.max_row+1):
                rowData = []
                for colNum in range(1,sheet.max_column+1):
                    rowData.append(sheet.cell(row=rowNum,column=colNum).value)
                csvWritter.writerow(rowData)
            csvObj.close()