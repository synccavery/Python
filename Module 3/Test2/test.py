operation = input("Enter the operation you want to use: 1.Addition, 2. Substarction, 3.Multiplication, 4. Division (Answer in either 1,2,3,4)")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a%b)
try:
    if operation == 1:
       result = add(num1,num2)
       print("The answer is: ", result)
    elif operation == 2:
       result = sub(num1,num2)
       print("The answer is: ", result)
    elif operation == 3:
       result = mul(num1,num2)
       print("The answer is: ", result)
    elif operation == 4:
       result = div(num1,num2)
       print("The answer is: ", result)
    else:
       print("Invalid operational choice")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Number cannot be divided by zero!")



      


