import tkinter as tk
import random 
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"
TITLE_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 40, "bold")

random_word = None

# ----------------------------- Next card ----------------------------- #
def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn_vocabulary)

    canvas.itemconfig(canvas_image, image = card_front_canvas_image)
    canvas.itemconfig(title_label, text=learning_languages_list[0], fill=BLACK_COLOR)
    canvas.itemconfig(word_label, text=f"{random_word[to_learn_language]}", fill=BLACK_COLOR)
    
    flip_timer = canvas.after(3000, func=card_back)


def already_know():
    try:
        to_learn_vocabulary.remove(random_word)
    except ValueError:
        pass
    finally:
        data = pd.DataFrame(to_learn_vocabulary)
        data.to_csv(r"sec_031_flash_card_app_capstone\data\words_to_learn.csv", index=False)
        print(len(to_learn_vocabulary))
        next_card()
       
    

def card_back():
    global random_word
    canvas.itemconfig(canvas_image, image = card_back_canvas_image)
    canvas.itemconfig(title_label, text=learning_languages_list[1], fill=WHITE_COLOR)
    
    try:
        translated_word = random_word[learning_languages_list[1]]
    except TypeError:
        translated_word = "word"
    finally:
        canvas.itemconfig(word_label, text=translated_word)
        canvas.itemconfig(word_label, fill="white")
    
    
# ----------------------------- Read data ----------------------------- #

try:
    data = pd.read_csv(r"sec_031_flash_card_app_capstone\data\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"sec_031_flash_card_app_capstone\data\ger_sk_150.csv")
finally:
    learning_languages_list = data.columns.to_list()
    to_learn_language  = learning_languages_list[0]
    to_learn_vocabulary = data.to_dict(orient="records")


# ----------------------------- GUI setup ----------------------------- #
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=card_back)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_canvas_image = tk.PhotoImage(file=r"sec_031_flash_card_app_capstone\images\card_front.png")
card_back_canvas_image = tk.PhotoImage(file=r"sec_031_flash_card_app_capstone\images\card_back.png")
canvas_image = canvas.create_image(400, 263, image = card_front_canvas_image)
title_label = canvas.create_text(400, 150, text=to_learn_language, font=TITLE_FONT)
word_label = canvas.create_text(400, 263, text="word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)


right_button_image = tk.PhotoImage(file=r"sec_031_flash_card_app_capstone\images\right.png")
right_button = tk.Button(image=right_button_image, highlightthickness=0, bd=0, command=already_know)
right_button.grid(row=1, column=1)

wrong_button_image = tk.PhotoImage(file=r"sec_031_flash_card_app_capstone\images\wrong.png")
wrong_button = tk.Button(image=wrong_button_image, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)




window.mainloop()