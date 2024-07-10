class ValueTooHighError(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        if self.num > 100:
            return f"Error {self.num} is greater than 100"
        
val = int(input("Please enter a number: "))

print(ValueTooHighError(val))