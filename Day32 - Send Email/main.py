import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "fgbrgbgtb@gmail.com"
my_pw = "dfbsbgf#g45efbd"

if weekday == 4:
    with open("quotes.txt", "r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
       


with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=my_email, password=my_pw)
    conn.sendmail(
            from_addr=my_email, 
            to_addr="afgtgttrvvver@gmail.com", 
            msg=f"Subject: Today's motivation quote \n\n{quote}"
    )
conn.close()
        