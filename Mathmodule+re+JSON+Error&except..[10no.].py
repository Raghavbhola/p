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
print(x.count('o'))                                           #NOTE:  ^:->Gap, bs:->print full word
x=re.findall("[A-Z]",pg)  #find all alphabets
x=re.findall("[s-z]",pg)
x=re.findall("[^a-z,^,0-9,^,^-]",pg) #negation-find all except small alphabets
x=re.findall("[0-9]",pg)  #find all alphanumeric characters
x=re.sub("\s","7",pg,5)   #substitute function
x=re.sub("\s","7",pg)
x=re.search("ra",pg)  #will search

print(x)
