import tkinter as tk
import mysql.connector

# Connect MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="huh_cafe"
)

mycursor = mydb.cursor()

#Register Data
def collect_data():
    First_Name = str(First_Name_entry.get())
    Last_Name = str(Last_Name_entry.get())
    Phone_Number = Phone_Number_entry.get()
    Email = str(Email_entry.get())

    # Check if any field is empty
    if not all([First_Name, Last_Name, Phone_Number, Email]):
        output_label.config(text="Please fill in all the fields", bg='#F1948A')
        return
    

    # Insert Data to Database
    sql = "INSERT INTO `profile` (First_Name , Last_Name , Phone_Number, Email) VALUES (%s, %s, %s, %s)"
    val = (First_Name, Last_Name, Phone_Number, Email)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back the output.
    output_label.config(text="Your profile has been successfully registered", bg=('#82E0AA'))
    

  #To limit the number phone  
def validate_Phone_Number_callback(value):
    return value.isdigit() and len(value) <= 11 or value == '' 

#Delete Data
def delete_data():
    Email_to_delete = str(Email_delete_entry.get())

    # Check if Email field is empty
    if not Email_to_delete:
        delete_output_label.config(text="Please enter your email", bg='#F1948A')
        return

    # Delete Data from Database
    sql = "DELETE FROM `profile` WHERE Email = %s"
    val = (Email_to_delete,)
    mycursor.execute(sql, val)
    mydb.commit()

    # To print back the output.
    delete_output_label.config(text="Your profile has been deactivated", bg=('#82E0AA'))

#Update Data
def update_data():
    Old_Email = str(Old_Email_entry.get())
    New_First_Name = str(New_First_Name_entry.get())
    New_Last_Name = str(New_Last_Name_entry.get())
    New_Phone_Number = str(New_Phone_Number_entry.get())
    New_Email = str(New_Email_entry.get())

    # Start building the SQL query
    sql = "UPDATE `profile` SET "
    update_values = []

    
    if New_First_Name:
        sql += "First_Name=%s, "
        update_values.append(New_First_Name)
    if New_Last_Name:
        sql += "Last_Name=%s, "
        update_values.append(New_Last_Name)
    if New_Phone_Number:
        sql += "Phone_Number=%s, "
        update_values.append(New_Phone_Number)
    if New_Email:
        sql += "Email=%s, "
        update_values.append(New_Email)


    sql = sql.rstrip(', ')
    sql += " WHERE Email=%s"
    update_values.append(Old_Email)

    # Execute the update query
    mycursor.execute(sql, tuple(update_values))
    mydb.commit()

    # To print back the output
    update_output_label.config(text=f"Your profile has been updated", bg=('#82E0AA'))

#To limit the number for new number phone
def validate_New_Phone_Number_callback(value):
        return value.isdigit() and len(value) <= 11 or value == ''

# Main window.
root = tk.Tk()
root.title("Profile")
root.geometry('1350x400')
root.config(bg='#D2B4DE')

# Registration Section on the Left
registration_frame = tk.Frame(root, bg='#D2B4DE')
registration_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

# Page Title
label = tk.Label(registration_frame, text='PROFILE', font=("FZShuTi", 30, "bold"),bg='#D2B4DE')
label.grid(row=0, column=0, columnspan=2, pady=10)

# First Name Entry
First_Name_label = tk.Label(registration_frame, text="Insert your first name:", font=("Cascadia Code", 10), bg='#D2B4DE')
First_Name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
First_Name_entry = tk.Entry(registration_frame)
First_Name_entry.grid(row=1, column=1, padx=10, pady=5)

# Last Name Entry
Last_Name_label = tk.Label(registration_frame, text="Insert your last name:", font=("Cascadia Code", 10), bg='#D2B4DE')
Last_Name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
Last_Name_entry = tk.Entry(registration_frame)
Last_Name_entry.grid(row=2, column=1, padx=10, pady=5)

# Phone Number Entry
Phone_Number_label = tk.Label(registration_frame, text="Insert your phone number:", font=("Cascadia Code", 10), bg='#D2B4DE')
Phone_Number_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
validate_phone_number = registration_frame.register(validate_Phone_Number_callback)
Phone_Number_entry = tk.Entry(registration_frame, validate="key", validatecommand=(validate_phone_number, '%P'))
Phone_Number_entry.grid(row=3, column=1, padx=10, pady=5)

