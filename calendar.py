import calendar

calObj1 = calendar.TextCalendar(calendar.SUNDAY)
TextCal = calObj1.formatmonth(1996,1)
print(TextCal)

#calObj.formatyear(year, w=2, l=1, c=6,m=3)
#width between two columns
#blank line between two rows
#space between two months(column wise)
#no of months in a row
calObj3 = calendar.TextCalendar(calendar.SUNDAY)
TextCal2 = calObj3.formatyear(1996,1,2)
print(TextCal2)

#calObj2 = calendar.HTMLCalendar(calendar.SUNDAY)
#HtmlCal = calObj2.formatmonth(2018, 8)
#print(HtmlCal)


