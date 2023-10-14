alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original postion: {alien_0['x_position']}")

#Move the alien to the right 
#Determin how far to move the alien based on its current location

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:   
# this alien is fast 
    x_increment = 3

# The new position is the old postion plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New postion: {alien_0['x_position']}")


