#   Programming language have internally-support in Arrays, language like=Java,JS,C++..etc
#   But in Python have not any internal support in Array.

# Arrays:->A dataset that accepts homogeneous data
#         *Sequential data type
#         also called *container
#       Ex:- int arr[10]={10,5,7,9,11,73......20}
#             arr=mo.array(typeCode[initial])
#     *Indexing starts from zero.                                   *Deprication:- will discontinue

# Operations using in Arrays:---->
#    (1)Traverse:-access the node/Accessing any array
#    (2)Insertion:-Adds an element at given index
#    (3)Deletion:-delete an element
#    (4)Search:-search an element[search by index & value]
#    (5)Update:-update an element at given index[Modify]

#(1)---------------------->
import array as ModArr

ar =ModArr.array('i', [1,2,3,4,5])
print(ar)         #array('i', [1, 2, 3, 4, 5])
ar.append(6)  #Adds an element at the end
print(ar)         #array('i', [1, 2, 3, 4, 5, 6])
#(2)----------------------->
import array as ModArr

arr=ModArr.array('d',[1,2,3,4,5])  #Array of integer
print(arr, type(arr))              #array('d', [1.0, 2.0, 3.0, 4.0, 5.0]) <class 'array.array'>

arr1=ModArr.array('f',[1.5,2.5,3.5,4.5])
print(arr1, type(arr1))            #array('f', [1.5, 2.5, 3.5, 4.5]) <class 'array.array'>

arr2=ModArr.array('u',['a','b','c','d'])     #** u:- will Deprecation warning.
print(arr2, type(arr2))            #array('u', 'abcd') <class 'array.array'>

a, b, c, d = 10, 20, 30, 40
arr2 = ModArr.array('i', [a, b, c, d])
print(arr2, type(arr2))             #array('i', [10, 20, 30, 40]) <class 'array.array'>

#(3)------------------------------------------{Accessing array elements}--------------------------------------------------------------
arr=ModArr.array('d',[1,2,3,4,5])  #Array of integer
print(arr, type(arr)) 
print(arr[0])         #1.0
print(arr[3])         #4.0

arr1=ModArr.array('f',[1.5,2.5,3.5,4.5])
print(arr1, type(arr1)) 
print(arr1[2])       #3.5
print(arr1[3])       #4.5
print(arr1[-3])      #2.5
#(4)----------------------------->
arr=ModArr.array('d',[1,2,3,4,5]) 
for i in arr:
    print(i,end=' , ')
    print(i,end=' , ')

for i in range (len(arr)):
    print(i,"-->",arr[i])

for loc,val in enumerate(arr):
    print(f"Index:-{loc}:,value:-{val}")
    print(f"{loc},value:-{val}")

print(arr[2:7])   #slicing array from index 2 to 6
print(arr[2:])    #slicing array from start to index 3
print(arr[:5])    #slicing array from start to index 4
print(arr[:])     #slicing the entire array

#-----------------------------------------------{Modifying Array elements}--------------------------------------------------
#(1)Adding elements:->
arr=ModArr.array('d',[1,2,3,4,5])  #Array of integer
arr.append(110)     #Appending elements at the end
print(arr)   #array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 110.0])

arr.extend([120,130,140])   #Extending array with Multiple elements
print(arr)   #array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 110.0, 120.0, 130.0, 140.0])

arr.insert(2,225)   #Inserting element at index 2 
print(arr)   #array('d', [1.0, 2.0, 225.0, 3.0, 4.0, 5.0, 110.0, 120.0, 130.0, 140.0])

arr.insert(-2,9999)
print(arr)   #array('d', [1.0, 2.0, 225.0, 3.0, 4.0, 5.0, 110.0, 120.0, 9999.0, 130.0, 140.0])

#(2)Replacing elements
arr=ModArr.array('d',[1,2,3,4,5])  #Array of integer
#arr.remove(50)   #Remove First occurrence of element with value 50
#print(arr)

arr.remove(4)  #Removing element at index 4
print(arr)   #array('d', [1.0, 2.0, 3.0, 5.0])

arr.pop()      #Removing last element
print(arr)   #array('d', [1.0, 2.0, 3.0])

del arr[2]     #Deleting element at index 2
print(arr)   #array('d', [1.0, 2.0])

#del arr()      #Deleting the entire Array   
#print(arr)   #This will raise a name error since arr is deleted

i=0

while i < len(arr):
        print(arr[i])
        i+=1

#(3)---------------------->
import array as ModArr
import copy as cp
arr=ModArr.array('i',[10,20,30,40,50,50,60,70,80,90,100])
ac=arr
print("Original array:",arr)  #Original array: array('i', [10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100])
print("Copied array:",ac)     #Copied array: array('i', [10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100])
print(id(arr),id(ac))

ac[5]=999
print(arr)  #array('i', [10, 20, 30, 40, 50, 999, 60, 70, 80, 90, 100])
print(ac)   #array('i', [10, 20, 30, 40, 50, 999, 60, 70, 80, 90, 100])
#(4)-------------------------->
import array as ModArr
import copy as cp
arr=ModArr.array('i',[10,20,30,40,50,60,70,80,90,100])
ac= cp.deepcopy(arr)
print("Original array:",arr)
print("Copied array:",ac)
print(id(arr),id(ac))
ac[-5]=999
print("After modification:-")
print("Original array:",arr)
print("Copied array:",ac)      #Copied array: array('i', [10, 20, 30, 40, 50, 999, 70, 80, 90, 100]) 

