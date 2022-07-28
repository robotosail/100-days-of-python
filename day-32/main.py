import smtplib

my_gmail = "no.reply.testingpy@gmail.com"
# app password
password = "bqhkfbpivkvgjegm"
# gmail default port num
port = 587

subject = """
This link takes you to goat.com in which you will be able to see what the jordans look like. I am a size 10. You have to create an account in order to confim the purchase.
https://www.goat.com/sneakers/air-jordan-12-retro-playoff-2022-ct8013-006
if you need any help at all please be sure to call me. 
Thank you in advance.

Update:
    in order to return you need to download the goat app. There are not cost to return. If you initiate a return, it must be within 3 days of getting the item.
"""

with smtplib.SMTP("smtp.gmail.com", port=port) as connection:
    # creating a secure connection
    connection.starttls()
    # logining in
    connection.login(my_gmail, password)
    connection.sendmail(from_addr=my_gmail,
                        to_addrs="dealsexcellente@gmail.com", msg=f"Subject: The link to buy the jordans\n{subject}")

#     # use with keyword instead of this - connection.close()

# import datetime as dt

# # getting the current date
# now = dt.datetime.now()
# # getting the current year
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2007, month=2, day=11)
