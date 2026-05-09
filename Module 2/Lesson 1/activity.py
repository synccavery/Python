medical_cause = input("Do you have any medical conditions? (y or n).:").lower()
if medical_cause == "n":
    attendance = int(input("Enter your attendance: "))
    if attendance >= 75:
        print("You are allowed for the exam.")
    else:
        print("You are not allowed for the exam.")
else:
    print("You are allowed for the exam.")