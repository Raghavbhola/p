#--------------------------------------------{Math Module}-------------------------------------------------------------------
#*inbuilt math module and extensive mathematical functions (Math module)

x=min(5,10,15,2,15,0,-5,3)
y=max(5,10,25,2,15,0,-5,)
print(x)          #-5
print(y)          #25

z=(23354,34324,34234555,3332535,-32234)
print(max(z))     #34234555
print(min(z))     #-32234

#abs:-absolute(give +ve no.) [Even if it is -ve, it will still give +ve.]
#pow:-Power
a=abs(-100.25) #abs() Function returns the absolute (+ve) value of the specified number.
print(a)

b= pow(4,3) #pow()function returns the value of x to the power of x,y
print(b)          #64
c=pow(5964900,6)
print(c)
#-------------------------
import math as m #Alias
d=m.sqrt(15)     #math.sqrt()function returns the square root of (_)
print(d)
e=m.sqrt(29)
print(e)
#NOTE:-(1)Ceil:-Whatever value is given, it will give the [Nearest upper value] digit. But it will give an integer.
#      (2)floor:-[give Lowest no.]
#      (3)Round:-independent function [give nearest value]
#*Comb:->(n)Integar
#       *tell the no. of ways
#       *Probability

import math as m #Alias
d=m.ceil(4.2)   #math.ceil()function rounds a number UP to the nearest integar
print(d)   #5

e=m.floor(44.7) #math.floor()Func. rounds a no. DOWN to the nearest integar
print(e)   #44

r=round(58.1)   #round()Func. rounds a no. to the nearest integar
print(r)   #58

f=m.factorial(5)#math.Factorial returns the factorial of a no.
print(f)   #120

p=m.pi          #math.pi function returns the value of pi
print(p)   #3.14....

a=m.tau         #math.tau function returns the value of tau(2*pi)
print(a)   #6.28....

b=m.nan         #math.nan func. returns a floating point "Not a Number"[nan]value
print(b)   #nan

c=m.inf         #math.inf func. returns a floating point [+ve] Infinity Value
print(c)   #inf
#Comb--->
C=m.comb(8,3) #math.Comb(n,k) Func. returns the number of ways to choose K items from n item.
print(C)   #56 

#-----------------------------------{regular expressions}----------------------------------------------------
#(1)--->
import re
pg="Global warming is the hello F long-term1   increase 66 by Gloy hellooo error Error RROR is hellooooooo a ror of thor gror Shubham 3 in Ea$rth's average 5 Surface temperature, primarily Shiva caused by human activities that release greenhouse gases like carbon dioxide, methane, and nitrous oxide into the Globe a78tmosphere, Glowing which trap heat54 and intensify the natural green23house effect. Key drivers include the burning of fossil globe fuels for energy and transportation, deforestation, industrial processes, and certain agricultural practices. The consequences of this warming are far-reaching, with impacts ranging from rising sea levels and more frequent extreme weather events like heatwaves and floods to threats to ecosystems, ocean acidification, and significant economic disruptions. Addressing this crisis requires a global, concerted effort that includes transitioning to renewable energy, improving energy efficiency, protecting forests, and implementing policies to reduce emissions while also adapting to the changes already underway.The primary driver of global warming is the enhanced greenhouse effect, a natural process that is intensified by human activities. When humans burn fossil fuels such as coal, oil, and natural gas for power, transport, and industry, vast quantities of carbon dioxide are released into the atmosphere. Deforestation is another major contributor, as trees absorb from the atmosphere, and when they are cut or burned, this stored carbon is released, and the planet's ability to absorb future emissions is diminished. Other significant sources of greenhouse gases include agricultural activities, which release methane and nitrous oxide, and various industrial processes. These gases act like a blanket around the Earth, allowing sunlight in but trapping heat that would otherwise radiate back into space, causing the planet's average temperature to rise. Scientific evidence shows the Earth's average temperature has increased significantly since the pre-industrial era, with the rate of warming accelerating in recent decades.The impacts of this temperature increase are diverse and severe. One of the most visible effects is the melting of glaciers and polar ice caps, which contributes to a rise in sea levels, threatening coastal communities and low-lying island nations with inundation and increased storm surges. Changes in atmospheric and oceanic circulation patterns are leading to more frequent and intense extreme weather events, including hurricanes, heatwaves, droughts, and heavy rainfall. Ecosystems are also under immense pressure, with coral reefs experiencing bleaching due to warmer ocean temperatures and many species forced to migrate or face extinction as their habitats change."
x=re.findall("[a-d]",pg)
x=re.findall("/$",pg)
x=re.findall("/s",pg)
x=re.findall("\S",pg)
x=re.findall("...ror",pg)
x=re.findall("^ror",pg)      #(We'll catch up later)
x=re.findall("Gl.b..",pg)      #['Global', 'Globe ']
x=re.findall("planet$",pg)   #we'all catch up later
x=re.findall("hel.o*",pg)      #zero or more occurrences of preceding element
x=re.findall("hel.o+",pg)      #one or more occurrences of preceding element
x=re.findall("hel.o{5}",pg)    #exactly (5) occurrences of preceding element
x=re.findall("hel.o{0,5}",pg)  #between 0 and 5 occurrences of preceding element
print(x)

