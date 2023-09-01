class Employee:
    empl = []

    def __init__(self, Ename, Eid, Edept, Esal):
        self.name = Ename        
        self.id = Eid        
        self.dept = Edept       
        self.salary = Esal

        Employee.empl.append(self)

    def display(self):
        for emp in Employee.empl: 
            print("Name = ", emp.name, "\nID= ", emp.id, "\nDept= ", emp.dept, "\nSalary= ", emp.salary, "\n")
    
    def updateSal(self, dept, sal):
        for emp in Employee.empl:
            if emp.dept == dept:
                emp.sal = sal


n = int (input("Enter no of employees: "))

print("Enter name, id, dept, sal of each employee:")
for i in range (n):
    Ename, Eid, Edept, Esal = input(), int(input()), input(), int(input())

    E = Employee(Ename, Eid, Edept, Esal)

E.display()

print("Enter dept and salary to update: ")
dept, sal = input(), int(input())

E.updateSal(dept, sal)

E.display()