

    """
            Pants class¶
            Write a Pants class with the following characteristics:

            the class name should be Pants
            the class attributes should include
            color
            waist_size
            length
            price
            the class should have an init function that initializes all of the attributes
            the class should have two methods
            change_price() a method to change the price attribute
            discount() to calculate a discount
    """

    class Pants:

    def __init__(self, pant_color, pant_size, pant_length, pant_price):
            """
            - first_name (string), the first name of the salesperson
            - last_name (string), the last name of the salesperson

           - employee_id (int), the employee ID number like 5681923
           - salary (float), the monthly salary of the employee

          - pants_sold (list of Pants objects),
          - pants that the salesperson has sold

          - total_sales (float), sum of sales of pants sold

            """
        self._price = pant_price
        self._color = pant_color
        self._length = pant_length
        self._price = pant_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price
