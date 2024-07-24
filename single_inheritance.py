class Shape:
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
       pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def calculate_area(self):
        result = self.length * self.width
        return f"Area of a rectangle is {result}"
    
class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def calculate_area(self):
        result = self.length**2
        return f"Area of a square is {result}"

value1 = Rectangle(5, 4)
value2 = Square(4)
print(f"{value1.calculate_area()}\n{value2.calculate_area()}")