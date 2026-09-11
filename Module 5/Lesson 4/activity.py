class myClass:
    #private variable
    __privateVar = 27

    #private method
    def __privateMethod(self):
        print("I am inside the myClass.")

    #Public method
    def hello(self):
        print(myClass.__privateVar)

ob = myClass()
ob.hello()
ob.__privateMethod()
