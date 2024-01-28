import string
import random
import smtplib
def generate_password(length=10):
    print("generatep")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
a=""
# Function to send login credentials via email
def send_email():
    newpassword = generate_password()
    sender_email = 'ultemateaziz64@gmail.com'
    app_password = 'qfpi xyhv qbwq agzh'

    receiver_email = 'livewiremyd@gmail.com'
    subject = 'Subject of the Email'
    body = f'your user name :admin.\n password: {newpassword}'

    # Compose the email message
    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

send_email()