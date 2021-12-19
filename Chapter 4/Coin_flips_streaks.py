import random
numberOfStreaks=0
lis =[]

for experimentNumber in range(10000):
    for i in range(0,100):
        n=random.randint(0,1)
        lis.append(n)

    for i in range(0,100):
        if (lis[i:i+7]==[1,1,1,1,1,1])or(lis[i:i+7]==[0,0,0,0,0,0]):
            numberOfStreaks+=1


print('Chance of streak: %s%%' %(numberOfStreaks/100))
