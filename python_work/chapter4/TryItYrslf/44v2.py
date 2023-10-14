# PROBLEM - make list of nums from 1 to 1 million, use for loop to print nums

#genNums = list(range(1, 1000000))
#print(genNums)


#genNums = []
#for number in range(1, 1000001):
#    storedNum = number 
#    genNums.append(storedNum)
#print(genNums)


genNums = []
for number in range(1, 1000001):
    genNums.append(number)
print(genNums)


#LINE 14 - empty list 'genNums' is created

#LINE 15 -  create for loop, temp var 'number' is created, range number generator
#           is tasked to gen nums 1 - 1million and they become associated to 'number'

#LINE 16 - genNums is called to use append function so that values can be stored at 
#          last index in list, those values come from 'number' since it is asssociated to range values

#LINE 17 - for loop has been exited and print is called to call each value from 'genNums'





















