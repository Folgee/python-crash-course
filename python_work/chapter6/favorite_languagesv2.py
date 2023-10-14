favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python',
        }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t {name.title()}, I see you love {language}")




#ALGORITHM
#
#1. Initiate dictionary fav_languages, dictionary hold keys = names, values = language
#2. create list 'friends', elements are "phil", "sarah"
#3. loop, temp var 'name' and associate it to fav_... (dictionary), specificly keys 
#   1. print var name
#
#4. conditional test, ask is name in friends?
#   yes? var lanage = fav_lanagues dictionary with key being associated to temp 'var'
#       1.print var name, 'I see you love' var 'lanague'
#
#
#













