from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
import tk


#employee
def employform():
        def submit_form():
            name = name_entry.get()
            dob = dob_entry.get()
            gender = gender_var.get()
            qualification = qualification_combobox.get()
            phone_number = phone_entry.get()
            address = address_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()

            # You can add validation logic here

            # Create a string with the form data
            data = f"Name: {name}\nDOB: {dob}\nGender: {gender}\nQualification: {qualification}\nPhone Number: {phone_number}\nAddress: {address}\nUsername: {username}\nPassword: {password}\n"

            # Write the data to a text file
            with open('employee_details.txt', 'a') as file:
                file.write(data)
                file.write("\n")

        # Create the Tkinter window
        emp = Tk()
        emp.title("Employee Details Form")
        emp.geometry("1000x700")  # Set the geometry of the window

        name_label = Label(emp, text="Name:")
        name_label.place(relx=0.02, rely=0.10)
        name_entry = Entry(emp)
        name_entry.place(relx=0.10, rely=0.10)

        dob_label = Label(emp, text="Date of Birth:")
        dob_label.place(relx=0.02, rely=0.20)
        dob_entry = Entry(emp)
        dob_entry.place(relx=0.10, rely=0.20)

        gender_label = Label(emp, text="Gender:")
        gender_label.place(relx=0.02, rely=0.30)
        gender_var = StringVar()
        gender_male_radio = Radiobutton(emp, text="Male", variable=gender_var, value="Male")
        gender_male_radio.place(relx=0.10, rely=0.30)
        gender_female_radio = Radiobutton(emp, text="Female", variable=gender_var, value="Female")
        gender_female_radio.place(relx=0.15, rely=0.30)

        qualification_label = Label(emp, text="Qualification:")
        qualification_label.place(relx=0.02, rely=0.40)
        qualification_combobox = Combobox(emp, values=["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
        qualification_combobox.place(relx=0.10, rely=0.40)

        phone_label = Label(emp, text="Phone Number:")
        phone_label.place(relx=0.02, rely=0.50)
        phone_entry = Entry(emp)
        phone_entry.place(relx=0.10, rely=0.50)

        address_label = Label(emp, text="Address:")
        address_label.place(relx=0.02, rely=0.60)
        address_entry = Entry(emp)
        address_entry.place(relx=0.10, rely=0.60)

        username_label = Label(emp, text="Username:")
        username_label.place(relx=0.02, rely=0.70)
        username_entry = Entry(emp)
        username_entry.place(relx=0.10, rely=0.70)

        password_label = Label(emp, text="Password:")
        password_label.place(relx=0.02, rely=0.80)
        password_entry = Entry(emp, show="*")
        password_entry.place(relx=0.10, rely=0.80)

        confirm_password_label = Label(emp, text="Confirm Password:")
        confirm_password_label.place(relx=0.02, rely=0.90)
        confirm_password_entry = Entry(emp, show="*")
        confirm_password_entry.place(relx=0.10, rely=0.90)

        # Create a submit button
        submit_button = Button(emp, text="Submit", command=submit_form)
        submit_button.place(relx=0.50, rely=0.95)

        # Run the application
        emp.mainloop()


def customers():
    def submit_form():
        name = name_entry.get()
        dob = dob_entry.get()
        gender = gender_var.get()
        qualification = qualification_combobox.get()
        phone_number = phone_entry.get()
        address = address_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # You can add validation logic here

        # Create a string with the form data
        data = f"Name: {name}\nDOB: {dob}\nGender: {gender}\nQualification: {qualification}\nPhone Number: {phone_number}\nAddress: {address}\nUsername: {username}\nPassword: {password}\n"

        # Write the data to a text file
        with open('customers_details.txt', 'a') as file:
            file.write(data)
            file.write("\n")

    # Create the Tkinter window
    cust = Tk()
    cust.title("Customer Details Form")
    cust.geometry("1000x700")  # Set the geometry of the window

    name_label = Label(cust, text="Name:")
    name_label.place(relx=0.02, rely=0.10)
    name_entry = Entry(cust)
    name_entry.place(relx=0.10, rely=0.10)

    dob_label = Label(cust, text="Date of Birth:")
    dob_label.place(relx=0.02, rely=0.20)
    dob_entry = Entry(cust)
    dob_entry.place(relx=0.10, rely=0.20)

    gender_label = Label(cust, text="Gender:")
    gender_label.place(relx=0.02, rely=0.30)
    gender_var = StringVar()
    gender_male_radio = Radiobutton(cust, text="Male", variable=gender_var, value="Male")
    gender_male_radio.place(relx=0.10, rely=0.30)
    gender_female_radio = Radiobutton(cust, text="Female", variable=gender_var, value="Female")
    gender_female_radio.place(relx=0.15, rely=0.30)

    qualification_label = Label(cust, text="Qualification:")
    qualification_label.place(relx=0.02, rely=0.40)
    qualification_combobox = Combobox(cust, values=["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
    qualification_combobox.place(relx=0.10, rely=0.40)

    phone_label = Label(cust, text="Phone Number:")
    phone_label.place(relx=0.02, rely=0.50)
    phone_entry = Entry(cust)
    phone_entry.place(relx=0.10, rely=0.50)

    address_label = Label(cust, text="Address:")
    address_label.place(relx=0.02, rely=0.60)
    address_entry = Entry(cust)
    address_entry.place(relx=0.10, rely=0.60)

    username_label = Label(cust, text="Username:")
    username_label.place(relx=0.02, rely=0.70)
    username_entry = Entry(cust)
    username_entry.place(relx=0.10, rely=0.70)

    password_label = Label(cust, text="Password:")
    password_label.place(relx=0.02, rely=0.80)
    password_entry = Entry(cust, show="*")
    password_entry.place(relx=0.10, rely=0.80)

    confirm_password_label = Label(cust, text="Confirm Password:")
    confirm_password_label.place(relx=0.02, rely=0.90)
    confirm_password_entry = Entry(cust, show="*")
    confirm_password_entry.place(relx=0.10, rely=0.90)

    # Create a submit button
    submit_button = Button(cust, text="Submit", command=submit_form)
    submit_button.place(relx=0.50, rely=0.95)

    # Run the application
    cust.mainloop()



def load_data_from_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(': ')
                data.append(value)
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"File not found: {file_path}")
    return data

def create_employees():
    messagebox.showinfo("Create Employees", "Functionality to create employees")
    # Placeholder code for creating employees
    print("Create employees function")

def create_customers():
    messagebox.showinfo("Create Customers", "Functionality to create customers")
    # Placeholder code for creating customers
    print("Create customers function")

def dashboard():
    dash = tk.Tk()
    dash.title("Dashboard")
    dash.geometry('1200x600')


    sidepanel3 = Frame(dash, bg='bisque4', height=700, width=200)
    sidepanel3.place(relx=0.0)

    # Load images
    create_emp_img = PhotoImage(file="emplyee.png")
    create_cut_img = PhotoImage(file="customer.png")

    # Create buttons with images and text
    create_emp = Button(dash, text="Create Employees", image=create_emp_img, compound="left", command=create_employees)
    create_emp.place(relx=0.015, rely=0.05)

    create_cut = Button(dash, text="Create Customers", image=create_cut_img, compound="left", command=create_customers)
    create_cut.place(relx=0.015, rely=0.20)

    view = tk.Frame(dash)
    view.place(relx=0.20, rely=0.10, height=400, width=900)

    tree = ttk.Treeview(view, columns=('Name', 'DateOfBirth', 'Phoneno', 'Address'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('DateOfBirth', text='DateOfBirth')
    tree.heading('Phoneno', text='Phone Number')
    tree.heading('Address', text='Address')
    tree.pack()

    # Load data from file
    file_path = 'customers_details.txt'
    data = load_data_from_file(file_path)

    # Add your treeview data or further configuration here if needed
    for item in data:
        values = item.split('\n')  # Split by newline to extract individual values
        tree.insert('', 'end', values=values[:-1])  # Omit the last empty value from the split

    dash.mainloop()



#main panel
root = Tk()
root.title("Login Panel")
root.geometry('400x400')
#function
def submitlog():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'admin' and password == '123':
        sucessmessage = messagebox.showinfo(title="Success",message="Your login successful")
        root.destroy()
        dashboard()
    else:
        message = messagebox.showwarning(title="Warning", message="Your Credential is Wrong Try Again.!")

# panel
sidepanel1 = Frame(root, bg='chartreuse1', height=500, width=100)
sidepanel1.pack_propagate(0)  # This line prevents the frame from resizing
sidepanel1.pack(side='left', fill='both', expand=True)

sidepanel2 = Frame(root, bg='antiquewhite1', height=500, width=400)
sidepanel2.pack(side='right', fill='both', expand=True)

# Label
heading = Label(text="Welcome to Login Panel", bg='blue3')
heading.place(relx=0.45, rely=0.03)
username_label = Label(text="Username:", bg='antiquewhite1')
username_label.place(relx=0.30, rely=0.20)
password_label = Label(text="Password:", bg='antiquewhite1')
password_label.place(relx=0.30, rely=0.30)

# Entry boxes
username_entry = Entry(root, width=30)
username_entry.place(relx=0.45, rely=0.20)
password_entry = Entry(root, show="*", width=30)  # The show option hides the password
password_entry.place(relx=0.45, rely=0.30)

#Button
submit_btn = Button(root, width=20, text='Login', activebackground='green', command=lambda: submitlog())
submit_btn.place(relx=0.50, rely=0.40)

root.mainloop()
