import keyword

#Check if a word is a Python keyword
word = input("Enter a word: ")
print(keyword.iskeyword(word))

#Printing all the Python keywords
print(keyword.kwlist)