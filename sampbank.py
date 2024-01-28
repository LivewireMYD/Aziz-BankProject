from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import smtplib
import random
import string
import pymysql as mysql

databasename = ('bankmanagement',)
connection = mysql.connect(host='localhost', user='root', password='livewire')
cursor = connection.cursor()
cursor.execute('SHOW DATABASES')

for x in cursor:
    if x == databasename:
        print("Already database available")
        connection = mysql.connect(host='localhost', user='root', password='livewire', database=databasename[0])
        cursor = connection.cursor()
        break
    else:
        print("else ", x)
        connection = mysql.connect(host='localhost', user='root', password='livewire')
        cursor = connection.cursor()

        # Create the database
        cursor.execute(f'CREATE DATABASE {databasename[0]}')

        # Switch to the newly created database
        cursor.execute(f'USE {databasename[0]}')

def createCustomer():
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

    acountno = Label(exframe, text="Account No:", bg="coral1", font=labels_font)
    acountno.place(relx=0.5, rely=0.75)

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

    accountno = Entry(exframe, width=30, font=entry_font)
    accountno.place(relx=0.7, rely=0.75)


    account_types = ["Saving Account", "Salary Account", "Open Account", "NRI Account"]
    account_type_var = StringVar()
    account_type_var.set(account_types[0])  # Set default value
    account_dropdown = Combobox(exframe, textvariable=account_type_var, values=account_types, state="readonly")
    account_dropdown.place(relx=0.7, rely=0.60, width=150)

    # Bind event for combobox selection
    account_dropdown.bind("<<ComboboxSelected>>")

    #create drop down [salary,NRI,Open, Saving]

    credit_amount_entry = Entry(exframe, width=30, font=entry_font)
    credit_amount_entry.place(relx=0.2, rely=0.75)

    def save_details():
        name = name_entry.get()
        father_name = father_name_entry.get()
        dob = dob_entry.get()
        aadhar = aadhar_entry.get()
        phone_no = phone_no_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        account_type = account_type_var.get()
        credit_amount = credit_amount_entry.get()
        account_no = accountno.get()

        # Prepare the data to be written to the file
        table_name="customer_details"
        cursor.execute('SHOW DATABASES')
        for x in cursor:
            if x == cursor:
                print('tabel is already available')
            else:
                cursor.execute(f'CREATE TABLE {table_name[0]} (customername varchar(250),fathername varchar(250),dob varchar(250), aadharno varchar(16), primary key(aadharno), accountype varchar(250), amount varchar(255),account_no varchar(255) )')
        s = f"INSERT INTO {table_name[0]}(customername,fathername,dob,aadharno,accountype,amount,account_no) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        t = (name,father_name,dob,aadhar,phone_no,address,email,account_type,credit_amount,account_no)
        cursor.execute(s,t)
        connection.commit()

        # Clear entry fields after submission
        name_entry.delete(0, END)
        father_name_entry.delete(0, END)
        dob_entry.delete(0, END)
        aadhar_entry.delete(0, END)
        phone_no_entry.delete(0, END)
        address_entry.delete(0, END)
        email_entry.delete(0, END)
        credit_amount_entry.delete(0, END)

    # Optionally, you can display a success message or perform any other action after submission

    submit = Button(exframe, text="Submit", font=("Arial", 12), command=save_details)
    submit.place(relx=0.8, rely=0.90)

    custPanel.mainloop()


def createEmployee():
    custPanel = Tk()
    custPanel.title("Create Customer")
    custPanel.geometry("1500x800")

    # frame
    exframe = Frame(custPanel, bg="aquamarine1")
    exframe.place(relx=0.15, rely=0.02, height=660, width=1002)



    heading = Label(exframe, text="Create Customer", bg="aquamarine3", fg="white", font=("Arial", 15))
    heading.place(relx=0.0, rely=0.02, height=50, width=1000)

    labels_font = ("Arial", 12)  # Font for labels
    entry_font = ("Arial", 10)   # Font for entry boxes

    name = Label(exframe, text="Enter your name:", bg="aquamarine1", font=labels_font)
    name.place(relx=0.07, rely=0.15)

    fathername = Label(exframe, text="Father name:", bg="aquamarine1", font=labels_font)
    fathername.place(relx=0.5, rely=0.15)

    doblab = Label(exframe, text="Date of Birth:", bg="aquamarine1", font=labels_font)
    doblab.place(relx=0.07, rely=0.30)

    aadhar = Label(exframe, text="Aadhar number:", bg="aquamarine1", font=labels_font)
    aadhar.place(relx=0.5, rely=0.30)

    phoneno = Label(exframe, text="Phone No:", bg="aquamarine1", font=labels_font)
    phoneno.place(relx=0.07, rely=0.45)

    address = Label(exframe, text="Address:", bg="aquamarine1", font=labels_font)
    address.place(relx=0.5, rely=0.45)

    email = Label(exframe, text="Email id:", bg="aquamarine1", font=labels_font)
    email.place(relx=0.07, rely=0.60)


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


    #create drop down [salary,NRI,Open, Saving]
    def save_details():
            name = name_entry.get()
            father_name = father_name_entry.get()
            dob = dob_entry.get()
            aadhar = aadhar_entry.get()
            phone_no = phone_no_entry.get()
            address = address_entry.get()
            email = email_entry.get()

            # Prepare the data to be written to the file
            data = f"Name: {name}\nFather's Name: {father_name}\nDate of Birth: {dob}\nAadhar Number: {aadhar}\nPhone Number: {phone_no}\nAddress: {address}\nEmail: {email}"

            # Write data to the file
            with open("new_employee_details.txt", "a") as file:
                file.write(data)
                file.write("\n")  # Adding a line break for next entry

            # Clear entry fields after submission
            name_entry.delete(0, END)
            father_name_entry.delete(0, END)
            dob_entry.delete(0, END)
            aadhar_entry.delete(0, END)
            phone_no_entry.delete(0, END)
            address_entry.delete(0, END)
            email_entry.delete(0, END)

        # Optionally, you can display a success message or perform any other action after submission
    submit = Button(exframe, text="Submit", font=("Arial", 12), command=save_details)
    submit.place(relx=0.8, rely=0.90)

    custPanel.mainloop()






