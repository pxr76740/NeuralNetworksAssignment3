class Employee:
    Employee_count=0
    Total_Salary=0  #datamembers
    def __init__(self,name,family,salary,department):  #constructor
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department
        Employee.Employee_count+=1
        Employee.Total_Salary+=salary
    def avg_salary(self): #function for Average Salary
        average_salary=Employee.Total_Salary/Employee.Employee_count
        return average_salary
class Full_time_Emp(Employee):
    def __init__(self,name,family,salary,department,emp_type):
        self.emp_type=emp_type
emp1=Employee("Ammu","4",23000,"Dev")
emp2=Employee("Deepu","5",52000,"Prod")
emp3=Employee("Disha","6",16000,"Test")

print("Total number of employees are:",Employee.Employee_count)
print("Total given salary to employess",Employee.Total_Salary)
print("Average Salary is:", emp3.avg_salary())  #Average salary using instance