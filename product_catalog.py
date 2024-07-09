class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def value(self):
        value = f"Total value of {self.name} in stock is: ${self.quantity * self.price}"
        return value

one = product("sugar",10, 2)
two = product("salt", 5, 10)
print(f"{one.value()}\n{two.value()}")