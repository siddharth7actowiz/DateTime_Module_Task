# 37. Date Difference Breakdown
#
# Write a Python program to convert difference of two dates into days, hours, minutes, and seconds.
from datetime import datetime, date, timedelta

date_1=date(2026,2,12).timetuple()
date_2=date(2026,1,12).timetuple()
d1_day=date_1.tm_yday
d2_day=date_2.tm_yday
diff=d1_day-d2_day

diff_hours=diff*24
diff_mins=diff_hours*60
diff_secs=diff_mins*60



print(f"Difference between days:{diff}")
print(f"Difference between hours:{diff_hours}")
print(f"Difference between mins:{diff_mins}")
print(f"Difference between secs:{diff_secs}")

