import smtplib

my_email = "testingmailwithpy@gmail.com"
my_pw = "xxxxxxxx!"

with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=my_email, pw=my_pw)
    conn.send_message(
            from_addr=my_email, 
            to_addr="myrecptn@gmail.com", 
            msg="Subject:Hello\n\nSending this from my python program."
    )
conn.close()
