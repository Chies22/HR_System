"""Department as an object with the 2 attributes and three methods"""
class Department:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    
    #methods
    def conduct_training(self,date):
        print(date)    
    def recruit(self,number):
        print(number)    
    def keep_employee_record(self):
        print("We have records of our employees for as long as they are working for us")

