import string
import random

if __name__ == '__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
password_length=int(input("Enter password length\n"))
list1=[]
list1.extend(list(s1))
list1.extend(list(s2))
list1.extend(list(s3))
list1.extend(list(s4))
random.shuffle(list1)
# print(list1[0:password_length])
password="".join(list1[0:password_length])
print(password)

