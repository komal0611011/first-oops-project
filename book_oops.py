class Book:
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self, percent):
        discount_amount = self.price * percent/100
        self.price = self.price - discount_amount
    def show_details(self):
        print(self.title)
        print(self.author)
        print(self.price)
Book1 = Book("Let Me Live The Moment", "Joseph Kamay", 290)
Book1.apply_discount(10)
Book1.show_details()
        