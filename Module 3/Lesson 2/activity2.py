def cube(number):
    return number**3
def divisibleBy3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
num = int(input("Enter the number: "))
print(divisibleBy3(num))