
# new_list = [new_item + operation for new_item in list if test]



# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers] # list comprehension
# print(new_numbers)


# name = "Andrej"
# latters_list = [letter for letter in name]
# print(latters_list)



# old_range = range(1, 5)
# new_range = [number * 2 for number in old_range]
# print(new_range)



# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# upper_long_names = [name.upper() for name in names if len(name) > 5]
# print(upper_long_names)




with open(r"sec_026_nato_alphabet\file1.txt") as file:
  file_one_raw = file.readlines()
  file_one = [int(item) for item in file_one_raw]

with open(r"sec_026_nato_alphabet\file2.txt") as file:
  file_two_raw = file.readlines()
  file_two = [int(item.replace("\n","")) for item in file_two_raw] #.replace("\n","") not needed during str -> int conversion

result = [number for number in file_one if number in file_two]
print(result)