class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = Parrot("Blu",12)
woo = Parrot("Woo", 10)

print(f"{blu.name} is a {blu.species}. He is {blu.age} years old.")
print(f"{woo.name} is a {woo.species}. He is {woo.age} years old.")

