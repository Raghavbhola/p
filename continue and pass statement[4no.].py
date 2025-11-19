#Continue statement:->it will skips the current iteration.
#(1)
for letter in "PythonisaAmazinglanguagewhichisveryeasytolearnusegreatlyandalsoverypowerful":

    if letter=="A" or letter=="a":
        print("found on 'A' or 'a',skipping..")
        continue      #skips the current iteration
    print(letter,end="-")  #print all letters in a single line with space.
#output 
'''
P-y-t-h-o-n-i-s-found on 'A' or 'a',skipping..
found on 'A' or 'a',skipping..
m-found on 'A' or 'a',skipping..
z-i-n-g-l-found on 'A' or 'a',skipping..
n-g-u-found on 'A' or 'a',skipping..
g-e-w-h-i-c-h-i-s-v-e-r-y-e-found on 'A' or 'a',skipping..
s-y-t-o-l-e-found on 'A' or 'a',skipping..
r-n-u-s-e-g-r-e-found on 'A' or 'a',skipping..
t-l-y-found on 'A' or 'a',skipping..
n-d-found on 'A' or 'a',skipping..
l-s-o-v-e-r-y-p-o-w-e-r-f-u-l-   '''

#Pass Statement:->It is used to avoid getting errors when a statement is required syntactically but you don't want to do anything.
#(1)
for letter in "PythonIsAmazingLanguage":
    if letter=="g":
        pass      #does nothing,avoids error.
    print(letter,end="-")
#output
#P-y-t-h-o-n-I-s-A-m-a-z-i-n-g-L-a-n-g-u-a-g-e-
#(2)
for letter in "ABCDEFGHIJKLMNOP":
    if letter == "D" or letter == "M":
        pass #does nothing, avoids error
        print("This is pass block, doing nothing for 'D' or 'M'")
    print(letter)
#output
'''
A
B
C
This is pass block, doing nothing for 'D' or 'M'
D
E
F
G
H
I
J
K
L
This is pass block, doing nothing for 'D' or 'M'
M
N
O
P '''   
