my_dict ={
    "name":"Adreyii",
    "grade":7,
    "age":13,
    "country":"Bangladesh"
}
#Length of the dictionary
print(len(my_dict))
#Accessing Values
print(my_dict["name"])#method 1
print(my_dict.get("age"))#method 2
#Adding an item
my_dict["city"] = "Dhaka"
print(my_dict)
#Update an item
my_dict["grade"] = 8
print(my_dict)
#removing an item
my_dict.pop("country")
print(my_dict)
#Deleting the dictionary
my_dict.clear()
print(my_dict)