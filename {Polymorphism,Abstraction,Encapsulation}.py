#Polymorphism:-> The ability of a function or method to take on many forms. it allows us to same mathod name for different types of objects.

#NOTE:->Its very easy to acheive polymorphism in Python because of its dynamic typing and duck typing features. We can use the same method name for different types of objects and it will work based on the type of object.
#        We can also achieve polymorphism by using inheritance and method overriding.

#1. Function Overriding - When a method in a child class has the same name as a method in the parent class, the method in the child class overrides the method in the parent
#2. Operator Overloading - When a operator is used with different types of objects, it behaves differently based on the type of object.
#3. Function Overloading - When a function is defined with the same name but different parameters, it is called function overloading. Python does not support function overloading, but we can achieve it by using default parameters or variable length arguments.
#4. Duck typing - When the type of an object is determined by its behavior rather than its class. It is based on the principle of "If it looks like a duck and quacks like a duck, then it is a duck". It allows us to use objects of different classes in the same way if they have the same behavior.

#(1)Duck Typing:->
(1)
class duck:
    def quack(self):
        return"Quack Quack"
    def fly (self):
        return"I am flying"

class AnotherBird:
    def quack(self):
        return"I am not a duck but I can quack like a duck"
    def fly(self):
        return"I am flying too"
    def makeSound(bird):
        print(bird.quack())
        print(bird.fly())

duck1 = duck()
bird1 = AnotherBird()
AnotherBird.makeSound(bird1)
AnotherBird.makeSound(duck1)

(2)
class Dog:
    def sound(self):
        return "Bark"
    def scratch(self):
        return"Fetching the ball"
class cat:
    def sound(self):
        return"Meow"
    def scratch(self):
        return"Scratching the furniture"
    def animal_sound(self):
        print(self.sound())
        print(self.scratch())

class Human:
    def sound(self):
        return"Hello"
    def scratch(self):
        return"Typing on the keyboard"
    def Human_method(self):
        print(self.sound())
        print(self.scratch())

c1 = cat()
d1 = Dog()
h1 = Human()
Human.Human_method(d1)
Human.Human_method(c1)
Human.Human_method(h1)

#Function/ Method Overloading:->In this class can have multiple methods with the same name but different parameters.Python doesnot support function overloading, but we can achieve it by default parameters or variable length arguments.

class Calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
c1 = Calculator()
#print(c1.add(2,3)) #This will give an error because the second add method will override the first add method.
print(c1.add(10,10,4)) #This will work because the second add method is defined with three parameters.

#This will give an error because the second add method will override the first add method. To achieve function overloading, we can use default parameters or variable length arguments.
    
class Calculator:
    def add(self,a,b,c=0,d=0):
        return a+b+c+d

c2 = Calculator()
print(c2.add(1,5))
print(c2.add(2,3,4))
print(c2.add(100000,30,4987,89874))
print(c2.add(2,3,4,5,6)) #This will give an error because the add method is defined with four parameters only. To achieve function overloading, we can use variable length arguments.

#2nd way to achieve the function overloading.
#-Need to install the package- pip install multiple dispatch
#from multiple dispatch import dispatch


#3. Operator Overloading - When a operator is used with different types of objects, it behaves differently based on the type of object. We can achieve operator overloading by defining special methods in the class. These special methods are called magic methods or dunder methods (double underscore methods). 
#                          For example, the __add__ method is used to overload the + operator, the __sub__ method is used to overload the - operator, the __mul__ method is used to overload the * operator, and so on.

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return point(self.x + other.x , self.y + other.y)
    def __str__(self):
        return"({},{})".format(self.x, self.y)

p1 = point(2,3) 
p2 = point(4,5)
print(p1)       #This will call the _str_ method to print thr point in the format(x,y).
print(p2)       #This will call the _str_ method to print thr point in the format(x,y).
p3 = p1 + p2
print(p3)       #This will call the _str_ method to print thr point in the format(x,y).  

#4. Method Overriding - When a method in a child class has the same name as a method in the parent class, the method in the child class overrides the method in the parent class. We can achieve method overriding by defining a method with the same name in the child class.
#(1)------------------->
class Parent:
    def greet(self):
        return"Hello From Parent"
    def greet1(self):
        return"Good Morning from Parent"
    def greet2(self):
        return"Good night from parent"

class child(Parent):
    def greet(self):
        return"Hello from child"
    def greet1(self):
        return"Good morning from child"
    def greet2(self):
        return"Good night child"

c1 = child()
c2 = Parent()
print(c1.greet())
print(c1.greet1())
print(c1.greet2())
print(c2.greet())     
print(c2.greet1())
print(c2.greet2())      

#(2)------------------>
class Employee:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def employee_info(self):
        return"Name:{}, age:{}".format(self.name,self.age)
    def employee_salary(self,salary):
        return"salary:{}".format(salary)

class Manager(Employee):
    def manager_info(self):
        return"Manager Name:{}, Manager Age:{}".format(self.name, self.age)
    def manager_salary(self, salary):
        return"Manager Salary:{}".format(salary)

e1 = Employee("Akash", 25)
m1 = Manager("Yashika", 30)
print(e1.employee_info())
print(e1.employee_salary(50000))
print(m1.manager_info())
print(m1.manager_salary(100000))

#(3)---------------->
class Employee:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def getname(self):
        return self.name
    def getage(self):
        return self.age

class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    def getdepartment(self):
        return self.department

e1 = Employee("Akash", 25)
m1 = Manager("Yashika", 30, "HR")
print(e1.getname())
print(e1.getage())
print(m1.getname())
print(m1.getage())
print(m1.getdepartment())

# Dynamic binding=> The method to be called is determined at runtime based on the object type. It is the process of linking a procedure call to the code to be executed in response to the call. 
#                   It is also known as late binding or runtime binding. It allows us to achieve polymorphism in Python because we can use the same method name for different types of objects and it will work based on the type of object. 
#                   It is used to achieve polymorphism in Python because we can use the same method name for different types of objects and it will work based on the type of object.

# Dynamic typing => The type of an object is determined at runtime based on the value assigned to it.

# Dynamic vs static typing ==> Dynamic typing allows us to change the type of an object at runtime, while static typing does not allow us to change the type of an object at runtime. Python is a dynamically typed language, which means that we can change the type of an object at runtime.

