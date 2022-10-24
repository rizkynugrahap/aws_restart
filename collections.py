"""
List Data Type
"""

#Defining a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

"""
# Tuple data type
"""

#Defining a tupe
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

"""
Dictionary data type
"""

#Defining a Dictionary
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineaple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Accessing a Dictionary
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

