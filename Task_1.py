# 1. DateTime Formats Display
#
# Write a Python script to display the various Date Time formats -
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

from datetime import datetime

#a
curr_date_time=datetime.now()
print(f"Current Date and Time{curr_date_time}")

#b
curr_Year=datetime.today().strftime("%Y")
print(curr_Year)


#C
month_of_Year=datetime.today().strftime("%B")
print(month_of_Year)

#D
today=datetime.today()
week_Num_Year=today.strftime("%W")
print(week_Num_Year)

#E
print(today.strftime("%w"))

#f
print(today.strftime("%j"))

#g
print(today.strftime("%d"))

#h
print(today.strftime("%A"))