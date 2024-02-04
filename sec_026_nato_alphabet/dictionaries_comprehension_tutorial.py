# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}


import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)




# input: What is the Airspeed Velocity of an Unladen Swallow?
sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
sentence_list = sentence.split(" ")
result = {word:len(word) for word in sentence_list}
print(result)




# input: {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_c = eval(input())
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
