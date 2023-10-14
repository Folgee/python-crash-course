
user = {'name': 'chugg rivers', 'weight': 200, 'employment status': 'unemployed',
        'addiction': 'weed and gluten', 'age':25, 'education': 'college dropout'}

#print(user['name'], user['addiction'], user['education'])

print(f"The following users name is {user['name'].title()}")
print(f"{user['name'].title()} has the following addition(s), {user['addiction']}")

user['other info'] = 'lives with parents, streams video games, known for swattting'

print(f"\n\t There is some other information officers should know before going in; {user['other info']}")

user['education'] = 'high school and college dropout'
print(f"\n We just recived an update that {user['name']} is a {user['education']}")








