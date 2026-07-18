lst = [4, 5, 6, 3, 1, 2, 10]
sum = 0
for item in lst:
    sum = item + sum
print("Sum is: ", sum)
avg = sum/len(lst)
avg = round(avg,2)
print("Average is: ",avg)
lst.sort()
print("After sorting: ", lst)
print("Smallest number: ", lst[0])
print("largest number : ", lst[-1])
