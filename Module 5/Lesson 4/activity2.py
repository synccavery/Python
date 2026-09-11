class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setmaxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
c.__maxprice = 1200
c.sell()
c.setmaxprice(1200)
c.sell()