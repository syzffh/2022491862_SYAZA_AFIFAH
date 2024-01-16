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

# Coding and Calculation
def collect_data():
    # List to store selected stages
    selected_menu = []

    # Check which menu are selected
    if menu_type_var_Puteri_Favorite.get():
        selected_menu.append("Puteri's Favorite")
    if menu_type_var_Tasha_Favorite.get():
        selected_menu.append("Tasha's Favorite")
    if menu_type_var_Syaza_Favorite.get():
        selected_menu.append("Syaza's Favorite")
    if menu_type_var_Amalin_Favorite.get():
        selected_menu.append("Amalin's Favorite")
    if menu_type_var_Best_Seller.get():
        selected_menu.append("Best Seller")

    # Dictionary to store quantities
    quantities = {
        "Puteri's Favorite": int(puteri_quantity_var.get()) if puteri_quantity_var.get() else 0,
        "Tasha's Favorite": int(tasha_quantity_var.get()) if tasha_quantity_var.get() else 0,
        "Syaza's Favorite": int(syaza_quantity_var.get()) if syaza_quantity_var.get() else 0,
        "Amalin's Favorite": int(amalin_quantity_var.get()) if amalin_quantity_var.get() else 0,
        "Best Seller": int(best_seller_quantity_var.get()) if best_seller_quantity_var.get() else 0,
    }

    name = str(name_entry.get())
    address = str(address_entry.get())
    phone_number_str = phone_number_entry.get()
    phone_number = int(phone_number_str) if phone_number_str else 0

    menu_type = selected_menu

    # The price
    price = {
        "Puteri's Favorite": 30,
        "Tasha's Favorite": 29,
        "Syaza's Favorite": 28,
        "Amalin's Favorite": 26,
        "Best Seller": 27,
    }

    # Calculate the total price.
    total_price = sum(price[menu_item] * quantities[menu_item] for menu_item in selected_menu)

    # To insert Data into the database
    sql = "INSERT INTO `menu` (name, address, phone_number, menu_type, quantity, price) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, address, phone_number, ",".join(selected_menu), ",".join(str(quantities[menu_item]) for menu_item in selected_menu), total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back the output.
    output_label.config(text=f"Total Price: RM{total_price}", bg='#D2B4DE', font=10)


# Main window.
root = tk.Tk()
root.title("HUH? CAFE")
root.geometry('1000x1000')
root.config(bg='#D2B4DE')

# Page Title
label = tk.Label(root, text='HUH? CAFE ORDERING SYSTEM', font=("FZShuTi", 30, "bold"), bg='#D2B4DE')
label.pack(ipadx=20, ipady=20)

# Prices List 
prices_text = tk.Text(root, height=12, width=100, font=("Arial Black", 9), bg='#EBDEF0')
prices_text.pack(pady=20)

# The defined list
prices_text.insert(tk.END, "Menu & Prices:\n\n")
prices_text.insert(tk.END, "Puteri's Favorite: Creamy Carbonara Pasta, Cromboloni, Earl Grey Tea \nPrice: RM30\n\n")
prices_text.insert(tk.END, "Tasha's Favorite: Pesto Pasta, Croissant, Honey Lemon \nPrice: RM29\n\n")
prices_text.insert(tk.END, "Syaza's Favorite: Beef Bolognese Pasta, Pain au Chocolat, Iced Chocolate \nPrice: RM28\n\n")
prices_text.insert(tk.END, "Amalin's Favorite: Tomyum Thai Pasta, Egg Tart, Hazelnut Latte \nPrice: RM26\n\n")
prices_text.insert(tk.END, "Best Seller: Gigi Hadid Pasta, Choux Creme, Lychee Strawberry \nPrice: RM27\n\n")
prices_text.configure(state='disabled')

# User Information Frame
user_info_frame = tk.LabelFrame(root, text="User Information", bg='#EBDEF0')
user_info_frame.pack(side=tk.LEFT, padx=20, pady=10, fill="both", expand=True)

# User name entry
name_label = tk.Label(user_info_frame, text="Enter your name:", bg='#EBDEF0', font= 'Century')
name_entry = tk.Entry(user_info_frame)

# User address entry
address_label = tk.Label(user_info_frame, text="Enter your address:",bg='#EBDEF0',font= 'Century')
address_entry = tk.Entry(user_info_frame)

# User phone number entry
phone_number_label = tk.Label(user_info_frame, text="Enter your phone number:",bg='#EBDEF0',font= 'Century')
phone_number_entry = tk.Entry(user_info_frame)

# Organize widgets using grid
name_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
name_entry.grid(row=0, column=1, pady=(0, 5))

address_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
address_entry.grid(row=1, column=1, pady=(0, 5))  

phone_number_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
phone_number_entry.grid(row=2, column=1, pady=(0, 5))

