"""Main class where we have instanciated the objects on employee and departments"""
from Department import *
from Employee import *
class Main:
 
    print("Department 1\n")
   
    Marketing = Department("Marketing"," Marketing and advertising")
    print("Department:")
    print(Marketing.name)
    print("Our role:")
    print(Marketing.role)
    print("Employee training is on date:")
    Marketing.conduct_training(15)
    print("We have recruited:")
    Marketing.recruit(300)
    print("persons.")
    Marketing.keep_employee_record()
       
    print("\nJust information concering the employees\n")
    
    worker01 = Employee("Brian",31,23782,"Nanyuki",7,"Marketing","Recording sales")
    worker01.name = "Brian"
    print("My name is: ")
    print(worker01.name)
    worker01.age=31
    print("I am aged:")
    print(worker01.age)
    worker01.setId_no(23782)
    print("ID number:")
    print(worker01.getId_no())
    worker01.setAddress("Nakuru")
    print("I live in:")
    print(worker01.getAddress())
    worker01.department = "Marketing"
    print("Department:")
    print(worker01.department)
    worker01.Experience = 7
    print("I am in this work for:")
    print(worker01.Experience)
    print("years")
    worker01.role = "Recording sales"
    print("I am tasked with:")
    print(worker01.role)
    print("During my free time I:")
    worker01.hobby("reade books","do sports","go for shooting")
    
    print("\nDepartment 2\n")
    Eng = Department("Engineering"," Build planes")
    print("Employee training is on date:")
    Eng.conduct_training(24)
    print("We have recruited:")
    Eng.recruit(30)
    print("persons.")
    Eng.keep_employee_record()
    
    print("\nAnother employee record\n")
    
    worker02 = Employee("Jeff",27,20082,"Nairobi",4,"Marketing","Web maintainer")
    worker02.name = "Jeff"
    print("My name is: ")
    print(worker02.name)
    worker02.age=27
    print("I am aged:")
    print(worker02.age)
    worker02.setId_no(20082)
    print("ID number:")
    print(worker02.getId_no())
    worker02.setAddress("Nairobi")
    print("I live in:")
    print(worker02.getAddress())
    worker02.department = "Engineering"
    print("Department:")
    print(worker02.department)
    worker02.Experience = 4
    print("I am in this work for:")
    print(worker02.Experience)
    print("years")
    worker02.role = "fying planes"
    print("I am tasked with:")
    print(worker02.role)
    print("During my free time I:")
    worker02.hobby("Dance","do ports","swim")

