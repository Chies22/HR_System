"""This class is inherited by employee for an employee is a person"""
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,ID_no,Address):
        self.name = name
        self.age = age
        self.__ID_no = ID_no
        self.__Address = Address
    
    # methods
    def work(self,institution):
        print("I work in "+institution)
    @abstractmethod
    def setId_no(self,number):
        pass
    @abstractmethod
    def setAddress(self,home_add):
        pass
    @abstractmethod
    def getId_no(self):
        pass
    @abstractmethod
    def getAddress(self):
        pass
    