# Order Summary Frame
order_summary_frame = tk.LabelFrame(root, text="Order Summary", bg='#EBDEF0')
order_summary_frame.pack(side=tk.LEFT, padx=20, pady=10, fill="both", expand=True)

# Menu Type Checkboxes
menu_type_var_Puteri_Favorite = tk.BooleanVar(order_summary_frame)
menu_type_var_Tasha_Favorite = tk.BooleanVar(order_summary_frame)
menu_type_var_Syaza_Favorite = tk.BooleanVar(order_summary_frame)
menu_type_var_Amalin_Favorite = tk.BooleanVar(order_summary_frame)
menu_type_var_Best_Seller = tk.BooleanVar(order_summary_frame)

Puteri_Favorite_checkbox = tk.Checkbutton(order_summary_frame, text="Puteri's Favorite",bg='#EBDEF0',font= 'Century', variable=menu_type_var_Puteri_Favorite)
Puteri_Favorite_checkbox.grid(row=0, column=0, sticky="w", pady=(0, 5))

# Quantity entry for Puteri's Favorite
puteri_quantity_label = tk.Label(order_summary_frame, text="Quantity:", bg='#EBDEF0', font=('Century', 9))
puteri_quantity_var = tk.Entry(order_summary_frame, font=('Century', 9))

puteri_quantity_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
puteri_quantity_var.grid(row=1, column=1, pady=(0, 5))

Tasha_Favorite_checkbox = tk.Checkbutton(order_summary_frame, text="Tasha's Favorite",bg='#EBDEF0',font= 'Century', variable=menu_type_var_Tasha_Favorite)
Tasha_Favorite_checkbox.grid(row=2, column=0, sticky="w", pady=(0, 5))

# Quantity entry for Tasha's Favorite
tasha_quantity_label = tk.Label(order_summary_frame, text="Quantity:",bg='#EBDEF0',font= ('Century',9))
tasha_quantity_var = tk.Entry(order_summary_frame, font=('Century',9))

tasha_quantity_label.grid(row=3, column=0, sticky="w", pady=(0, 5))
tasha_quantity_var.grid(row=3, column=1, pady=(0, 5))

Syaza_Favorite_checkbox = tk.Checkbutton(order_summary_frame, text="Syaza's Favorite",bg='#EBDEF0',font= 'Century', variable=menu_type_var_Syaza_Favorite)
Syaza_Favorite_checkbox.grid(row=4, column=0, sticky="w", pady=(0, 5))

# Quantity entry for Syaza's Favorite
syaza_quantity_label = tk.Label(order_summary_frame, text="Quantity:",bg='#EBDEF0',font= ('Century',9))
syaza_quantity_var = tk.Entry(order_summary_frame, font=('Century',9))

syaza_quantity_label.grid(row=5, column=0, sticky="w", pady=(0, 5))
syaza_quantity_var.grid(row=5, column=1, pady=(0, 5))

Amalin_Favorite_checkbox = tk.Checkbutton(order_summary_frame, text="Amalin's Favorite",bg='#EBDEF0',font= 'Century', variable=menu_type_var_Amalin_Favorite)
Amalin_Favorite_checkbox.grid(row=6, column=0, sticky="w", pady=(0, 5))

# Quantity entry for Amalin's Favorite
amalin_quantity_label = tk.Label(order_summary_frame, text="Quantity:",bg='#EBDEF0',font= ('Century',9))
amalin_quantity_var = tk.Entry(order_summary_frame, font=('Century',9))

amalin_quantity_label.grid(row=7, column=0, sticky="w", pady=(0, 5))
amalin_quantity_var.grid(row=7, column=1, pady=(0, 5))

Best_Seller_checkbox = tk.Checkbutton(order_summary_frame, text="Best Seller",bg='#EBDEF0',font= 'Century', variable=menu_type_var_Best_Seller)
Best_Seller_checkbox.grid(row=8, column=0, sticky="w", pady=(0, 5))

# Quantity entry for Best Seller
best_seller_quantity_label = tk.Label(order_summary_frame, text="Quantity:",bg='#EBDEF0',font= 'Century')
best_seller_quantity_var = tk.Entry(order_summary_frame)

best_seller_quantity_label.grid(row=9, column=0, sticky="w", pady=(0, 5))
best_seller_quantity_var.grid(row=9, column=1, pady=(0, 5))

# Save Button
save_button = tk.Button(root, text="Calculate", font=("FZShuTi", 12, "bold"), bg='#9B59B6',fg='#F9F9F7', command=collect_data)
save_button.pack(pady=10)

# Output Label & Result
total_price_label = tk.Label(root, text='Total Price:', font=("Imprint MT Shadow", 12), bg='#D2B4DE')
total_price_label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
