
currentUsers = ['folgee', 'doom', 'quake', 'cartman', 'stanTheMan', 'Ben Dove']

newUsers = ['batman', 'wonder woman', 'doOm', 'STANtheMaN', 'V']


for newUser in newUsers:
    if newUser.lower() in currentUsers:
        print(f"Sorry, {newUser} that user name is already taken, please enter a new name")
    else:
        print(f"Username  '{newUser}' is available, you may continue")









































