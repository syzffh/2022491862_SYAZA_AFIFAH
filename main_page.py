import tkinter as tk
from tkinter import messagebox
import subprocess

def open_profile_gui():
    try:
        subprocess.run(["python", "Profile.py"])
    except FileNotFoundError:
        messagebox.showerror("Error")

def open_menu_gui():
    try:
        subprocess.run(["python", "menu.py"])
    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Error: {e}")

def open_finance_gui():
    try:
        subprocess.run(["python", "finance.py"])
    except FileNotFoundError as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Error: {e}")

# Main window.
main_page = tk.Tk()
main_page.title("Main Page")
main_page.geometry('487x350')
main_page.config(bg='#D2B4DE')

# Page Title
label = tk.Label(main_page, text='Welcome to the Huh? Cafe Main Page', font=("Monotype Corsiva", 25, 'bold'), bg='#9B59B6' , fg='#F9F9F7')
label.pack(pady=20)

# Button to open Profile GUI
open_profile_button = tk.Button(main_page, text="PROFILE", font=("FZShuTi", 14, "bold"),bg='#9B59B6',fg='#F9F9F7',command=open_profile_gui)
open_profile_button.pack(pady=20)

# Button to open menu GUI
open_menu_button = tk.Button(main_page, text="MENU", font=("FZShuTi", 14, "bold"), bg='#9B59B6',fg='#F9F9F7',command=open_menu_gui)
open_menu_button.pack(pady=20)


# Button to open finance GUI
open_finance_button = tk.Button(main_page, text="FINANCE", font=("FZShuTi", 14, "bold"),bg='#9B59B6',fg='#F9F9F7', command=open_finance_gui)
open_finance_button.pack(pady=20)

main_page.mainloop()
