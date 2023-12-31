###################BASIC EMAILING GUIDE######################################################################################

#
# import smtplib
#
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body.")

#####################BASIC DATETIME GUIDE#####################################################################################

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
#
# birthday = dt.datetime(year=2020, month=10, day=21, hour=4, minute=21, second=3, microsecond=2)
# print(birthday)

####################MOTIVATIONAL MONDAY QUOTES CHALLENGE#######################################################################

# import smtplib
# import datetime as dt
# import random
#
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 0:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         random_quote = random.choice(all_quotes)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(my_email, password)
#         connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivation\n\n{random_quote}")

##################AUTOMATIC BIRTHDAY WISHER####################################################################################

import smtplib
import datetime as dt
import pandas
import random

my_email = "appbreweryinfo@gmail.com"
password = "abcd1234()"

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n"
                                                                                       f"{contents}")

