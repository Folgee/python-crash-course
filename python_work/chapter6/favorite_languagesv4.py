favorite_languages = {
        'jen': 'python',
        'sarah': 'C',
        'edward': 'rust',
        'phil': 'python',
        }

print("The following languages have been mentioned")
for language in set(favorite_languages.values()):
    print(f"\n\t{language.title()}")

#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for taking the poll!")

#if 'erin' not in favorite_languages.keys():
#    print(f"Erin, please take the poll")

    



















