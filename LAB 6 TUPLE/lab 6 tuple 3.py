from datetime import date

date1 = (15, 2, 2024)  # 15th Feb 2024
date2 = (8, 3, 2025)  # 8th Mar 2025

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

days_difference = abs((d2 - d1).days)

print("Number of days between the two dates:", days_difference)
