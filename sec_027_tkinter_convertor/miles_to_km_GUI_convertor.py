from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20) # spacing from entire window



miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)



is_equal_to = Label(text="is equal to:")
is_equal_to.grid(column=0, row=1)


km_converted = Label()
km_converted.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)




def conversion():
    miles_to_be_converted = miles_input.get()
    km_conv = 1.60934 * float(miles_to_be_converted)
    km_converted.config(text=f"{km_conv}")
    
calculate = Button(text="Calculate", command=conversion)
calculate.grid(column=1, row=2)



window.mainloop() # at very end of my program to keep window open