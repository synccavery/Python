amount = int(input("Enter your amount: "))

note_100 = amount//100
note_50 = (amount%100)//50
note_10 = ((amount%100)%50)//10

print("notes of 100 taka: ",note_100)
print("notes of 50 taka: ",note_50)
print("notes of 10 taka: ",note_10)