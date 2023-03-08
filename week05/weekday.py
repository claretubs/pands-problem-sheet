# Program determines whether today is a weekday or weekend.
# Author: Clare Tubridy
# Date: 01/03/2023

import datetime

current_date = datetime.datetime.now()              # Determines current date
day = current_date.weekday()                        # Determines the day of the week

#Weekday is stored as a number, 0-6, 0 being Monday.
if day < 5:                                         # Monday to Friday
    print("Yes, unfortunately today is a weekday")
else:                                               # Saturday and Sunday
    print("It is the weekend, yay!")


