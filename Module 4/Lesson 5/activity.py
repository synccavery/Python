items = ["pencil", "eraser", "notebook", "sharpner", "glue"]
stock_counts = [12,0,8,5,3]
inventory = {item : count for item, count in zip(items,stock_counts)}
print("Full Inventory:" , inventory)
in_stock_items = [item for item in items if inventory[item] > 0]
print("In stock items: ",in_stock_items)
chosen_item = input("What item do you want to buy? ->")
if chosen_item not in inventory or inventory[chosen_item] ==0:
    print(f"{chosen_item} is stock out! Stopping the checker.")
    exit()
prices = [10,5,40,15,20]
markup = int(input("Enter the markup amount to add to every price: "))
markedup_prices = list(map(lambda p : p +markup,prices))
item_index = items.index(chosen_item)
chosen_price = markedup_prices[item_index]
print(f"Price of {chosen_item} after markup {chosen_price}")
inventory[chosen_item] = inventory[chosen_item] - 1
print(f"{chosen_item} purchased! Remaining stock:{inventory[chosen_item]}")
