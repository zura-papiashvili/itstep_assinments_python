# დაწერეთ პითონის პროგრამა კლასების გამოყენებით,
#  რომელიც წარმოადგენს კალათას. დაწერეთ ნივთების 
#  დამატებისა და წაშლის მეთოდები და პროდუქტების ფასის დათვლა.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def get_total_price(self):
        return sum(item.price for item in self.items)

# მაგალითი
cart = ShoppingCart()
apple = Product("ვაშლი", 1.0)
banana = Product("ბანანი", 0.5)
butter = Product("კარაქი", 2.0)




cart.add_item(apple)
cart.add_item(banana)
cart.add_item(butter)
print("ჯამი:", cart.get_total_price())

cart.remove_item(apple)
print("ჯამი ვაშლის წაშლის შემდეგ:", cart.get_total_price())