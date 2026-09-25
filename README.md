# Inventory management system built with python and tkinter
features:
add an item through a graphical button and dialog boxes
store the item name, quantity, category and price
display items in a table 
validate quantity and price values
cancel safely without crashing the program

How it works
when the user clicks the add item button, the python function add_item() runs. When said function runs it then opens dialogue boxes which ask for
item name
category
quantity
price

the information is stored in a python directory and is then added to the inventory list

python code:
item = {
    "name": name,
    "category": category,
    "quantity": quantity,
    "price": price
}
said item is then added to the table using tkinter treeview widget

i used tkinters dialog boxes instead of pythons input() function as this is a graphical application. therefore using input() would make the program wait for information in the terminal which would then lead the window to seem frozen.I found this out when i went to click the add item button and it would not work so I used tkinters dialog boxes widget as the fix.

requirements:
tkinter
python 3
however tkinter is included with python installations

#running the program
open a terminal in visual studio code and run:
python inventory.py
then click add item to enter a new inventory item.

#summary
overall the project was very fun to develop and a good first project to do.
