#Continue statement:->it will skips the current iteration.
#(1)
for letter in "PythonisaAmazinglanguagewhichisveryeasytolearnusegreatlyandalsoverypowerful":

    if letter=="A" or letter=="a":
        print("found on 'A' or 'a',skipping..")
        continue      #skips the current iteration
    print(letter,end="-")  #print all letters in a single line with space.