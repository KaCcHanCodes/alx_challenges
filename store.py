from exception_practice import OutOfStockError

paint_stock = {"red": 10, "blue": 10, "white": 5, "black": 5, "green": 0}

def item_quantity(item, quantity):
    try:
        if paint_stock[item] == 0:
            raise OutOfStockError(item)
        elif quantity > paint_stock[item]:
            print("Error: the quantity is greater than in-stock")
        else:
            print(f"Your purchase of {quantity} bucket(s) of {item} paint is successful")
            paint_stock[item] -= quantity
    except KeyError:
        print(f"{item} not found")

color = input("What color of paint do you need: ")
quant = int(input("What quantity do you need: "))

try:
    item_quantity(color, quant)
except Exception as e:
    print(e)

    
# item = input("Put a paint inside the store: (color) ")
# val = int(input("What is the quantity: "))

# key = item
# value = val
# paint_stock.update({key: value})

# print(paint_stock)