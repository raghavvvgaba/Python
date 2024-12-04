class Order: 
    def __init__(self, items, price):
        self.items = items
        self.price = price
    def __gt__(self, ord2):
        return self.price > ord2.price
ord1 = Order("chips", 20)
ord2 = Order("tea", 10)

print(ord1 > ord2) #returns True

