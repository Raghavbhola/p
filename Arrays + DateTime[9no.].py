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

#(3)----------------------------------Accessing array elements----------------------------------------------
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

#------------------------------------------Modifying Array elements------------------------------------
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
