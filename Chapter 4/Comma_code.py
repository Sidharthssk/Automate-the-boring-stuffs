def func(lis):
    str_var=''
    if len(lis)!=0:
        if len(lis)==1:
            return str(lis[0])
        for i in range(len(lis)):
            if i == (len(lis)-1):
                str_var += 'and'+' '+str(lis[i])
            else:
                if i != (len(lis)-2):
                   str_var += str(lis[i])+','+' '
                if i == (len(lis)-2):
                    str_var+=str(lis[i])+' '
    return str_var

arr=[]
print('enter the size of list')
n=int(input())
print('enter the list entries')
for i in range(0,n):
    ele = input()
    arr.append(ele)
print(func(arr))
