##################### Extra Hard Starting Project ######################
from ast import stmt
import datetime as dt
import random
import smtplib
import pandas

data = pandas.read_csv("birthdays.csv")
my_gmail = "no.reply.testingpy@gmail.com"
# app password
password = "bqhkfbpivkvgjegm"
# gmail default port num
port = 587
birthdays = {
    # itterating through the rows and getting the month and day
    (day["month"], day["day"]): day for (index, day) in data.iterrows()
}
# getting todays date
date = dt.datetime.now()
month = date.month
day = date.day
# turning it into a tuple
today = (month, day)
# # if todays date is in the birthday randomly pick from the letters and send it to the recipient
if today in birthdays:
    file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file) as letter_data:
        bday_person = birthdays[today]
        print(bday_person)
        content = letter_data.read()
        content = content.replace("[NAME]", bday_person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=port) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            connection.sendmail(from_addr=my_gmail,
                                to_addrs=bday_person.email, msg=f"Subject:Happy Birthday\n\n{content}")
