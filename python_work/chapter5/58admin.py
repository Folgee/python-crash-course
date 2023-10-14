#PROBLEM
#
#Make list of username, including 'admin.
#Create message that will greate each user  after they log in
#
#loop though the list and print a greeting message through each usr 
#


users = ['emily', 'nathan', 'nick', 'mike', 'admin',
         'jorge', 'alex', 'antonio', 'ivan', 'marisa']

for user in users:

#    if 'admin' in user:
#    I had made a decision to check if Admin is in our list of user 
    if user == 'admin':
        print(f'\n\tHello there sir, would you like to see a status report?')
    else: 
        print(f"\n\tHi {user.title()} and welcome back to our site!")








#AlGORITHM
#
#1. Create list of users
#2. create loop that loop through my list of user 
#3. make decision that will check if 'admin is located in list, if true print
#   'hello admin, would you like to see a status report?'
#5. else print 'greeting message to each usr that logged in'
#
#



#OUTPUT 
#
#SO it looks like both conditions that i used produced the same output, but 
#I would like to know which one the author use and which one is more effeicient
#
#
