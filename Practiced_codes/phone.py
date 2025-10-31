#2. **Abstraction**:
#- Design a `Phone` class with methods to `call_contact` and `take_picture`. Abstract away any internal processing details and focus on creating a user-friendly interf
class phone:
    def __init__(self,contact,picture):
        self.contact=contact
        self.picture=picture
    def call(self):
        print
        