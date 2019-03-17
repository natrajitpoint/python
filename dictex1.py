stu = {'id':101, 'name':'Divya', 'marks': 78}
print("Id : ", stu['id'])
print("Name : ", stu['name'])
print("Marks : ", stu['marks'])

#update and del
stu['gender'] = 'Female'
stu['name'] = 'Divya sree'

print(stu)

#Delete
del stu['marks']
print(stu)

del stu
print("Stu deleted")
print(stu)

