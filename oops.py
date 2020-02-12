#creating employee class
class Employee:
    print('Common base class for all employees')
    empCount = 0
    #creating constructor
    def __init__(self, name, salary, age, bloodgroup):
        self.name = name
        self.salary = salary
        self.age = age
        self.bloodgroup = bloodgroup
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
  
    def displayEmployee(self):
        print("name :", self.name,"Salary:", self.salary,"age:",
                self.age,"bloodgroup:", self.bloodgroup)
#displaying information
print("This would create first object of Employ class")
emp1 = Employee("Zara", 2000, 30, "A+")
print("This would create second object of Employ class")
emp2 = Employee("Manni", 5000, 33, "B-")
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
