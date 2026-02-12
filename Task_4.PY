#19. Last Tuesday Finder
# Write a Python program to get the date of the last Tuesday.
from datetime import datetime, timedelta

today=datetime.today()
diff=(today.weekday()-1)%7
last_tuesday=today-timedelta(days=diff)
print(last_tuesday.strftime("%D"))