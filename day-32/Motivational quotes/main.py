import datetime
import smtplib
import random

username = "no.reply.testingpy@gmail.com"
pwd = "bqhkfbpivkvgjegm"
host = "smtp.gmail.com"
port = 587

# opening the quotes file
with open("quotes.txt") as quotes:
    # getting the contents
    content = quotes.readlines()
# randomly choosing a quote
chosen_quote = random.choice(content)

Today_date = datetime.datetime.now()
# if todays date is wednesday - which it is
if Today_date.weekday() == 2:
    # send a quote
    with smtplib.SMTP(host=host, port=port) as connection:
        connection.starttls()
        connection.login(username, pwd)
        connection.sendmail(
            from_addr=username,
            to_addrs=username,
            msg=f"Subject: Motivation Morning Quotes\n\n{chosen_quote}")
