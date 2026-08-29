#Parent class
class FamilyMember:
    def __init__(self,eyes,height_cm):
        self.eyes = eyes
        self.height_cm = height_cm
        
    def show_traits(self):
        print("Eye Color:" ,self.eyes)
        print("Height in cm:" ,self.height_cm)
#Child class
class Kid(FamilyMember):
    def __init__(self,name,age,eyes,height_cm):
        self.name = name
        self.age = age
        super().__init__(eyes,height_cm)

    def show_traits(self):
        print("Name: ",self.name)
        print("Age: ", self.age)
        super().show_traits()

    def fav_hobby(self,hobby):
        print(f"{self.name} has a hobby which is {hobby}")

child = Kid("Adreyii","13","white","152")
child.show_traits()
child.fav_hobby("reading books")
    
