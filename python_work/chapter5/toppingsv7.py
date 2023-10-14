availableToppings = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

requestedToppings = ['mushrooms', 'french fries', 'extra cheese']

for requestedTopping in requestedToppings:
    if requestedTopping in availableToppings:
        print(f"\nAdding {requestedTopping.upper()}")

    else:
        print(f"\nERROR---Sorry we do not have {requestedTopping}!")

print(f'\nFinished making your pizza')






























