'''
Author: Sreehari Sreekumar Nair
Date: 8 October 2024
Purpose: A program to familiarize time and date in various formats
'''

from datetime import datetime
current_time = datetime.now()

format1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(format1)

format2 = current_time.strftime("%m/%d/%Y")
print(format2)

format3 = current_time.strftime("%A,%B,%Y")
print(format3)

format4 = current_time.strftime("%A,%B,%Y %H:%M:%S %p")
print(format4)

format5 = current_time.strftime("%a-%b-%d %I:%M:%S IST %Y")
print(format5)

format6 = current_time.strftime("%a-%b-%d %I:%M:%S IST %Y")
print(format6)

format7 = current_time.isoformat()
print(format7)

format8 = current_time.strftime("%d")
print(format8)

format9 = current_time.strftime("%I:%M %p")
print(format9)

format10 = current_time.strftime("%B")
print(format10)

format11 = current_time.strftime("%Y")
print(format11)