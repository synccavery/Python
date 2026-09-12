from abc import ABC, abstractmethod

#Abstract Class
class AbsClass(ABC):
    def print(self,x):
        print("Passed value:" ,x)

    @abstractmethod
    def task(self):
        print("We are inside an abstract method.")

class test_class(AbsClass):
    def task(self):
        print("We are inside the test class.")

ob = test_class()
ob.task()
ob.print(100)