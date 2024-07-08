#Practicing how to create classes.

class student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        info = f"Student's name: {self.name}\nStudent's age: {self.age}\nStudent's department: {self.department}\n"
        return info

#Extra challenge
#Store user input in a list
#Pass the items in the list as arguements for the attributes of class student
list = []

item = input("Please input the following details: (name, age, department) ").split(", ")
list = item
    
details = student(*list) # *+list removes the brackets when printing lists.
print(details.display_info())