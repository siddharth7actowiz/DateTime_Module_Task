# 13. Week Number Finder
#
# Write a Python program to get the week number.
#
# Sample Date : 2015, 6, 16
# Expected Output : 25

from datetime import datetime,date
sample_date=date(2025,6,16)
print(sample_date.isocalendar().week)