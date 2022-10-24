# String data type
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# String concatenation
firstString = "water"
secondString = "fall"
thridString = firstString + secondString
print(thridString)

# input String
name = input("what is your name? ")
print(name)

# Output String
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
