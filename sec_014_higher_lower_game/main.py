import random
from replit import clear
from art import logo, vs
from game_data import data

score = 0
already_picked_names = []

first_choice = random.randint(0,len(data)-1)
already_picked_names.append(first_choice)
a_choice = data[first_choice]

second_choice = random.randint(0,len(data)-1)
while second_choice in already_picked_names:
    second_choice = random.randint(0,len(data)-1)
already_picked_names.append(second_choice)
b_choice = data[second_choice]

clear()
print(logo)
print(f"Compare A: {a_choice["name"]}, {a_choice["description"]}, {a_choice["country"]}")
print("")
print(vs)
print("")
print(f"Compare B: {b_choice["name"]}, {b_choice["description"]}, {b_choice["country"]}")

user_pick_up = input("Who has more followers?. Type 'A' or 'B': ")
while user_pick_up != "A" and user_pick_up != "B":
    user_pick_up = input("Ooops a wrong input. Please type 'A' or 'B': ")

if user_pick_up == "A":
    user_choice = a_choice
else:
    user_choice = b_choice

def you_lost(first, second, current_score):
    clear()
    print(logo)
    print(f"""
Sorry, thats's wrong. Final score: {current_score}

{first["name"]} - {first["follower_count"]} followers.
{second["name"]} - {second["follower_count"]} followers.
    """)

def next_round(previous_question, new_question, current_score, previously_drawn):
    clear()
    print(logo)
    print(f"""
You are right! Current score: {current_score}
Compare A: {previous_question["name"]}, {previous_question["description"]}, {previous_question["country"]}

{vs}
    
Compare B: {new_question["name"]}, {new_question["description"]}, {new_question["country"]}
    """)

    round_pick_up = input("Who has more followers?. Type 'A' or 'B': ")
    while round_pick_up != "A" and round_pick_up != "B":
        round_pick_up = input("Ooops a wrong input. Please type 'A' or 'B': ")
    if round_pick_up == "A":
        round_pick_up = a_choice
    else:
        round_pick_up = b_choice

    return round_pick_up

def comparasion(a_option, b_option, u_option):
    comparasion_list = [a_option['follower_count'], b_option['follower_count']]
    higher_value = max(comparasion_list)
    if u_option['follower_count'] == higher_value:
        return u_option
    else:
        return {}

game = True
while game != False:
    result = comparasion(a_option=a_choice, b_option=b_choice, u_option=user_choice)
    if result != {}:
        score += 1
        a_choice = result
        b_choice = random.randint(0,len(data)-1)
        while b_choice in already_picked_names:
            b_choice = random.randint(0,len(data)-1)
        already_picked_names.append(b_choice)
        b_choice = data[b_choice]
        user_choice = next_round(a_choice, b_choice, score, already_picked_names)
    else:
        you_lost(a_choice, b_choice, score)
        game = False
