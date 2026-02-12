# 7. Relative Dates Printer
#
# Write a Python program to print yesterday, today, tomorrow.



from datetime import datetime,timedelta
today=datetime.today()
print(f"Today's Date is :-{today}")

const=timedelta(days=1)
tommorow=today+const
print(f"Tommorow's Date is :-{tommorow}")

yesterday=today-const
print(f"Yesterday's Date is :-{yesterday}")
