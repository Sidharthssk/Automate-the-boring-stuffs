def collatz(number):
    if number%2==0:
        return number/2
    elif (number%2)==1:
        return (3*number)+1

try:
       print('Enter a number')
       n = int(input())

       while True:
           n=(collatz(n))
           print(int(n))
           if n==1:
               break


except ValueError:
        print('You entered a non integer string')
