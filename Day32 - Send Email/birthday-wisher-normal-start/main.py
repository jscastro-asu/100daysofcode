##################### Normal Starting Project ######################

import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "avocado@gmail.com"
my_pw = "guacamole435234"

now = dt.datetime.now()
today = (now.month, now.day)
df = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}
# tuple exist in dict
if today in birthdays_dict:
    bday_name = birthdays_dict[today]
    # pythonanywhere was used here for the path to be able to do set task just like cronjob
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
with open(file_path) as letter_file:
    contents = letter_file.read()
    # you have to assign it to a new variable when
    contents = contents.replace("[NAME]", bday_name["name"])
    print(contents)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, my_pw)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=bday_name["email"],
        msg=f"Subject:Happy Birthday {bday_name}!\n\n{contents}"
    )
connection.close()
