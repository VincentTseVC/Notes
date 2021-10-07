from typing import Dict

# d = { Key1: value1, key2: value2} 
# dictionary HAS NO ORDER!!!
# key has to be unique
# key has to be immutable type

name_to_gpa = {'Alice': 4.0, 'Bob': 0.7, 'Carol': 3.5}

# -- how to get Alice's gpa
## just like getting the value qt an index from a string or list
## we can just [ ] to get the corresponding value of a given key
print(name_to_gpa['Alice'])         # -> 4.0
print(name_to_gpa.get('Alice'))     # -> 4.0

# print(name_to_gpa['Vincent'])       # -> KeyError


# -- how to add a new entry to the dictionary
print('--- adding new entry ---')
name_to_gpa['Vincent'] = 2.7
print(name_to_gpa)


# -- how to update/modify an existing entry
print('--- updating existing entry ---')
name_to_gpa['Bob'] = 1.0
print(name_to_gpa)

# -- how to delete an entry
print('--- deleting an entry ---')
bobs_gpa = name_to_gpa.pop('Bob')
print("Bob's gpa is: ", bobs_gpa)
print(name_to_gpa)

del name_to_gpa['Vincent']
print(name_to_gpa)


# -- how to combine with another dictionary
print('--- combine two dictionary ---')
d2 = {'Jacky': 3.0, 'Alice': 2.9}
name_to_gpa.update(d2)
print(name_to_gpa)


# -- how to get all the keys
print('--- get all keys ---')
names = list(name_to_gpa.keys())
print(names)

# -- how to get all the values
print('--- get all values ---')
gpas = list(name_to_gpa.values())
print(gpas)




print('=== example ===')
# print the name of the person with the highest gpa

## step1: get a list of names
names = list(name_to_gpa.keys())
## step2: get a list of gpas
gpas = list(name_to_gpa.values())
## step3: get the maximum gpa
highest_gpa = max(gpas)
## step4: get the index of the highest gpa in the gpa list
index = gpas.index(highest_gpa)
## step5: get the name at the same position of the index in gpas list
name = names[index]
## step5: Yaayyyyyy. print the name :)
print(name)

print(names[gpas.index(max(gpas))])


# -- how to iterate a dictionary
print('--- looping over a dict ---')
for name in name_to_gpa:
    gpa = name_to_gpa[name]
    print(name, gpa)








'''=========== IMPORTANT EXAMPLE ==========='''
def create_gpa_to_name(name_to_gpa: Dict[str, float]):
    '''
    >>> d = {'Alice': 4.0, 'Bob': 0.7, 'Carol': 4.0, 'David': 2.5}
    >>> create_gpa_to_name(d)
    {4.0: ['Alice', 'Carol'], 0.7: ['Bob'], 2.5: ['David']}
    '''

    ## res -> {  4.0: ['Alice', 'Carol'] , 0.7: ['Bob'] }


    ## name -> Alice ----> Bob ----> Carol
    ## gpa  -> 4.0   ----> 0.7 ----> 4.0

    gpa_to_name = {}
    for name in name_to_gpa:
        gpa = name_to_gpa[name]
        
        # ---------- IMPORTANT -----------
        ## case1: if key is ALREADY in the result dictionary
        if gpa in gpa_to_name:
            ## append it to the end of the corresponding list
            gpa_to_name[gpa].append(name)
        ## case2: key is not YET in the result dictionary
        else:
            ## add a new entry to the result dictionary
            gpa_to_name[gpa] = [name]
        # -------------------------------

    return gpa_to_name



print("==== important example ====")
name_to_gpa = {'Alice': 4.0, 'Bob': 0.7, 'Carol': 4.0, 'David': 2.5}
gpa_to_name = create_gpa_to_name(name_to_gpa)
print(gpa_to_name)