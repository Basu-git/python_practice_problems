class movie:
    def __init__(self,name="NOT FOUND",rating="ERROR"):
        self.name=name
        self.rating=rating
        
    def display(self):
        print(f"The movie name is {self.name} and the rating is {self.rating}")
c=movie("Kantara",4.5)
d=movie()
c.display()
d.display()