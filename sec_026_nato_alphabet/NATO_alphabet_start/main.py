# --------------------------------- HINTS ---------------------------------

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# ---------------------------------------------------------------------------


import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv(r"sec_026_nato_alphabet\NATO_alphabet_start\nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Enter a word: ").upper()
word_input_list = [nato_alphabet[letter] for letter in word_input]
print(word_input_list)

