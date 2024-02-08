# # File not found
# with open("a_file.txt") as file:
#     file.read()
    
    
# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apple", "Bannana", "Pear"]
# print(fruit_list[3])

# # TypeError
# text = "abc"
# print(5 + text)

# NameError
# print(a-list)



#Exception Handling
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # print(a_dictionary["non_existing_code"])
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")



# #BMI Example

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)














