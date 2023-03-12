import tkinter as tk
import tkinter.ttk as ttk

# Define a function to retrieve all employee data
def retrieve_all():
    employees = tree.get_children()
    for employee in employees:
        data = tree.item(employee)['values']
        print(data)

# Define a function to add an employee
def add_employee():
    name = name_entry.get()
    city = city_entry.get()
    street = street_entry.get()
    tree.insert("", tk.END, values=(name, city, street))

# Define a function to remove an employee
def remove_employee():
    selected = tree.selection()
    for item in selected:
        tree.delete(item)

# Define a function to clear the table widget
def clear_table():
    tree.delete(*tree.get_children())

# Define a function to clear the entry widgets
def clear_entries():
    name_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    street_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Employee Database")

# Create the treeview widget
tree = ttk.Treeview(root, columns=("name", "city", "street"), show="headings")
tree.heading("name", text="Name")
tree.heading("city", text="City")
tree.heading("street", text="Street")
tree.pack()

# Create the entry widgets
name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

city_label = tk.Label(root, text="City")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

street_label = tk.Label(root, text="Street")
street_label.pack()
street_entry = tk.Entry(root)
street_entry.pack()

# Create the button widgets
retrieve_button = tk.Button(root, text="Retrieve All", command=retrieve_all)
retrieve_button.pack()

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.pack()

remove_button = tk.Button(root, text="Remove Employee", command=remove_employee)
remove_button.pack()

clear_table_button = tk.Button(root, text="Clear Table", command=clear_table)
clear_table_button.pack()

clear_entries_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_entries_button.pack()

# Start the main loop
root.mainloop()

