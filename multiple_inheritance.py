class Bird:
    def fly(self):
        return "I can fly"

class Mammal:
    def run(self):
        return "I can run"

class Quail(Bird, Mammal):
    def action(self):
       act1 = super().fly()
       act2 = super().run()
       return f"I am bird, {act1} and {act2}"

animal = Quail()
print(f"{animal.action()}")