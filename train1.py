import tkinter as tk
from tkinter import ttk

# Read data from the file
file_path = 'new_customer_details.txt'
data = []

with open(file_path, 'r') as file:
    current_entry = {}
    for line in file:
        if line.strip():
            key, value = map(str.strip, line.split(':'))
            current_entry[key] = value
        else:
            data.append(current_entry)
            current_entry = {}

# Create Tkinter window
dash = tk.Tk()
dash.title("Data Display")

# Create Treeview with columns
columns = ('Name', 'Fathername', 'DOB', 'Aadhar', 'Email', 'Accountno', 'Accounttype', 'Amount')
tree = ttk.Treeview(dash, columns=columns, show='headings')

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)  # Adjust the width as needed

# Insert data into the Treeview
for row in data:
    tree.insert('', 'end', values=(
        row.get('Name', ''),
        row.get('Fathername', ''),
        row.get('DOB', ''),
        row.get('Aadhar', ''),
        row.get('Email', ''),
        row.get('Accountno', ''),
        row.get('Accounttype', ''),
        row.get('Amount', '')
    ))

# Place the Treeview
tree.place(relx=0.05, rely=0.05, height=400, width=900)

# Run the Tkinter main loop
dash.mainloop()
