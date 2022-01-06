import ezsheets

ss = ezsheets.upload('prodeuceSales.xlsx')

wb=ss.downloadAsExcel()
od=ss.downloadAsODS()
pd=ss.downloadAsPDF()