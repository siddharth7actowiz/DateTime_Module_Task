# 31. String Date to Timestamp
#
# Write a Python program to convert a string date to a timestamp.
#

from datetime import datetime, time
str_date="2026-02-12"
date_obj=datetime.strptime(str_date,"%Y-%m-%d")
print(date_obj.timestamp())