secretno = random(1,50)
lives = 5
while lives>0:
    print("Think of a number between 1 to 50, lets see if you can guess the number which I thought of!")
    answer = int(input("Enter your number: "))
    if answer == secretno:
      print("Congratss!!! You've guessed it!")
    else:
       lives -=1
       hintxxx = lives-secretno
       if hintxxx 