#-----(Set of sequences)------------>
x=re.findall("[au]",pg)   #find all vowels
print(x)
print(x.count('a'))  
print(x.count('u'))
print(x.count('i'))
print(x.count('e'))
print(x.count('o'))                                                                 #NOTE:  ^:->Gap, bs:->print full word
x=re.findall("[A-Z]",pg)  #find all alphabets
x=re.findall("[s-z]",pg)
x=re.findall("[^a-z,^,0-9,^,^-]",pg) #negation-find all except small alphabets
x=re.findall("[0-9]",pg)  #find all alphanumeric characters
x=re.sub("\s","7",pg,5)   #substitute function
x=re.sub("\s","7",pg)
x=re.search("ra",pg)  #will search

print(x)

st="Aakash Anand Ajay Bhanu Akash Amit Arjun" #by Raghav
x=re.search(r"\bB\w+",st)    #\b :- will search

print(x)
print(x.span())  #obj m se value ko access krwana   *Match object
print(x.group())
print(x.string)
#print(x(1)-x(0))

txt="The rain in spain mainly in the plain be the sain claim"
x=re.findall("[a-c]",txt)
print(x)

#---------------------------------------------------------------------------------------------------
#*JSON:-JavaScript Object Notation, used for data interchange
#          (Data storage and exchange)

#(2)------------------------------>
import json
x={
    "id":"unique-identifier",
    "firstname":"John",
    "dateofBirth":"1990-01-15",
    "email":"John.doe@example.com",
    "phone":"+1-2222-3455",
    "address":{
        "street":"123 Main st",
        "city":"springfield",
        "zipcode":"62701",
        "country":"USA"
        },
        "gender":"male",
        "nationality":"American"
}
y=json.dumps(x) #converts Python dictionary to json string
print(type(y))
print("-----------------------------------------")
print(json.dumps({"name":"John","age":30}))
print("-----------------------------------------")
print(json.dumps(["apple","bananas"]))
print("-----------------------------------------")
print(json.dumps(42))
print("-----------------------------------------")
print(json.dumps(31.76))
print("-----------------------------------------")
print(json.dumps(True))
print("-----------------------------------------")
print(json.dumps(False))
print("-----------------------------------------")
print(json.dumps(None))
print("-----------------------------------------")

#(3)------------------------------------------->
y=json.dumps(x,indent=4,separators=(" , ","="))   #Pretty print Json with custom seprators
print(y)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Error & Exceptions:-> error->Compile-time problem/issue
#                      exception->run-time problem/issue
#Exception handling:->It is managing runtime error during execution of program/code
#execution raised when error or unexcepted situation arise during the programming execution

#EVENT:-during runtime/execution of program which disrupts the normal flow of program.
#exception:-python script has raised the exception. it must either handle the exception immediately otherwise it terminates & quit.

#Handling an exception:->
#(1)Try,catch
#(2)Try,catch,throw,final
#(3)except:-Jo bhi line of code will get execute

#(4)else:-It will get executed when try-block executes without failure.
#(5)Finally:-It will get execute for sure
#(6)raise:-It use to raise an exception

#(1)--------------------->
try:
    print(a)
except:
    print("An error occured")    

#(2)--------------------->
try :
    print(545/90)
except NameError:
    print("A NameError exception occurred.")
except:
    print("An error occurred.")
else:
    print("No Error occurred")           

#(3)-------------------------->
try:
    print("Akash is  a good boy")
except NameError:
    print("A NameError exception occurred")