def dashboard():
   dash = Tk()
   dash.title("Dashboard")
   dash.geometry("1500x800")



   def ViewEmployee():
    columns = ('name', 'fathername', 'dob', 'aadhar', 'email')
    tree = Treeview(dash, columns=columns, show='headings')
    # define headings
    tree.heading('name', text='Name')
    tree.column('name', width=60)
    tree.heading('fathername', text='Father Name')
    tree.column('fathername', width=60)
    tree.heading('dob', text='Date of Birth',)
    tree.column('dob', width=40)
    tree.heading('aadhar', text='Aadhar No')
    tree.column('aadhar', width=40)
    tree.heading('email', text='Email')
    tree.column('email', width=40)
    tree.place(relx=0.150, rely=0.00, height=800, width=1150)


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


   # Create buttons with images
   cust = Button(dashside, text="Create New Customer", image=createcustimage, compound=LEFT, command=createCustomer)
   cust.place(relx=0.02, rely=0.10)

   emp = Button(dashside, text="Create New Employee", image=createempimage, compound=LEFT, command=createEmployee)
   emp.place(relx=0.02, rely=0.20)

   # viewcust = Button(dashside, text="View Customers", image=custimage, compound=LEFT, command=viewCustomer)
   # viewcust.place(relx=0.02, rely=0.30, width=170)
   #
   # viewemp = Button(dashside, text="View Employees", image=empimage, compound=LEFT, command=ViewEmployee)
   # viewemp.place(relx=0.02, rely=0.40, width=170)


   dash.mainloop()

dashboard()

# def generate_password(length=10):
#     print("generatep")
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password
# a=""
# newpassword = generate_password()
# # Function to send login credentials via email
# def send_email():
#     sender_email = 'ultemateaziz64@gmail.com'
#     app_password = 'qfpi xyhv qbwq agzh'
#     receiver_email = 'livewiremyd@gmail.com'
#     subject = 'Subject of the Email'
#     body = f'your user name: admin.\n password: {newpassword}'
#
#     # Compose the email message
#     message = f'Subject: {subject}\n\n{body}'
#
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()  # Enable TLS encryption
#             server.login(sender_email, app_password)
#             server.sendmail(sender_email, receiver_email, message)
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")
#
# # Function to handle the login process
# def checkLogin():
#     username = usrn_entry.get()
#     password = passw_entry.get()
#     print(username, password, newpassword)
#     if username == 'admin' and password == newpassword:
#         alert = messagebox.showinfo("Success", "Your Login was Successful!")
#         log.destroy()
#         dashboard()
#     else:
#         alert = messagebox.showerror("Error", "Your credentials are incorrect!")
#
# # Create the main window
# log = Tk()
# log.title("Login Panel")
# log.geometry("1500x800")
#
# # main login panel
# # Create a frame
# log1 = Frame(log, bg="bisque2", height=300, width=500)
# log1.place(relx=0.3, rely=0.25)
#
# # Create a heading label inside the window
# head = Label(log, text="Ind Bank", bg="blue", fg="white", font=("Arial", 20))
# head.place(relx=0.5, rely=0.1, anchor=CENTER)
#
# # Create the username label and entry field within the frame
# usrn_label = Label(log1, text="Username:", bg="bisque2", font=("Arial", 15))
# usrn_label.place(relx=0.05, rely=0.1)
#
# usrn_entry = Entry(log1, width=50)
# usrn_entry.place(relx=0.3, rely=0.12, height=20)
#
# passw_label = Label(log1, text="Password:", bg="bisque2", font=("Arial", 15))
# passw_label.place(relx=0.05, rely=0.30)
#
# passw_entry = Entry(log1, width=50, show="*")  # Hide password with 'show="*"' attribute
# passw_entry.place(relx=0.3, rely=0.32, height=20)
#
# login = Button(log1, text="Login", command=checkLogin)  # Remove '()' from command
# login.place(rely=0.50, relx=0.40, width=70)
#
# send_email()
# # Run the application
# log.mainloop()