# Email Entry
Email_label = tk.Label(registration_frame, text="Insert your email:", font=("Cascadia Code", 10), bg='#D2B4DE')
Email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
Email_entry = tk.Entry(registration_frame)
Email_entry.grid(row=4, column=1, padx=10, pady=5)

# Save Button
save_button = tk.Button(registration_frame, text="Register", bg='#BB8FCE', command=collect_data)
save_button.grid(row=5, column=1, pady=10)

# Output Label & Result
output_label = tk.Label(registration_frame, text='Registration status:', font=("Imprint MT Shadow", 12), bg=('#D2B4DE'))
output_label.grid(row=6, column=0, columnspan=2, pady=10)
output_result_label = tk.Label(registration_frame, text="")
output_result_label.grid(row=7, column=0, columnspan=2)

# Deletion Section in the Middle
deletion_frame = tk.Frame(root, bg='#D2B4DE')
deletion_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

# Email Entry for DELETE
Email_delete_label = tk.Label(deletion_frame, text="Account deactivation.\nEnter email to delete your profile:", font=("Cascadia Code", 10), bg='#D2B4DE')
Email_delete_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
Email_delete_entry = tk.Entry(deletion_frame)
Email_delete_entry.grid(row=1, column=1, padx=10, pady=5)

# Delete Button
delete_button = tk.Button(deletion_frame, text="Deactivate", bg='#BB8FCE', command=delete_data)
delete_button.grid(row=2, column=1, pady=10)

# Delete Output Label & Result
delete_output_label = tk.Label(deletion_frame, text='Deactivation status:', font=("Imprint MT Shadow", 12), bg=('#D2B4DE'))
delete_output_label.grid(row=3, column=0, columnspan=2, pady=10)
delete_result_label = tk.Label(deletion_frame, text="")
delete_result_label.grid(row=4, column=0, columnspan=2)

# Update Section on the Right
update_frame = tk.Frame(root, bg='#D2B4DE')
update_frame.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

Old_Email_label = tk.Label(update_frame, text="Insert old email to update:", font=("Cascadia Code", 10), bg='#D2B4DE')
Old_Email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
Old_Email_entry = tk.Entry(update_frame)
Old_Email_entry.grid(row=1, column=1, padx=10, pady=5)

New_First_Name_label = tk.Label(update_frame, text="Insert new first name:", font=("Cascadia Code", 10), bg='#D2B4DE')
New_First_Name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
New_First_Name_entry = tk.Entry(update_frame)
New_First_Name_entry.grid(row=2, column=1, padx=10, pady=5)

New_Last_Name_label = tk.Label(update_frame, text="Insert new last name:", font=("Cascadia Code", 10), bg='#D2B4DE')
New_Last_Name_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
New_Last_Name_entry = tk.Entry(update_frame)
New_Last_Name_entry.grid(row=3, column=1, padx=10, pady=5)

New_Phone_Number_label = tk.Label(update_frame, text="Insert new phone number:", font=("Cascadia Code", 10), bg='#D2B4DE')
New_Phone_Number_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
validate_New_Phone_Number = update_frame.register(validate_New_Phone_Number_callback)
New_Phone_Number_entry = tk.Entry(update_frame, validate="key", validatecommand=(validate_New_Phone_Number, '%P'))
New_Phone_Number_entry.grid(row=4, column=1, padx=10, pady=5)

New_Email_label = tk.Label(update_frame, text="Insert new email:", font=("Cascadia Code", 10), bg='#D2B4DE')
New_Email_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
New_Email_entry = tk.Entry(update_frame)
New_Email_entry.grid(row=5, column=1, padx=10, pady=5)

# Update Button
update_button = tk.Button(update_frame, text="Update", bg='#BB8FCE', command=update_data)
update_button.grid(row=6, column=1, pady=10)

# Update Output Label & Result
update_output_label = tk.Label(update_frame, text='Update status:', font=("Imprint MT Shadow", 12), bg=('#D2B4DE'))
update_output_label.grid(row=7, column=0, columnspan=2, pady=10)
update_result_label = tk.Label(update_frame, text="")
update_result_label.grid(row=8, column=0, columnspan=2)

root.mainloop()