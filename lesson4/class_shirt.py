
class Shirt:
    """Shirt Objece
    arg:
    shirt_color: string
    shirt_size: string ( 's m l xxl')
    shirt_style: string
    shirt_price: int

    methods:
     change_price: add new price to current new_price
     discount: integer, the discount should be less than 1.
    """

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):

        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)



new_shirt = Shirt('red', 's', 'short sleeve', 15)
orange_shirt = Shirt('orange', 'L', 'short sleeve', 10)

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
