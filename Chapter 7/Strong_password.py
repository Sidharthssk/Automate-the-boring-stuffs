import re
import sys

def passwordCheck(text):
    password=re.compile(r'[a-z]+[A-Z]+[0-9]+|[a-z]+[0-9]+[A-Z]|[A-Z]+[a-z]+[0-9]+|[A-Z]+[0-9]+[a-z]+|[0-9]+[a-z]+[A-Z]+|[0-9]+[A-Z]+[a-z]+')
    if len(text)>=8:
        pass_check=password.findall(text)
    else:
        print('The password is week because it should be atleast 8 character long')
        sys.exit()   
    if len(pass_check)==0:
        print('The password is week because it should contain uppercase and lowercase and atleast one digit ')
        sys.exit()
    print('The password is strong')

passWord=input("Enter password: ")
passwordCheck(passWord)