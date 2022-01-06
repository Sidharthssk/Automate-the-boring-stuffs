import ezsheets

ss1=ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet1 = ss1[0]

ss2 = ezsheets.upload()
sheet2 = ss2[0]

firstRow = sheet1.getRow(1)
sheet2.updateRow(1,firstRow)
for i in range(2,15002):
    if (int(sheet1.getRow(i)[0])*int(sheet1.getRow(i)[1])) == int(sheet1.getRow(i)[2]):
        sheet2.updateRow(i, sheet1.getRow(i))
    else:
        result = sheet1.getRow(i)
        result[2] = int(sheet1.getRow(i)[0])*int(sheet1.getRow(i)[1])
        sheet2.updateRow(i,result)

