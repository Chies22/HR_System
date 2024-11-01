"""This class allows for instanciation of employee object"""
from Person import *
class Employee(Person):
    def __init__(self,name,ID_no,Address,age,Experience,department,role):
        super().__init__(name,age,ID_no,Address)
        self.name = name
        self.__Address = Address
        self.__ID_no = ID_no
        self.age = age
        self.Experience = Experience
        self.department = department
        self.role = role
        
    # methods
    def work(self,institution):
        print("I work in "+institution)
    def retire(self,age):
        print("I plan to retire when I am "+age+" old")
    def setId_no(self,number):
        self.__ID_no = number
    def setAddress(self,home_add):
        self.__Address = home_add
    def getId_no(self):
        return self.__ID_no
    def getAddress(self):
        return self.__Address
    def hobby(self,hobby):
        print("I like "+hobby)
    def hobby(self,*hobby2):
        print(*hobby2)
