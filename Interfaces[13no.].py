#Interfaces - A class can implement multiple interfaces, which are defined as abstract base classes. An interface is a contract that specifies the methods that a class must implement.
#             In Python, we can use the abc module to define abstract base classes and interfaces.

# the only difference between an abstract class and an interface is that an abstract class can have both abstract and concrete methods, while an interface can only have abstract methods.
#  In Python, we can use the abc module to define both abstract classes and interfaces.

#2 types of interfaces in python
# 1. Formal Interface - A formal interface is defined using the abc module, and it is enforced by the language. 
#                       A class that implements a formal interface must implement all the methods defined in the interface. For example, we can define a formal interface for a class that represents a shape:
# 2. Informal Interface - An informal interface is a convention that specifies the methods that a class should implement. 
#                         It is not enforced by the language, and there is no way to check if a class implements an informal interface. For example, we can define an informal interface for a class that represents a shape:

#formal Interface:-->
from abc import ABC , abstractmethod #abstruct base class
import abc
class Interface1(ABC):
    @abstractmethod
    def method1 (self):
        pass
    @abstractmethod
    def method2 (self):
        pass
class Interface2(ABC):
    @abstractmethod
    def method2 (self):
        pass

class kunalClass(Interface1,Interface2):
    def method1(self):
        #pass
        print("Implementation of method1")
    def method2(self):
        print("Implementation of method2")
    def method3(self):
        print("Implementation of method3")    

obj = kunalClass()
#obj1 = Interface1()  #This will give an error becoz we cannot instantiate an abstruct class
obj.method1()
obj.method2()   
obj.method3()          
       
