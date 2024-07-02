import random

numbers = random.randint(1, 10)
count = 5
list = []

while count > 0:
    for i in range(1, numbers):
        list.append(i)
    count -= 1
x = set(list)
print(x)