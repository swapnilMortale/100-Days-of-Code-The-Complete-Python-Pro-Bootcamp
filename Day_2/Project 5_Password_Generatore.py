# project : Create a Password Generator..

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','Y','V','W','X','Y','Z']

numbers = ['1','2,','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','%','^','&','*','(',')','-']

print("Welcome to the Pythone Password Generatore..!")

in_letters= int(input("How Many Letters would you Like in your Password... : "))
in__symbols = int(input("How Many symbole would you like... : "))
in_number = int(input("How Many numbers  would you like... : "))


Password = []


for char in range(0,in_letters):
    Password += random.choice(letters)

for char in range(0,in_number):
    Password += random.choice(numbers)

for char in range(0,in__symbols):
    Password += random.choice(symbols)

print(Password)
random.shuffle(Password)
print(Password)



str_Password = " "
for char in  Password :
    str_Password += char

print(f" Your password is  : {str_Password}")