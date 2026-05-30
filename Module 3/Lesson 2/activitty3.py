def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
    
print("Pactorial of 0: ",fact(0))
print("Pactorial of 1: ",fact(1))
print("Pactorial of 3: ",fact(3))
print("Pactorial of 5: ",fact(5))
