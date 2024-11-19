inventory = [
    ("Laptop", 10, 30000),
    ("Keyboard", 20, 1000),
    ("Mouse", 20, 600),
    ("Headphones", 25, 1250),
    ("Monitor", 20, 2100)
]

highest_stock_value = 0
item_with_highest_stock_value = None
for item in inventory:
    name, quantity, price = (item)
    stock_value = quantity * price
    print(f"item name: {name}, total value: {stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value = stock_value
        item_with_highest_stock_value = name

print(f"item with highest stock value is {item_with_highest_stock_value} and it is worth {highest_stock_value}")