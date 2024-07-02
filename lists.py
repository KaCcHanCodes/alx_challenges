#fruits = [items for items in input("Mention your favourite three fruits: ").split()]
#print(fruits[1])

#Get user input
fruits = input("Mention your favourite three fruits: ")

#iterate through the items in fruits and store them in list
list = [items for items in fruits.split()]

#print the second element in the list
print(list[1])