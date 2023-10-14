#This program will demonstrate why it is important to use multiple if statements
#rather than if-elif-else

#if they use multple situations, then not all toppings will be added as onlyone 
# test need to pass, and once it does, it skips the rest of tests


requestedToppings = ['mushrooms', 'extra cheese',]
meats = ['Pepperoni']

if 'mushrooms' in requestedToppings:
    print("Adding mushrooms")

elif 'extra cheese' in requestedToppings:
    print("Adding extra cheese")

elif 'Pepperoni' in requestedToppings:
    print("Adding pepperoni")


#Output only shows 'Adding mushrooms'
#
#WHY? because our block of code ask only for test to pass, and when it does
#pass, it skips the rest of the test, and so the program terminates

#
#
















