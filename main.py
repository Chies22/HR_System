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
    
    #another object of the Employee class
    print("\nAnother employee record\n")
    worker03 = Employee("name",00,0000,"address",0,"department","tasks")
    worker03.name = input("Enter you name")
    print("My name is: ")
    print(worker03.name)
    worker03.age= int(input("Enter your age"))
    print("I am aged:")
    print(worker03.age)
    worker03.setId_no(2025)
    print("ID number:")
    print(worker02.getId_no())
    worker03.setAddress("Lodwar")
    print("I live in:")
    print(worker03.getAddress())
    worker03.department = input("Enter the Department you work in ")
    print("Department:")
    print(worker03.department)
    worker03.Experience = int(input("Enter your years of experience"))
    print("I am in this work for:")
    print(worker03.Experience)
    print("years")
    worker03.role = input("Enter the tasks you do as a routine")
    print("I am tasked with:")
    print(worker03.role)
    print("During my free time I:")
    worker03.hobby("Dance","do ports","swim")