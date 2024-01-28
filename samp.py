from tkinter import *
from tkinter import messagebox


#dashboard
def dashboard():
   dash = Tk()
   dash.title("Dashboard")
   dash.geometry("1500x800")

   # side panel of the dashboard
   dashside = Frame(dash, bg="cornsilk3")
   dashside.place(relx=0.0, rely=0.0, width=200, height=1000)

   name = Label(dashside, text="Side panel", bg="blue", fg="white", font=("Arial", 20))
   name.place(relx=0.0, rely=0.01, width=200)

   # Load the image
   img_path = "assets/image/customer.png"
   custimage = PhotoImage(file=img_path)
   img_path = "assets/image/createcust.png"
   createcustimage = PhotoImage(file=img_path)
   img_path = "assets/image/emplyee.png"
   empimage = PhotoImage(file=img_path)
   img_path = "assets/image/createemployee.png"
   createempimage = PhotoImage(file=img_path)
def createCust():
    custPanel = Tk()
    custPanel.title("Create Customer")
    custPanel.geometry("1500x800")

    # frame
    exframe = Frame(custPanel, bg="coral1")
    exframe.place(relx=0.15, rely=0.02, height=660, width=1002)

    heading = Label(exframe, text="Create Customer", bg="cornflowerblue", fg="white", font=("Arial", 15))
    heading.place(relx=0.0, rely=0.02, height=50, width=1000)

    labels_font = ("Arial", 12)  # Font for labels
    entry_font = ("Arial", 10)   # Font for entry boxes

    name = Label(exframe, text="Enter your name:", bg="coral1", font=labels_font)
    name.place(relx=0.07, rely=0.15)

    fathername = Label(exframe, text="Father name:", bg="coral1", font=labels_font)
    fathername.place(relx=0.5, rely=0.15)

    doblab = Label(exframe, text="Date of Birth:", bg="coral1", font=labels_font)
    doblab.place(relx=0.07, rely=0.30)

    aadhar = Label(exframe, text="Aadhar number:", bg="coral1", font=labels_font)
    aadhar.place(relx=0.5, rely=0.30)

    phoneno = Label(exframe, text="Phone No:", bg="coral1", font=labels_font)
    phoneno.place(relx=0.07, rely=0.45)

    address = Label(exframe, text="Address:", bg="coral1", font=labels_font)
    address.place(relx=0.5, rely=0.45)

    email = Label(exframe, text="Email id:", bg="coral1", font=labels_font)
    email.place(relx=0.07, rely=0.60)

    accounttype = Label(exframe, text="Account Type:", bg="coral1", font=labels_font)
    accounttype.place(relx=0.5, rely=0.60)

    creditamnt = Label(exframe, text="Credit Amount:", bg="coral1", font=labels_font)
    creditamnt.place(relx=0.07, rely=0.75)


   #ENTRYBOX
    name_entry = Entry(exframe, width=30, font=entry_font)
    name_entry.place(relx=0.2, rely=0.15)

    father_name_entry = Entry(exframe, width=30, font=entry_font)
    father_name_entry.place(relx=0.7, rely=0.15)

    dob_entry = Entry(exframe, width=30, font=entry_font)
    dob_entry.place(relx=0.2, rely=0.30)

    aadhar_entry = Entry(exframe, width=30, font=entry_font)
    aadhar_entry.place(relx=0.7, rely=0.30)

    phone_no_entry = Entry(exframe, width=30, font=entry_font)
    phone_no_entry.place(relx=0.2, rely=0.45)

    address_entry = Entry(exframe, width=30, font=entry_font)
    address_entry.place(relx=0.7, rely=0.45)

    email_entry = Entry(exframe, width=30, font=entry_font)
    email_entry.place(relx=0.2, rely=0.60)

    account_type_var = StringVar()
    account_type_var.set("Select Account Type")
    account_types = ["Saving Account", "Salary Account", "Open Account", "NRI Account"]
    account_dropdown = OptionMenu(exframe, account_type_var, *account_types)
    account_dropdown.place(relx=0.7, rely=0.60)

    credit_amount_entry = Entry(exframe, width=30, font=entry_font)
    credit_amount_entry.place(relx=0.2, rely=0.75)

    submit = Button(exframe, text="Submit", font=("Arial", 12)).place(relx=0.8, rely=0.90)

    custPanel.mainloop()


createCust()

   # Create buttons with images
   cust = Button(dashside, text="Create New Customer", image=createcustimage, compound=LEFT)
   cust.place(relx=0.02, rely=0.10)
   createCust()


   emp = Button(dashside, text="Create New Employee", image=createempimage, compound=LEFT)
   emp.place(relx=0.02, rely=0.20)

   viewcust = Button(dashside, text="View Customers", image=custimage, compound=LEFT)
   viewcust.place(relx=0.02, rely=0.30, width=170)

   viewemp = Button(dashside, text="View Employees", image=empimage, compound=LEFT)
   viewemp.place(relx=0.02, rely=0.40, width=170)

   dash.mainloop()

dashboard()

# Create the main window
log = Tk()
log.title("Login Panel")
log.geometry("1500x800")

# main login panel
# Create a frame
log1 = Frame(log, bg="bisque2", height=300, width=500)
log1.place(relx=0.3, rely=0.25)

# Create a heading label inside the window
head = Label(log, text="Indian Overseas Bank", bg="blue", fg="white", font=("Arial", 20))
head.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create the username label and entry field within the frame
usrn_label = Label(log1, text="Username:", bg="bisque2", font=("Arial", 15))
usrn_label.place(relx=0.05, rely=0.1)

usrn_entry = Entry(log1, width=50)
usrn_entry.place(relx=0.3, rely=0.12, height=20)

passw_label = Label(log1, text="Password:", bg="bisque2", font=("Arial", 15))
passw_label.place(relx=0.05, rely=0.30)

passw_entry = Entry(log1, width=50, show="*")  # Hide password with 'show="*"' attribute
passw_entry.place(relx=0.3, rely=0.32, height=20)

def checkLogin():
    username = usrn_entry.get()
    password = passw_entry.get()
    if username == 'admin' and password == '123':
        messagebox.showinfo("Success", "Your login was successful")
        log.destroy()
        dashboard()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login = Button(log1, text="Login", command=checkLogin)  # Remove '()' from command
login.place(rely=0.50, relx=0.40, width=70)

# Run the application
log.mainloop()
