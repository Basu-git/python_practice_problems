class rectangle:
    def __init__(self,len,breadth):
        self.len=len
        self.breadth=breadth
    
    def perimeter(self):
        p=2*(self.len+self.breadth)
        print(f'The Perimeter of Rectangle is {p}m')
    
    def area(self):
        a=self.len*self.breadth
        print(f"The Area of the Rectangle is {a} sqmeter")

a=rectangle(2,3)
a.perimeter()
a.area()
