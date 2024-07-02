import random

#generate random numbers
numbers = random.randint(1, 10)
count = 5
list = []

#generate a list of random numbers 5 times
while count > 0:
    for i in range(1, numbers):
        #store each value of i in list
        list.append(i)
    count -= 1
#remove duplicate numbers
x = set(list)
print(x)