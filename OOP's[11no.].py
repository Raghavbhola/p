# OOP's[Object Oriented Program]
# Defn:->To map with real world scenarios, we started using objects in code. This is called OOP's

#NOTE- OOP is a approach not a coding.
#      OOP's are aapproach of programming or We tie him up as an object.
#      OOP's a POL i.e.[Paradigm] it is approach/concept.
#POL:->Procedural Oriented program Paradigm (program describes procedure of performing certain task ny written a series of instruction in a logical order)

#*Class & Object:-> *class is a blue print for creating objects.
#                 Ex:->   #creating class
#                      Class student:
#                         name="Karan Kumar"
#*Object refers to a real-world entity with state and behavior.
# Attribute+Behavior:->single-unit millke banati hai class

#Principle of OOP's:->
#(1)class
#(2)object
#(3)Encapsulation
#(4)Inheritance
#(5)Polymorphism
#(6)Abstruction 

# _init_ :-> initialization (its parameter self hi hoga)
#constructor:-All classes have a function called _init_(), which is always executed when the object is being initiated.


class Employee:
    #Constructor to initialize the object
    employee_count=0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.employee_count += 1

    #Method to diploy employee details
    def disploy_info(self):
        print(f"Name:{self.name},Position:{self.position},salary:{self.salary}")

    def display_count():
        print(f"Total Employee:{Employee.employee_count}")

#class object attribute
e1=Employee("Alice","Developer",70000)
e2=Employee("Bob","Designer",65000)
e3=Employee("Charlie","Manager",80000)
e4=Employee("Diana","Intern",30000)
e5=Employee("Ethan","Analyst",60000)


#print(e1.salary)  #Accessing attributes of objects e1

e1.display_info()
e2.disploy_info()
e3.disploy_info()
Employee.display_count()                
        