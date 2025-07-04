# . Write a python program to differentiate odd and even number of a given list. 
import random
elements = int(input("Enter a number of element "))

rand_list = list(random.randint(0,100) for _ in range(elements))

odd_num = []
even_num = []

for i in rand_list:
    if i % 2 == 0:
       even_num.append(i)
    else:
       odd_num.append(i)

print(even_num,odd_num)