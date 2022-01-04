import re

p=open('input.txt')
content = p.read()
p.close()
arr =content.split()

for i in range(len(arr)):
    if arr[i] == 'ADJECTIVE':
        arr[i] = input('Enter an adjective: ')
    elif arr[i] == 'NOUN':
        arr[i] = input('Enter a noun: ')
    elif arr[i] == 'ADVERB':
        arr[i] = input('Enter an adverb: ')
    elif arr[i] == 'VERB.':
        arr[i] = input('Enter a verb: ')

sentence = ' '.join(arr)
p = open('input.txt','w')
p.write(sentence)
p.close()
print(sentence)
