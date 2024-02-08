import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_letters = [letters[nr] for nr in range(nr_letters)]
    password_list_symbols = [symbols[nr] for nr in range(nr_symbols)]
    password_list_numbers = [numbers[nr] for nr in range(nr_numbers)]
    password_list = password_list_letters + password_list_symbols + password_list_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    
    
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    is_empty = website.strip() == "" or password.strip() == ""
    if is_empty:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open(r"sec_030_errors_exceptions_json\password_manager_updated\data.json", mode="r") as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(r"sec_030_errors_exceptions_json\password_manager_updated\data.json", mode="w") as data_file: 
                # saving data if file was not created - incialization
                json.dump(new_data, data_file, indent=4)
        else:       
            # updating old data with new data
            data.update(new_data)     
            
            with open(r"sec_030_errors_exceptions_json\password_manager_updated\data.json", mode="w") as data_file: 
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:            
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.focus()
  
# ------------------------- SEARCH PASSWORD --------------------------- #
def search_password():
    website = website_entry.get()
    is_empty = website.strip() == ""
    if is_empty:
        messagebox.showwarning(title="Oops", message="Please fill a website field for which you are looking for the password.")
    else:
        try:
            with open(r"sec_030_errors_exceptions_json\password_manager_updated\data.json", mode="r") as data_file:
                # read old data
                data = json.load(data_file)
            required_website = data[website]
        except FileNotFoundError:
            messagebox.showerror(title="Error message", message="No file with data found.") 
        except KeyError:
            messagebox.showerror(title="Error message", message=f"There is no record for: \n{website} website, in your data file.")
        else:
            messagebox.showinfo(title="Information message", message=f"Data were successfully founded: \n\nEmail: {data[website]["email"]} \nPassword: {data[website]["password"]}")

# ---------------------------- UI SETUP ------------------------------- #
def set_a_window_position(root, win_hei, win_wid):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_pos_center = (screen_width - win_wid) // 2
    y_pos_center = (screen_height - win_hei) // 2
    root.geometry(newGeometry=f"{win_wid}x{win_hei}+{x_pos_center}+{y_pos_center}")


window = tk.Tk()
window.title("Password Manager")
window_width = 520
window_height = 420
set_a_window_position(window, win_hei=window_height, win_wid=window_width )
window.config(padx=50, pady=50)

lock_canvas = tk.Canvas(height=200, width=200)
lock_path = tk.PhotoImage(file=r"sec_030_errors_exceptions_json\password_manager_updated\logo.png")
lock_canvas.create_image(100, 100, image=lock_path)
lock_canvas.grid(column=1, row=0)




website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = tk.Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1)
search_button = tk.Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1)


user_name_label = tk.Label(text="Email/Username:")
user_name_label.grid(column=0, row=2)
user_name_entry = tk.Entry(width=53)
user_name_entry.insert(0, "test@email.com")
user_name_entry.grid(column=1, row=2, columnspan=2)


password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3, padx=0)
password_generate_button = tk.Button(text="Generate Password", width=15, command=generate_password)
password_generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()