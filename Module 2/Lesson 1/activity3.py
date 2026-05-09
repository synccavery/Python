print("Please select your ride: ")
print("1.Bike")
print("2.Car")
choice = int(input("Enter your choice(1 or 2): "))
if choice == 1:
    print("What type of bike?: ")
    print("1.Scooter")
    print("2.Motorbike")
    choice2 = int(input("Enter your choice(1 or 2): "))
    if choice2 == 1:
      print("You have chosen Scooter as your ride")
    else:
      print("You have chosen Motorbike as your ride.")
elif choice == 2:
    print("What type of car?: ")
    print("1.Noah")
    print("2.Toyota")
    choice2 = int(input("Enter your choice(1 or 2): "))
    if choice2 == 1:
      print("You have chosen Noah as your ride")
    else:
      print("You have chosen Toyota as your ride.")
else:
   print("Invalid Opinion")

