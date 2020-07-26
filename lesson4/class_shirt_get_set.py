from shirt import Shirt

new_shirt = Shirt('red', 's', 'short sleeve', 45)
orange_shirt = Shirt('orange', 'L', 'short sleeve', 15)

print(new_shirt.__doc__)

# print

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_price = new_shirt.change_price(10)
print(new_shirt.price)

new_discount = new_shirt.discount(0.3)
print(new_discount)
