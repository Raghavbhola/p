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

#First concept of OOP:classes and objects:->
#(1)----------->
class Employee:
    #Constructor to initialize the object
    employee_count=0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.employee_count += 1

    #Method to diploy employee details
    def display_info(self):
        print(f"Name:{self.name},Position:{self.position},salary:{self.salary}")

    def display_count():
        print(f"Total Employee:{Employee.employee_count}")


#class object attribute
e1=Employee("Alice","Developer",70000)
e2=Employee("Bob","Designer",65000)
e3=Employee("Charlie","Manager",80000)
e4=Employee("Diana","Intern",30000)
e5=Employee("Ethan","Analyst",60000)

print(e1.salary)  #Accessing attributes of objects e1

e1.display_info()
e2.display_info()
e3.display_info()
e4.display_info()
Employee.display_count()                 


#print(e1.salary)  #Accessing attributes of objects e1

e1.display_info()
e2.disploy_info()
e3.disploy_info()
Employee.display_count()                

print(type(e1))      #output:<class'_main_.Employe'

#(2)------------->
class Employee:
    #constructer to intialize the object
    Employee_count = 0
    def __init__(abc,name,position,salary,age,city,experience):
        abc.name=name
        abc.position=position
        abc.salary=salary
        abc.age=age
        abc.city=city
        abc.experience=experience
        Employee.Employee_count +=1

#Method to display employee details
    def display_info(abc):
        print(f"Name:{abc.name},position:{abc.position},salary:${abc.salary},Age:{abc.age},city:{abc.city},experience:{abc.experience}")

    def display_count():
        print(f"Total Exployee:{Employee.Employee_count}")
    
#class objects attribute
e1=Employee("Alice","Developer",70000,30,"New York",5)
e2=Employee("Bob","Designer",65000,28,"San francise",4)
e3=Employee("Charlie","Manager",80000,35,"Chicago",10)           
e4=Employee("Diana","Intern",30000,22,"Boston",1)
e5=Employee("Ethan","Analyst",60000,27,"seatle",3)

e1.display_info()
e2.display_info()
e3.display_info()
e4.display_info()
e5.display_info()     

# to get delete
delattr(e3,'position')


e1.salary =30  #Dynamically additing attribution to object e1
e2.position="Design"

del e1.position

print(type(e1))
print(e2)
print(e1)
print(type(e2))
print(e3)
print(e4)

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__base__)
print(Employee.__bases__)
print(Employee.__dict__)

Flag_check= hasattr(e1,'Salary')  #check if e1 has attribute'salary'
print(Flag_check)  #False
Flag_check= hasattr(e3,'position') #check if e3 has attribute'position'
print(Flag_check)  #True

setattr(e2,'salary',7000) #setattribute 'salary' of e2 to 7000
e2.display_info()
getattr(e3,'position')
delattr(e4,'position')
e5.display_count