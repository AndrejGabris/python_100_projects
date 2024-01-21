
# list = ["adam", "barbara", "cesar", "dan"]
# print(list[list.index("barbara")])






programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# retrieving items from dictionary
# print(programming_dictionary["Bug"])

# adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# empty dicitionary
empty_dicitonary = {}

# wipe dictionary
# programming_dictionary = {} #clear all stored up to now

# edit and item in dicitionary
# programming_dictionary["Bug"]= "A moth in your computer"
# print(programming_dictionary["Bug"])

# Loop through a dicitonary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

