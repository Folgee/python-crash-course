favorite_languages = {
        'jen': 'python',
        'sarah': 'C',
        'edward': 'rust',
        'phil': 'python',
        }


#for key, value in favorite_languages.items():
#    print(f"\n\t {key.title()}'s favorite language is {value.title()}.")
friends = ['phil', 'sarah']

#next line of code, temp var name is associated to keys from 
#favorite_lanague dicitionary 
for name in favorite_languages.keys():
    print(f"{name.title()}")

    if name in friends:
#fav_lang dictionary with keys that are also in friends list are called so
#next line of code can print out values assoicated to 'name' which 
#are found in fav_lang dictionary 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
        




















