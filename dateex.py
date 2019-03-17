import datetime
d = datetime.date(1947, 8, 15)
print("Given Date : ", d)
print("Day : ", d.day)
print("Month : ", d.month)
print("Year : ", d.year)
print("Today Date : ", datetime.date.today())

print(d.strftime("%d-%b-%Y"))

