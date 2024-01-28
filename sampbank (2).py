from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pymysql as mysql

# Connection to MySQL server
connection = mysql.connect(host='localhost', user='root', password='root')
cursor = connection.cursor()

# Name of the database to be created
database_name = 'bankmanagement'

# Check if the database already exists
cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
existing_databases = cursor.fetchall()

if not existing_databases:
    # Create the database if it doesn't exist
    cursor.execute(f'CREATE DATABASE {database_name}')
    print(f"Database '{database_name}' was created successfully")
else:
    print(f"Database '{database_name}' already exists")

# Connect to the created or existing database
connection.select_db(database_name)


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
    entry_font = ("Arial", 10)  # Font for entry boxes

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

    accountno = Label(exframe, text="Account No:", bg='coral1', font=labels_font)
    accountno.place(relx=0.5, rely=0.75)

    # ENTRYBOX
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

    accountno_entry = Entry(exframe, width=30, font=entry_font)
    accountno_entry.place(rely=0.75, relx=0.7)

    account_types = ["Saving Account", "Salary Account", "Open Account", "NRI Account"]
    account_type_var = StringVar()
    account_type_var.set(account_types[0])  # Set default value
    account_dropdown = Combobox(exframe, textvariable=account_type_var, values=account_types, state="readonly")
    account_dropdown.place(relx=0.7, rely=0.60, width=150)

    # Bind event for combobox selection
    account_dropdown.bind("<<ComboboxSelected>>")

    # create drop down [salary,NRI,Open, Saving]

    credit_amount_entry = Entry(exframe, width=30, font=entry_font)
    credit_amount_entry.place(relx=0.2, rely=0.75)

    def save_details():

        # Get user input
        name = name_entry.get()
        father_name = father_name_entry.get()
        dob = dob_entry.get()
        aadhar = aadhar_entry.get()
        phone_no = phone_no_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        account_type = account_type_var.get()
        credit_amount = credit_amount_entry.get()
        accountno = accountno_entry

        # database
        table_name = 'customers'
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        existing_tables = cursor.fetchall()

        if not existing_tables:
            # Create the 'customers' table if it doesn't exist
            create_table_query = '''
                CREATE TABLE customers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    father_name VARCHAR(255),
                    dob DATE,
                    aadhar VARCHAR(20),
                    phone_no VARCHAR(15),
                    address TEXT,
                    email VARCHAR(255),
                    account_type VARCHAR(50),
                    credit_amount DECIMAL(10,2),
                    acountno VARCHAR(255)
                )
            '''
            cursor.execute(create_table_query)
            print("Table 'customers' was created successfully")
        else:
            print("Table 'customers' already exists")

        # SQL query to insert values into the 'customers' table
        insert_query = '''
            INSERT INTO customers (name, father_name, dob, aadhar, phone_no, address, email, account_type, credit_amount, acountno)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        # Execute the query with user input
        cursor.execute(insert_query,
                       (name, father_name, dob, aadhar, phone_no, address, email, account_type, credit_amount, accountno))

        # Commit the changes to the database
        connection.commit()

        print("Values added to the database successfully")

        # Clear entry fields after submission
        name_entry.delete(0, END)
        father_name_entry.delete(0, END)
        dob_entry.delete(0, END)
        aadhar_entry.delete(0, END)
        phone_no_entry.delete(0, END)
        address_entry.delete(0, END)
        email_entry.delete(0, END)
        credit_amount_entry.delete(0, END)


    message = messagebox.showinfo()
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
    entry_font = ("Arial", 10)  # Font for entry boxes

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

    # ENTRYBOX
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

    def save_details():
        name = name_entry.get()
        father_name = father_name_entry.get()
        dob = dob_entry.get()
        aadhar = aadhar_entry.get()
        phone_no = phone_no_entry.get()
        address = address_entry.get()
        email = email_entry.get()

        # Database
        table_name = 'employee'
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        existing_tables = cursor.fetchall()

        if not existing_tables:
            # Create the 'employee' table if it doesn't exist
            create_table_query = '''
                    CREATE TABLE employee (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(255),
                        father_name VARCHAR(255),
                        dob DATE,
                        aadhar VARCHAR(20),
                        phone_no VARCHAR(15),
                        address TEXT,
                        email VARCHAR(255)
                    )
                '''
            cursor.execute(create_table_query)
            print("Table 'employee' was created successfully")
        else:
            print("Table 'employee' already exists")

        # SQL query to insert values into the 'employee' table
        insert_query = '''
                INSERT INTO employee (name, father_name, dob, aadhar, phone_no, address, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''

        # Execute the query with user input
        cursor.execute(insert_query, (name, father_name, dob, aadhar, phone_no, address, email))

        # Commit the changes to the database
        connection.commit()

        print("Values added to the database successfully")

        message = messagebox.showinfo("Information", "Data Successfully Recorded ")

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

    def viewCustomer():
        columns = ('name', 'fathername', 'dob', 'aadhar', 'email', 'accountno', 'accounttype', 'amount')
        tree = Treeview(dash, columns=columns, show='headings')
        # define headings
        tree.heading('name', text='Name')
        tree.heading('fathername', text='Father Name')
        tree.heading('dob', text='Date of Birth')
        tree.heading('aadhar', text='Aadhar No')
        tree.heading('email', text='Email')
        tree.heading('accountno', text='Account No')
        tree.heading('accounttype', text='Account Type')
        tree.heading('amount', text='Balance Amount')
        tree.place(relx=0.150, rely=0.00, height=800, width=1200)

        #treeview from the database
        select_query = '''
            SELECT name, father_name, dob, aadhar, email, account_no, account_type, balance_amount
            FROM customers
        '''

        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Insert data into the Treeview
        for row in rows:
            tree.insert('', 'end', values=row)

        # Commit the changes and close the connection
        connection.commit()


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

    viewcust = Button(dashside, text="View Customers", image=custimage, compound=LEFT, command=viewCustomer)
    viewcust.place(relx=0.02, rely=0.30, width=170)

    viewemp = Button(dashside, text="View Employees", image=empimage, compound=LEFT)
    viewemp.place(relx=0.02, rely=0.40, width=170)

    dash.mainloop()


# delete this
dashboard()

# main panel
# def generate_password(length=10):
#     print("generatep")
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password
# a=""
# newpassword = generate_password()
# def send_email(newpassword):
#     sender_email = 'ultemateaziz64@gmail.com'
#     app_password = 'rfyj burw ogyw msrh '
#     receiver_email = 'livewiremyd@gmail.com'
#     subject = 'Login Password for Python GUI Application'
#
#     # Compose the email body using HTML for formatting
#     body = f"""
#     <html>
#         <body style="font-family: 'Arial', sans-serif; font-size: 14px; color: #333;">
#             <p>Dear User,</p>
#             <p>I trust this email finds you in good spirits.</p>
#             <p>As part of our ongoing commitment to security, we have implemented a dynamic password system to enhance the protection of your account.</p>
#             <p>Below, you will find your unique login credentials:</p>
#             <p><b>Username:</b> <span style="color: #3498db; font-weight: bold; font-style: italic;">Admin</span></p>
#             <p><b>Password:</b> <span style="color: #2ecc71; font-weight: bold; font-style: italic;">{newpassword}</span></p>
#             <p>Please ensure that you copy and paste both the username and dynamic password accurately into the application. This dynamic password is time-sensitive and will change periodically for added security.</p>
#             <p>Thank you for your cooperation and commitment to ensuring the safety of your account.</p>
#             <br>
#             <p><span style="font-weight: bold;">Best regards,</span></p>
#             <p><span style="font-weight: bold;">Developer MD Aziz</span></p>
#         </body>
#     </html>
#     """
#
#     # Create the MIME message with HTML content
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "html"))
#
#     try:
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()  # Enable TLS encryption
#             server.login(sender_email, app_password)
#             server.sendmail(sender_email, receiver_email, message.as_string())
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")
#
# # Example usage
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
# new_password = "your_dynamic_password"
# send_email(newpassword)
# # Run the application
# log.mainloop()
