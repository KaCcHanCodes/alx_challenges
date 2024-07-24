class Student:
    name = 'Rocky'
    age = 22
    course = 'Masters'

    def __repr__(self):
        return repr('Hello ' + self.name + ' your age is ' + str(self.age) + ' and you have enrolled for ' + self.course)

s = Student()
print(help(repr(s)))