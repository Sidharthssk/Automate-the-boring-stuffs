import ezsheets

ss = ezsheets.Spreadsheet('1kN2qvn82trJ06k5XAR_oz9WKruk2cccFWqzgEj1U9DQ')

email_adresses = []

sheet = ss[0]

for emails in sheet.getColumn(3):
    print(emails)