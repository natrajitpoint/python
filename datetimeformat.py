import datetime
dt = datetime.datetime.now()
print("Now : ", dt)

print(dt.strftime("%d/%m/%Y %H:%M:%S"))
print(dt.strftime("%d-%B-%y %H:%M:%S"))
print(dt.strftime("%d-%b-%y %I:%M:%S %p"))

print(dt.strftime("%A"))
print(dt.strftime("%a"))
print(dt.strftime("%c"))
print(dt.strftime("%X"))
print(dt.strftime("%x"))

