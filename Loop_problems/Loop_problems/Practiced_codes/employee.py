
class Employe:
    def __init__(self,name,salary=30000):
        self.name=name
        self.salary=salary
        
    def show(self):
        print(F"The name of the Employee is {self.name}\nSalary of the Employee {self.salary}")
        print()

e1=Employe("Basu",100000)
e2=Employe("Aniruddha",12)
e3=Employe("Shreya",200000)

e1.show()
e2.show()
e3.show()
