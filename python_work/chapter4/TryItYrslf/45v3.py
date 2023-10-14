#here is another more simpler way for 4-5

genNums = list(range(1, 1_000_000))

print(max(genNums))
print(min(genNums))
print(sum(genNums))

# main difference between this and v2 is that here we created our list and wrapped it with 
# range function so that nums could be generated inside of a list which has been assisned 
# to 'genNums' rather than creating empty list and, using a for loop to create 
# temp var and be assosiated to range() which then we called append() to add all values 
# from temp var to be added at last index, and loop goes through all cases to then print out 
# our needs "max" "min" "sum)
#
#
#












