definitions = {
        'del': 'removes values',
        'get()': 'sets default value as return for requested values that are not declared',
        'pop()': 'removes last elements of list',
        'append()': 'add element to the end of a list',
        'insert()': 'add element at any given position of a list',
        'for': 'a type of statement that is used to loop a block of code',
        'if' : 'a conditional statment, used for asking questions to check if something is ture then do this, if not then do this instead',
        'string' : 'data type, used by chaining characteres toghehter and seeing if they print words in english'
        }

print(f"Here is a small list of some terms that I've learned so far")
for k, v in sorted(definitions.items()):
    print(f"\n\t{k.title()}, --> {v.title()}")
    






























