
motorcycles = ['honda', 'yamah', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)


del motorcycles[3]
print(motorcycles)

motorcycles.insert(3, 'suzuki')
print(motorcycles)


popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#reminder that pop method removes suzuski as it the last element of 
#my list and it wont print again in the future unless I add it back
print(f"The last motorcycle that I bought was a {popped_motorcycles.title()}")


motorcycles.remove('honda')
print(motorcycles)



cheapBike = 'yamah'
motorcycles.remove(cheapBike)
print(motorcycles)
print(f"\n I was told {cheapBike.title()} is a low quality bike for my liking")


#print out remaining elements from list
print(f"\n Here are the remaining bikes {motorcycles}")
