from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    reps = 0
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer    
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 1:
            check_marks.config(text=(reps // 2) * "✔")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"sec_028_tkinter_pomodoro_app\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN ,bg=YELLOW, font=((FONT_NAME, 15, "bold")))
check_marks.grid(column=1, row=3)



window.mainloop()