except ZeroDivisionError:
    print("A ZeroDivisionError exception occurred")
except:
    print("An unxcepted error occurred.")
else:
    print("No Error occurred.")            

#(4)--------------------------->
try:
    num=int(input("Enter a number"))
    result=10/num
    print(f"Result is {result}")
except NameError:
    print("Invalid input! Please enter a valid integar")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except:
    print("An unxcepted error occurred.")
else:
    for i in range (11):
        print(f"{result} * {i}={result*i}")
        #print("No Error occurred")        

#NOTE- Finally:->Whether the work is done or not, you leave anyway
#(5)------------------------------->
try:
    num=int(input("Enter a number"))
    result=1/num
    print(f"Result is {result}")
except ValueError:
    print("Invalid input! Please enter a valid integar")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except:
    print("An unxcepted error occurred.")
else:
    for i in range (10):
        print(f"{result} x {i}={result*i}")
        #print("No Error occurred")   
finally:
    print("Execution completed")

#(6)----------------------------->
#raise exception("This is a custom exception")
def divide (a,b):
    if b==0:
        raise Exception("Karan Defined Error: Division by zero is not allowed")
    return a/b

try:
    result=divide(10,2)
    print("Result:",result)
except:
    print("An error occurred.")
#except Exception as e:
#    print("An error occured.",e)    

#(7)----------------------------->
class KunalException(Exception):
    pass
def risky_function():
    raise KunalException("Something went wrong in risky_function")

try:
    risky_function()
except KunalException:
    print(f"Caught a custom exception: {KunalException}")    

#(8)------------------------------->
class KunalException(Exception):
    pass
def risky_function():
    raise KunalException("Something went wrong in risky_function")
print("risky_function executed successfully")

try:
    risky_function()
except KunalException as e:
    print(f"caught a custom exception:{e}")    

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Exception chaining:-> is a technique where one exception is caught and a new exception is thrown with the original exception attached as the cause.
try:
    open("Non_exixtent_file.txt","r")
except OSError:
    raise RuntimeError("A runtime error occurred due to an OS error")
#print("FileNotFoundError exception occurred")

#File handling:- Python program ke through kisi file ko read,writr,update ya delete karna.

#Logging in python:->Logging is a code mechanisum, to record a message, during the excusion of the programming langauge transection on the run time, is known as Logging in python.
#Use only 3 karan:->
#            (1)we are able to debugging
#            (2)oditing
#            (3)Monitering

#NOTE-log-level: Info,Debug,Error,Warning,Critical
#Components of logging:->logger,handler, formatter, logger level, filter.

#(1)-------------------->
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')      #NOTE-(asctime)- for current time
                                                                                            
def total_sum(a,b):
    logging.debug(f"Calculating the sum {a} and {b}")
    result= a+b
    logging.debug(f"Result of sum:{result}")
    return result

If_name_="_main_"
x=5
y=10
logging.info(f"Starting sum calculation for {x} and {y}")
sum_result=total_sum(x,y)
logging.info(f"The total sum is :{sum_result}")

#(2)------------------------>
import logging 
logger = logging.getLogger('my_logger')
logger.setLevel (logging.DEBUG)
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
console_handler=logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is an warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
logger.debug("Akash is dangerous")
logger.critical("Akash is very dangerous")


#Types of logging handle:-> They determine where and how the log-message are processed and outputted. They play an important role in directing logs,
#                           console,files,email,database,or even remote servers.
# (1)Filehandler
# (2)RotatingFileHandler
# (3)SyslogHandler
# (4)MemoryHandler
# (5)Http Hander
# (6)SMTP Handler
# (7)Stream Handler

#---------------------------XXX-------------------------------XXX------------------------------------XXX---------------------------------------------- 
#FILE operations in python:-> we can read, write and append to files using built-in functions.
#                *File handling is an important part of any web application.
#                *File handling is an important part of programming while working.
#                *file handling is an important part of programming while working with data like retrieving data from a file, working data to a file,
#                 and appending data to a file.

#Modes of file operations:->
# 'r':->Read mode which is used when the file is only being read.
# 'w':->Write mode which is used to edit and write new information to the file.
# 'a':->Append mode which is used to add new data to the end of the file; that is new information is automatically amended to the end.
# 'r+':->Special read and write mode, which is used to handle both actions when a file.
# 'x':->create mode which is used to create the specified file, returns an error if the file exists.