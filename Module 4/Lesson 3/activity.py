basket1 = {"apple", "banana", "mango", "watermelon", "jackfruit"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}
print(f"Basket 1: {basket1}")
print(f"Basket 2: {basket2}")
basket2.add("orange")
print(f"Basket 2 after adding orange: {basket2}")
common_fruits = basket1.intersection(basket2)
print(f"Common fruits between 1&2: {common_fruits}")