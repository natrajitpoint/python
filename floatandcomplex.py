#area of circle
radius = float(input("Enter Circle Radius : "))
print("Type of radius is : ", type(radius))

area = 3.142 * (radius ** 2)
print("Area of circle is %f" %area)

#convert to complex
x = float(input("Enter Real part : "))
y = float(input("Enter imaginary part : "))

c = complex(x,y)
print("type of c is : ", type(c))
print("c = ", c)

#any type to string conversion
s1 = 10
s2 = 20
print(type(s1), type(s2))
#print(s1 + "\t" + s2)

#s1 = str(s1)
#s2 = str(s2)
#print(type(s1))
#print(type(s2))
print(str(s1) + "\t" + str(s2))



