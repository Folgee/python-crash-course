#PROBLEM 
#
#create a list of numbers 1-10 in ordinal order, and print them out  
#
#ex. 1st, 2nd, 3rd, 4th


nums = list(range(1, 11))
print("Here are the list of numbers in Ordinal order")

for num in nums:
    if num == 1:
        print(f"\n{num}st")
    elif num == 2:
        print(f"\n{num}nd")
    elif num == 3:
        print(f"\n{num}rd")
    else: 
        print(f"\n{num}th")

#   ALGORITHM
#
#1. create list of nums 1-10, print out to user what we are doing
#2. loop through list to detect all nums 
#3. condition test in loop, check if num == 1, print 1 with 'st'
#4. condition test in loop, check if num == 2, print 2 with 'nd'
#5. condition test in loop, check if num == 3, print 3 with 'rd'
#6. condition test in loop, other nums, print with 'th'
#


































