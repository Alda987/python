'''
Author: ALDA TREESA JOSY 
Date:19/10/2024
Description:Familiarize time and date in various formats (Eg. “Thu Jul 11 10:26:23 IST 2024”).

Display current date and time
Display the format  [YYYY-MM-DD HH:MM:SS]
Display the format  [MM/DD/YYYY]
Display the format  [Day, Month DD, YYYY]
Display the format  [Day, Month DD, YYYY HH:MM:SS AM/PM]
Format the date and time like "Thu-Jul-11 10:26:23 IST 2024"
Display [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]  Eg: Wed-Oct-02 12:41:18 IST 2024
Display format- 8 [ISO format:]
Display Date only
Display Time only
Display month only
Display Year only
'''
from datetime import datetime

current_time = datetime.now()

print("Current date and time:", current_time)

format_1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Format 1 [YYYY-MM-DD HH:MM:SS]:", format_1)

format_2 = current_time.strftime("%m/%d/%Y")
print("Format 2 [MM/DD/YYYY]:", format_2)

format_3 = current_time.strftime("%A, %B %d, %Y")
print("Format 3 [Day, Month DD, YYYY]:", format_3)

format_4 = current_time.strftime("%A, %B %d, %Y %I:%M:%S %p")
print("Format 4 [Day, Month DD, YYYY HH:MM:SS AM/PM]:", format_4)

format_5 = current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")
print("Format 5 [Abbr Weekday-Abbr month-DD HH:MM:SS IST YYYY]:", format_5)

format_6 = current_time.isoformat()
print("Format 6 [ISO format]:", format_6)

date_only = current_time.strftime("%Y-%m-%d")
print("Date only:", date_only)

time_only = current_time.strftime("%H:%M:%S")
print("Time only:", time_only)

month_only = current_time.strftime("%B")
print("Month only:", month_only)

year_only = current_time.strftime("%Y")
print("Year only:", year_only)
