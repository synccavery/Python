try:
    number = int(input("Enter the number: "))
    print("You have entered ", number)

except ValueError as ex:
    print("Value Error: ", ex)