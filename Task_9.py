# 49. String to Datetime Conversion
#
# Write a Python program to convert a string into datetime
#
from datetime import datetime, time
str_date="2026-02-12 12:00:00"
date_obj=datetime.strptime(str_date,"%Y-%m-%d %H:%M:%S")
print(date_obj)