# Create a class Employee and then do the followinga.
# Create a data member to count the number of Employeesb.
# Create a constructor to initialize name, family, salary, department
#  Create a function to average salary.
# Create a Fulltime Employeeclass and it should inherit the properties of Employee classe.
# Create the instances of Fulltime Employeeclass and Employee class and call their member functions.
class Employee():
    'Common base class for all employees'
    empCount = 0
    SumSalary =0
    Avg =0

    def __init__(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = did
        Employee.empCount += 1
        Employee.SumSalary += self.salary

    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did)
# Create a Fulltime Employeeclass and it should inherit the properties of Employee classe
class FullTimeEmp(Employee):
    def __init__(self, eid, name, salary, did, exp):
        Employee.__init__(self, eid, name, salary, did)
        self.exp = exp
    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did, ",Experience:", self.exp)


"This would create first object of Employee class"
emp1 = Employee(1, "Pragathi", 2000, 10)
"This would create second object of Employee class"
emp2 = Employee(2, "Thammaneni", 4000, 20)
emp3=FullTimeEmp(3, "Reddy", 4000, 20, 6)
emp1.displayEmployee()
emp2.displayEmployee()
# Total employee and average salary
print("Total Employees %d" % Employee.empCount)
print("Average salary of the employees is", (Employee.SumSalary/Employee.empCount))
print(emp1.displayEmployee())
print(emp2.displayEmployee())
print(emp3.displayEmployee())
