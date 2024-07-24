class Dog:
    def make_sound(self):
        return "I can bark, woof! woof!"
    
class Cat:
    def make_sound(self):
        return "I can purr, meow! meow!"
    
class Bird:
    def make_sound(self):
        return "I can chirp, chirp! chirp!"


def let_them_speak(obj1, obj2, obj3):
    list = [obj1, obj2, obj3]
    for obj in list:
        print(obj.make_sound())

obj1 = Dog()
obj2 = Cat()
obj3 = Bird()

let_them_speak(obj1, obj2, obj3)