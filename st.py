class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nMarks={self.marks}")
        
        
    def result(self):
        if self.marks>=40:
            print(f"You are Passed")
        else:
            print("You are Failed!!")
    
    print()
s1=student("Basu",19,40)
s2=student("Aniruddha",18,41)
s3=student("Shreya",18,32)
s1.display_info()
s1.result()
s2.display_info()
s2.result()
s3.display_info()
s3.result()