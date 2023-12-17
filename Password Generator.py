import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    try:
        length = int(length)
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length (a positive integer)")
        return

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(generated_password)

def save_password():
    website = website_var.get()
    password = password_var.get()

    if not website or not password:
        messagebox.showerror("Error", "Enter the website/application name and the generated password")
        return

    # Add the password to the dictionary
    passwords[website] = password
    update_password_list()

def show_passwords():
    passwords_window = tk.Toplevel(root)
    passwords_window.title("Generated Passwords")

    password_listbox = tk.Listbox(passwords_window, selectmode=tk.SINGLE, width=40, height=10)
    password_listbox_scroll = ttk.Scrollbar(passwords_window, orient=tk.VERTICAL, command=password_listbox.yview)
    password_listbox.config(yscrollcommand=password_listbox_scroll.set)

    for website, password in passwords.items():
        password_listbox.insert(tk.END, f"{website}: {password}")

    password_listbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    password_listbox_scroll.grid(row=0, column=1, sticky="ns")

# Create the main window
root = tk.Tk()
root.title("Password Generator and Manager")

# Variables to store password generation parameters
length_var = tk.StringVar(value="12")
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# Variables to store password data
website_var = tk.StringVar()
password_var = tk.StringVar()
passwords = {}

# Define widgets
length_label = ttk.Label(root, text="Password Length:")
length_entry = ttk.Entry(root, textvariable=length_var, width=5)
uppercase_check = ttk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
digits_check = ttk.Checkbutton(root, text="Digits", variable=digits_var)
symbols_check = ttk.Checkbutton(root, text="Symbols", variable=symbols_var)
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)

website_label = ttk.Label(root, text="Website/Application:")
website_entry = ttk.Entry(root, textvariable=website_var, width=20)
password_label = ttk.Label(root, text="Password:")
password_entry = ttk.Entry(root, textvariable=password_var, state="readonly", width=20)
save_button = ttk.Button(root, text="Save Password", command=save_password)
show_button = ttk.Button(root, text="Generated Passwords", command=show_passwords)

# Arrange widgets
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
uppercase_check.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")
digits_check.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")
symbols_check.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

website_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
website_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")
password_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
password_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")
save_button.grid(row=7, column=0, pady=10)
show_button.grid(row=7, column=1, pady=10)

# Run the main event loop
root.mainloop()
