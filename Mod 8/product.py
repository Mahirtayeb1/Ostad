class Product:
    def __init__(self, n, amnt, p):
        self.name = n
        self.amount = amnt
        self.price = p

    def memo(self):
        print(self.name, "total cost is: ", self.amount*self.price, "taka")

#taking inputs from user
name = input("What do u want?: ")
amount, price = map(float, input("Enter amount and price separated by space: ").split())

p1 = Product("Pizza", 3, 250)
p2 = Product(name, amount, price)
p1.memo()
p2.memo()