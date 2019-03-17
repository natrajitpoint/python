class employee:
    def setdata(self,eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def getdata(self):
        print("\n*** Employee Info ***\nEmployee Id : {}\n\
Employee Name : {}\nEmployee Salary : {}"\
              .format(self.eno,self.ename,self.esal))

#main
e1 = employee()
e2 = employee()

e1.setdata(1001, 'Srinivas',35000)

x = int(input("Enter employee Id : "))
y = input("Enter employee name : ")
z = float(input("Enter employee salary : "))
e2.setdata(x,y,z)

e1.getdata()
e2.getdata()

e3 = employee()
e3.getdata()#error

