pizzas = ['deep dish', 'thin crust', 'pan']
friendsPizzas = pizzas[:]

pizzas.append('hand tossed')
friendsPizzas.append('dry')


print("\n My favorite pizza's are ")
for pizza in pizzas:
    print(f"- {pizza}")


print("\n My friends Favorite pizza's are ")
for friendsPizza in friendsPizzas:
    print(f" - {friendsPizza}")











