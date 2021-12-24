

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(lis):
    colWidth=[0]*len(lis)
    counter=0
    for i in lis:
        count=0
        
        for j in i:
            if len(j)>count:
                count=len(j)
        colWidth[counter]=count
        counter+=1

   
    for i in range(len(lis[0])):
        for j in range(len(lis)):
            print(lis[j][i].rjust(colWidth[j]),end=' ')
       
        print()

printTable(tableData)            