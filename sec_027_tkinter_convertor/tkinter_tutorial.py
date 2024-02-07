from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # spacing from entire window



def button_clicked():
    print("I got clicked.")
    new_input = input.get()
    my_label.config(text=new_input)



# label
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label["text"] = "New Text" # same properties as line below
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=10, y=10)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=30)





# button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# new button
new_button = Button(text="New Button", command=button_clicked)
# new_button.pack()
new_button.grid(column=2, row=0)


# entry 
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)








window.mainloop() # at very end of my program to keep window open