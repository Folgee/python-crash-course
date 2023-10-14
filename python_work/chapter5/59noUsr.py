
#users = ['emily', 'nathan', 'nick', 'mike', 'admin',
#        'jorge', 'alex', 'antonio', 'ivan', 'marisa']

users = []

if users:
    for user in users:

#    if 'admin' in user:
#    I had made a decision to check if Admin is in our list of user 
        if user == 'admin':    
            print(f'\n\tHello there sir, would you like to see a status report?')
    
        else:
            print(f"\n\tHi {user.title()} and welcome back to our site!")

else: 
    print(f"Yo we need more user registered and logged in to the site!!")






























