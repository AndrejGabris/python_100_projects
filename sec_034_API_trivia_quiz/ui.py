from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_FONT = ("Arial", 16, "italic")
SCORE_LABEL_FONT = ("Arial", 12, "normal")


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=SCORE_LABEL_FONT, highlightthickness=0, background=THEME_COLOR, fg="white")  
        self.score_label.grid(row=0, column=1)
          
    
    
    
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Demo Text", font=CANVAS_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        
        
        
        
        correct_button_image = PhotoImage(file=r"sec_034_API_trivia_quiz\images\true.png")
        self.correct_button = Button(image=correct_button_image, highlightthickness=0, bd=0, command=self.right_button_pressed)
        self.correct_button.grid(row=2, column=0)
        
        
        wrong_button_image = PhotoImage(file=r"sec_034_API_trivia_quiz\images\false.png")
        self.wrong_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=self.wrong_button_pressed)
        self.wrong_button.grid(row=2, column=1)
        
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {f"{self.quiz.score}/{self.quiz.question_number}"}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="There is no more questions in databank")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    
    def right_button_pressed(self):
        self.is_right = self.quiz.check_answer(user_answer="true")
        self.give_feedback(self.is_right)
        
        
    def wrong_button_pressed(self):
        self.is_right = self.quiz.check_answer(user_answer="false")
        self.give_feedback(self.is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
        