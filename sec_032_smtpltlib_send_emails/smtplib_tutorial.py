import smtplib

# ---------------------------- GMAIL ----------------------------- #
GMAIL_EMAIL = "random_test@gmail.com"
GMAIL_PASSWORD = "generated_password"         # this password is genreated after enabling 2 steps verification -> generate app password 

# Set up the SMTP server details for Gmail
SMT_SERVER = 'smtp.gmail.com'              # special for every email provider
# ---------------------------------------------------------------- #


# ---------------------------- YAHOO ----------------------------- #
# Set up your Yahoo email credentials
YAHOO_EMAIL = 'random_test@yahoo.com'

# Set up the SMTP server details for Yahoo
# smtp_server = 'smtp.mail.yahoo.com'
# smtp_port = 587  # Yahoo's SMTP server port
# ---------------------------------------------------------------- #



# Create a connection to the SMTP server
try:
    connection = smtplib.SMTP(SMT_SERVER)
    connection.starttls()  # Enable TLS encryption
    connection.login(user=GMAIL_EMAIL, password=GMAIL_PASSWORD)  # Log in to your Yahoo account
except Exception as e:
    print("Error: Unable to connect to the SMTP server.")
    print(e)
    exit()

# Compose your email message
subject = 'Test Email from Python'
body = 'This is a test email sent using Python.'
sender_email = GMAIL_EMAIL
receiver_email = YAHOO_EMAIL


# Send the email
try:
    connection.sendmail(from_addr=sender_email, 
                        to_addrs=receiver_email, 
                        msg=f"Subject: {subject}\n\n{body}"
    )
    print("Email sent successfully!")
except Exception as e:
    print("Error: Unable to send email.")
    print(e)

# Close the connection to the SMTP server
connection.close()
