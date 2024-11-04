import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def generate_and_display():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo("Password Generated", "Password has been copied to clipboard.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Secure Password Generator")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack()

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display)
generate_button.pack()

password_entry = tk.Entry(root, width=50)
password_entry.pack()

root.mainloop()
