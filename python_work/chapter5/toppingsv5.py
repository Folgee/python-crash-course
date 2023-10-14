



#ALGORITHM
#
#1. Create of list of toppings
#2. Create a loop that will run through list.
#3. Decision is made from loop and ask if the current value of toppings is ==
#   green peppers,if true I must inform user  that green peppers are not avaliable
#   FALSE - Add remaining toppings that are instock
#4. Inform user that pizza is ready 





requestedToppings = ['mushrooms', 'green peppers', 'extra cheese']

for requestedTopping in requestedToppings:
    if requestedTopping == 'green peppers':
        print(f"Sorry we are out of green peppers")
    else:
        print(f"Adding {requestedTopping}")

print("\nFinished making your pizza")

































