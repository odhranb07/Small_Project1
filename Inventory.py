import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter import font 

inventory =[]

def add_item():
    name = simpledialog.askstring("Add Item", "Please enter the name of the item:", parent=window)
    if name is None:
        return

    category = simpledialog.askstring("Add Item", "Please enter the category of the item:", parent=window)
    if category is None:
        return

    quantity = simpledialog.askinteger("Add Item", "Please enter the quantity of the item:", parent=window, minvalue=0)
    if quantity is None:
        return

    price = simpledialog.askfloat("Add Item", "Please enter the price of the item:", parent=window, minvalue=0)
    if price is None:
        return

    item={
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    inventory.append(item)
    table.insert("", tk.END, values=(len(inventory), name, quantity, f"${price:.2f}"))
    messagebox.showinfo("Item Added", f"{name} was added to the inventory.", parent=window)

#main window

window=tk.Tk()
window.title("Inventory Management System")
window.geometry("800x600")

#window title

title_label=tk.Label(window,text="Inventory Management System",font=("Arial",24))
title_label.pack(pady=20)
columns = ("ID", "Name", "Quantity", "Price")
table = ttk.Treeview(window, columns=columns, show="headings")
add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.pack(pady=10)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

#create table headings
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Quantity", text="Quantity")
table.heading("Price", text="Price")

#displaying the table
table.pack(
    pady=20,
    padx=20,
    fill=tk.BOTH,
    expand=True
)

window.mainloop()
