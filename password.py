import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get() == 1
        use_digits = digits_var.get() == 1
        use_symbols = symbols_var.get() == 1

        password = generate_password(length, use_letters, use_digits, use_symbols)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

letters_var = tk.IntVar(value=1)
letters_check = tk.Checkbutton(root, text="Letters", variable=letters_var)
letters_check.grid(row=1, column=0)

digits_var = tk.IntVar(value=1)
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.grid(row=1, column=1)

symbols_var = tk.IntVar(value=1)
symbols_check = tk.Checkbutton(root, text="Symbols", variable=symbols_var)
symbols_check.grid(row=1, column=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=2, column=0, columnspan=3)

password_label = tk.Label(root, text="")
password_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
