#empty list is created
squares = []

#fooloop with temp var is created and is assigned numbers that were 
#generated using range function 1 thru 10
for value in range(1, 11):

    # variable square is assigned temp var 'value' which is holding a  number from range
    # function, that number is being raised to power of 2     (aka  ^2)
    square = value **2

    #the empty squares list is called back to be given appened function which allows
    #the numbers inside var square to be inserted at the end of the list
    squares.append(square)

    #program will then run and loop untill all numbers from range have been created
    #and ran through

#list is then printed out to user
print(squares)






