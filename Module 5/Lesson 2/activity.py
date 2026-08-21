class IOString:
    #constructor
    def __init__(self):
        self.strl = ""
    #Method
    def get_string(self):
        self.strl = input("Enter a word:")
    #Method to print the string in uppercase
    def print_string(self):
        print("Result:", self.strl.upper())

ob = IOString()
ob.get_string()
ob.print_string()