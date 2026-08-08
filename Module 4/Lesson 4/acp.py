snackbox1 = {"chocolates", "chips", "juice", "ramen", "nuts"}
snackbox2 = {"chips", "ice cream", "ramen", "ice cream"}
print(f"Snackbox 1: {snackbox1}")
print(f"Snackbox 2: {snackbox2}")
snackbox2.add("cookies")
print(f"Snackbox 2 after adding cookies: {snackbox2}")
common_snackss = snackbox1.intersection(snackbox2)
print(f"Common snacks between 1&2: {common_snackss}")
import array as arr
snack_counts = arr.array('i',[3,5,2,4])
print(snack_counts)

snack_counts.insert(0,1)
print(snack_counts)
snack_counts.append(6)
print(snack_counts)
snack_counts.reverse()
print(snack_counts)
