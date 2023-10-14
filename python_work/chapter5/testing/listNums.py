#I really dont know what this program is intended to do
#
#
#it seems more as if it is suppsed to create a list of nums between 1 and 50
#so that it may skip every two nums and then a loop is made that creates a 
#condition, where i a 

#
nums = list(range(1, 50, 2))

for num in nums:
    if num < 25:
        print(nums[:25])
    elif num > 26:
        print(nums[26:])

    











































