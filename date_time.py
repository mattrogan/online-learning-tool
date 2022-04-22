from datetime import datetime

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

todays_date = f"{day}/{month}/{year}"
print(todays_date)