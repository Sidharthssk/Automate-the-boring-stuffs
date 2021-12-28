import re

dateFormat = re.compile(r'(\d{2})\/(\d{2})\/(\d{4})')

date=dateFormat.search('Today was a good day. Todays date is 31/02/2021')

if (int(date.group(1))>=1 and int(date.group(1))<=31) and (int(date.group(2))>=1 and int(date.group(2))<=12) and (int(date.group(3))>=1000 and int(date.group(3))<=2999):
    day=int(date.group(1))
    month = int(date.group(2))
    year = int(date.group(3))

 
month30 = [4,6,9,11]
month31 = [1,3,5,7,8,10,12]

if month in month30:
    if day>=1 and day<=30:
        print('Valid date')
    else:
        print('Invalid date')

elif month in month31:
    if day>=1 and day<=31:
       print('Valid date')
    else:
        print('Invalid date')

elif month == 2:
    if year%4 == 0:
        if day<=29:
           print('Valid date')
        else:
            print('Invalid date')  
    else :
        if day<=28:
              print('Valid date')
        else :
            print('Invalid date')           

