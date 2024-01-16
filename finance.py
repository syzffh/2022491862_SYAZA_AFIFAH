import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="huh_cafe"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    topup_amount_str = topup_amount_entry.get()
    topup_method = topup_method_var.get()

    # Validate topup_amount as an integer value
    try:
        topup_amount = int(topup_amount_str)
    except ValueError:
        output_label.config(text="Invalid top up amount. Please enter a valid amount.", bg='#F1948A', font=10)
        return

    # Check if the top-up amount is less than 20
    if topup_amount < 20:
        output_label.config(text="Minimum top up amount is 20. Please enter a valid amount.", bg='#F1948A', font=9)
        topup_amount_entry.delete(0, tk.END)  # Clear the topup_amount_entry
    else:
        # Proceed with database insertion
        sql = "INSERT INTO `finance` (topup_amount, topup_method) VALUES (%s, %s)"
        val = (topup_amount, topup_method)
        mycursor.execute(sql, val)
        mydb.commit()

        # Clear entry fields after successful top-up
        topup_amount_entry.delete(0, tk.END)
        topup_method_var.set("Select Topup Method")

        # Update the output label
        output_label.config(text=f"You have successfully topped up RM{topup_amount} via {topup_method}.", bg='#82E0AA', font=10)

# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("FINANCE")
root.geometry('500x400')
root.config(bg='#D2B4DE')

# Page Title
label = tk.Label(root, text='FINANCE', font=("FZShuTi", 50, "bold"), bg='#D2B4DE')
label.pack(ipadx=5, ipady=5)

# Topup Method Dropdown (Label)
topup_method_label = tk.Label(root, text="Choose topup method:",font=("Cascadia Code", 15), bg='#D2B4DE')
topup_method_label.pack()

# Topup Method Dropdown
topup_method_var = tk.StringVar(root)
topup_method_var.set("Select Topup Method")
topup_method_dropdown = tk.OptionMenu(root, topup_method_var, "Online Banking", "TouchNGo", "Debit / Credit Card")
topup_method_dropdown.pack(pady=10)
dropdown_menu = topup_method_dropdown.nametowidget(topup_method_dropdown.menuname)
dropdown_menu.configure(bg='#D2B4DE', activebackground='#D2B4DE')


# Topup Amount Entry. Label and user can insert data thru entry
topup_amount_label = tk.Label(root, text="Enter Amount:",font=("Cascadia Code", 15), bg='#D2B4DE')
topup_amount_label.pack()
topup_amount_entry = tk.Entry(root)
topup_amount_entry.pack()

# Save Button
save_button = tk.Button(root, text="Topup",bg='#BB8FCE', font=("FZShuTi", 13, "bold"), command=collect_data)
save_button.pack(pady=5)

# Output Label & result
label = tk.Label(root, text='Top-Up Status', font=("Cascadia Code", 13),bg='#D2B4DE')
label.pack(ipadx=10, ipady=5)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()