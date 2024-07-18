import random
a=int(input("enter the password size:"))
characters="abcdefghijklmnopqrstuvwxyz@#$%^&*()1234567890"
password_out=""
i=1
while i<=a:
    password_out=password_out + random.choice(characters)
    i=i+1
print(password_out)