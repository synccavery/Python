word = input("Enter your word: ")
char = input("Enter your character: ")

count = 0
i = 0

while i<len(word):
    if (word[i] == char):
        count += 1
    i += 1

print("Total occurences: ",count)
