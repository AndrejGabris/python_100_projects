
import random
from replit import clear
from art import logo


def game():
    clear()
    def want_to_play_game():
        want_to_play = input("Do you want to play Blackjack Capstone? Write 'y' (yes) or 'n' (no): ")
        while want_to_play != 'y' and want_to_play != 'n':
            want_to_play = input("Do you want to play Blackjack Capstone? Write 'y' (yes) or 'n' (no): ")
        return want_to_play

    want_to_play = want_to_play_game()

    if want_to_play == 'y':
        print(logo)
        print("Note: 'Ace' counts as 11.")
        print()
        cards = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace",
        ]

        cards_value = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10,
            "Ace": 11,
        }

        user_cards = random.choices(cards , k=2)
        user_cards_values = [cards_value[user_cards[0]],cards_value[user_cards[1]]]
        dealer_cards = random.choices(cards , k=2)
        dealer_cards_values = [cards_value[dealer_cards[0]],cards_value[dealer_cards[1]]]
        drawn_cards = user_cards + dealer_cards
        print("")
        print(f"Your cards: {user_cards}")
        print(f"Dealer's cards: {[dealer_cards[0], "-"]}")
        print()

        def new_card(u_cards, uc_val, dr_cards):
            '''c_cards = user current card, uc_val = user's card value, d_cards = all drawn cards'''
            another_card = random.choice(cards)
            while dr_cards.count(another_card) > 4:
                another_card = random.choice(cards)
            u_cards.append(another_card)
            print(f"Your cards: {user_cards}")
            uc_val.append(cards_value[another_card])
            dr_cards.append(another_card)

            return u_cards, uc_val, dr_cards


        want_another_card = input("Do you want another card? Write 'y' (yes) or 'n' (no): ")
        while want_another_card != 'y' and want_another_card != 'n':
            want_another_card = input("Do you want another card? Write 'y' (yes) or 'n' (no): ")
        allowence = True
        while want_another_card == "y" and allowence == True:
            user_cards, user_cards_values, drawn_cards = new_card(u_cards=user_cards, uc_val=user_cards_values, dr_cards=drawn_cards)
            if sum(user_cards_values) > 21:
                print(f"\nYou lost\nYour cards: {user_cards}\nDealer's cards: {dealer_cards}\n")
                allowence = False
            else:
                want_another_card = input("Do you want another card? Write 'y' (yes) or 'n' (no): ")
                while want_another_card != 'y' and want_another_card != 'n':
                    want_another_card = input("Do you want another card? Write 'y' (yes) or 'n' (no): ")

                    
        if sum(user_cards_values) == sum(dealer_cards_values) and not sum(user_cards_values) > 21:
            print(f"\nIt's draw.\nYour cards: {user_cards}\nDealer's cards: {dealer_cards}\n")
        elif sum(user_cards_values) < sum(dealer_cards_values) and not sum(user_cards_values) > 21:
            print(f"\nYou lost.\nYour cards: {user_cards}\nDealer's cards: {dealer_cards}\n")
        elif sum(user_cards_values) <= 21 and sum(dealer_cards_values) > 22:
            print(f"\nYou won.\nYour cards: {user_cards}\nDealer's cards: {dealer_cards}\n") 
        elif sum(user_cards_values) > sum(dealer_cards_values) and not sum(user_cards_values) > 21:
            print(f"\nYou won.\nYour cards: {user_cards}\nDealer's cards: {dealer_cards}\n")    
        
        want_to_play = input("Do you want to play again?: Write 'y' (yes) or 'n' (no): ")
        if want_to_play == 'y':
            game()
game()


