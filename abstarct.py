class Employee:
    """ This is abstract class with common properties """
    def __init__(self, name, job):
        self.name = name
        self.job = job
        
    def details(self):
        print("***** Employee Details *****")
        print("Employee Name : {0}\nDesignation : {1}"\
              .format(self.name, self.job))
        
    # abstract methods
    def salary(self):
        pass
        #raise Exception("NotImplemented method")
    
class Company(Employee):
    __sal=0
    def salary(self):
        if self.job.lower()=='manager':
            __sal=25000
            
        if self.job.lower()=='project leader':
            __sal=22000
            
        if self.job.lower()=='developer':
           __sal=18000
            
        if self.job.lower()=='clerk':
            __sal=15000

        print("Salary : Rs.",__sal)
        print("HRA : {0}\nDA : {1}\nPF : {2}\n"\
.format((__sal*30/100), (__sal*20/100), (__sal*12/100)))

#Main       
emp1 = Company('Ravi', 'Manager')
emp1.details()
emp1.salary()

emp2 = Company('Divya', 'Developer')
emp2.details()
emp2.salary()

x =Employee('natraj','clerk')
x.details()





































