import random

user_name=input("Type your username:")
A = ['a', 'b', 'c', 'd', 'e']
B = ['A', 'B', 'C', 'D', 'E']
C = ['1', '2', '3', '4', '5']
D = ['@', '#', '$', '%', '&']

password1 = random.choice(A)
password2 = random.choice(B)
password3 = random.choice(C)
password4 = random.choice(D)

print(password1+password2+password3+password4)