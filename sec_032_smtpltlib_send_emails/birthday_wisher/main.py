import random
import smtplib
import datetime as dt
import pandas as pd


# CONSTANTS IN THIS CODE NEED TO BE CHANGE ACCORDING TO YOUR SPECIFITACIONS


GMAIL_EMAIL = "random_test@gmail.com"
GMAIL_PASSWORD = "generated_password"         # this password is genreated after enabling 2 steps verification -> generate app password for gmail account
SMTP_SERVER = 'smtp.gmail.com' 


RECIEVER_EMAIL = 'random_test@yahoo.com'


# ------------------------------------------------------------------------------------------------ #

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today = (today_month, today_day)

data = pd.read_csv(r"sec_032_smtpltlib_send_emails\birthday_wisher\birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:

    with open(f"sec_032_smtpltlib_send_emails\\birthday_wisher\\letter_templates\\letter_{random.randint(1,3)}.txt") as file:
        birthday_list_template = file.read()
        birthday_list = birthday_list_template.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(GMAIL_EMAIL, GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_EMAIL,
            to_addrs=RECIEVER_EMAIL,
            msg=f"Subject: Happy Birthday\n\n{birthday_list}"                   
        )