Arrlist= arr.tolist()
Arrlist.sort()
S_arr= ModArr.array('i',Arrlist)
sorted_list=sorted(arr)
print("original array:", arr, type(arr))
print("sorted array:", arr,S_arr,type,(S_arr))

a=cp.copy(arr)
a[0]=200
#a.sort()
print(id(a),id(arr))

#---------------------------------------------------(Reversing Array)-----------------------------------------------------------------
#(1)Slicing:->
import array as ModArr
import copy as cp
arr=ModArr.array('i',[10,20,30,40,50,60,70,80,90,100])
rev_arr= arr[: :-1]
print("Reversed array using slicing:",rev_arr)  #Reversed array using slicing: array('i', [100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
print("original array remains unchanged:",arr)

#(2)Using reverse() method:->
arr_list=arr.tolist()
arr_list.reverse()
ra=ModArr.array('i',arr_list)
print("Reversed array using reverse() method:",ra)
print("Original array after reverse() method:",arr)

#(3)Using a loop:->
#Array
import array as ModArr
import copy as cp
arr=ModArr.array('i',[10,20,30,40,50,60,70,80,90,100])
rev_arr=ModArr.array('i',[])
for i in range(len(arr) -1,-1,-1):
    rev_arr.append(arr[i])
    print("Appending:",arr[i])

print("Reversed array using slicing:",rev_arr)  
print("original array remains unchanged:",arr)

#-----------------------------------------------(Joining Arrays)-------------------------------------------------------------
#(1) Using + operator
import array as ModArr
import copy as cp
arr=ModArr.array('i',[10,20,30,40,50,60,70,80,90,100])
arr3=ModArr.array('i',[200,300,400,500,600])
arr4=arr+arr3   
print("Joined array using +operators:",arr4)

#(2)Using append() in a loop:->
for i in arr3:
    arr.append(i)

print("Joining array using append() in a loop",arr) 

#(3)Using extend() method:-> easy way
arr.extend(arr3)
print("Joined array using extend() method:",arr)

#(1)----------------------->
import array as ModArr
arr=ModArr.array('i',[140,23,42,12,42,5,16,71,66,53])
a=arr.buffer_info()
print(a[0],[1])   #prints:address of the array and number of elements in the arrays.

#(2)----------------------->
import array as ModArr
arr=ModArr.array('i',[140,23,42,12,42,5,16,71,66,53])
arr1=ModArr.array('f',[1.2,2.5,3.5,4.5,7.4])
#(1)bufer_info() method:-
a=arr.buffer_info()
b=arr1.buffer_info()
print(a[0],[1])
print(b[0],[1])
#(2)count() method:-
print(arr.count(16))  #Counts this occurrences of 16 in the array.
print(arr.count(400))
#(3)index() method:-
x=arr.index(71)  #find the index of first occurrence of 71
print(x)   #7
arr.reverse()
print(arr)
#----------------------------------{Array se list banani hai}-----------------------------------------------
import array as ModArr
arr=ModArr.array('i',[140,23,42,12,42,5,16,71,66,53])
list1=[1,2,3,4,5,6]
arr.fromlist (list1)
print(arr)      #array('i', [140, 23, 42, 12, 42, 5, 16, 71, 66, 53, 1, 2, 3, 4, 5, 6])


#----------------------------------------------------------------------------------------------------------------------------
#***DATETIME:-->Python doesn't allow internally
import datetime
n=datetime.datetime.now()
print("Current date and time:",n)
print("Current year:",n.year)         #current year
print("Current month:",n.month)       #current month
print("Current day:",n.day)           #current day
print("Current hour:",n.hour)         #current hour
print("Current minute:",n.minute)     #current minute
print("Current second:",n.second)     #current second

#**strf:->that's function.
print(n.strftime("%D"))                      #D->Date
print(n.strftime("%d"))                      #d->day in numbers
print(n.strftime("%Y-%m-%d  %H:%M:%S"))      #Y:-year,m:-month,d:-date, H:-hour in 24,M:-Min., S:-sec.
print(n.strftime("%W"))                      #W:-Which Saturday of the year is it?
print(n.strftime("%I:%M:%p"))                #I:- 12 hr. format ,p:-PM/AM
print(n.strftime("%B, %d, %Y"))              #B:-Nov
print(n.strftime("%A,%B,%Y"))                #A:-Week day
print(n.strftime("%X"))                    #X:-Time in 24 hr. format

X=datetime.datetime(2005,7,8)
print(X.strftime("%A,%B,%d,%Y"))    #Friday,July,08,2005
print(X.strftime("%H:%M:%S"))

s=datetime.datetime(2012,8,9)
print(s.strftime("%A,%B,%d,%Y"))    #Thursday,August,09,2012

S=datetime.datetime(1978,12,20)
print(S.strftime("%A,%B,%d,%Y"))

print(n.strftime("%C"))             #Century (year divided by 100, truncated to an integer)
print(n.strftime("%c"))             #Day of the year
print(n.strftime("%x"))             #date
print(n.strftime("%X"))             #time
print(n.strftime("%V"))             #ISO week number of the year.
print(n.strftime("%f"))             #Microsecond as a zero-padded decimal
print(n.strftime("%Z"))             #Time zone name
