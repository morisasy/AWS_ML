class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price
        self._color = shirt_color
        self._size = shirt_size
        self._style = shirt_style


    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price
