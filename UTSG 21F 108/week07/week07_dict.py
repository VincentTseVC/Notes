# Mapping (dict)

items = {'apple': 1.75, 'carrot': 2.25, 'banana': 3.25}

# d = {key1: value1, key2: value2, ...}
# dictionary has NO ORDER...
# key has to be unique
# key has to be immutable type

name_to_gpa = {'alice': 4.0, 'bob': 0.7, 'carol': 3.5}

# -- how to get alice's gpa
print(name_to_gpa['alice'])
print(name_to_gpa.get('alice'))
# print(name_to_gpa['vincent']) # => KeyError

# -- how to add a new entry (pair) to the dictionary
print('---- adding new entry ----')
name_to_gpa['vincent'] = 2.7
print(name_to_gpa)

# -- how to update/modify an existing entry
print('---- updating existing entry ----')
name_to_gpa['bob'] = 1.0
print(name_to_gpa)

# -- how to delete an entry
print('---- deleting an entry ----')
bobs_gpa = name_to_gpa.pop('bob')
print("bob's gpa: " + str(bobs_gpa))
print(name_to_gpa)

del name_to_gpa['vincent']
print(name_to_gpa)

# -- how to combine with antother dictionary
print('---- combine two dictionaries ----')
d2 = {'elaine': 3.0, 'alice': 2.0}
name_to_gpa.update(d2)
print(name_to_gpa)


# -- how to get all the keys
print('---- get all keys ----')
names = list(name_to_gpa.keys())
print(names)

# -- how to get all the values
print('---- get all values ----')
gpas = list(name_to_gpa.values())
print(gpas)


print("=== example ===")
# print the name of the smartest person (person with the highest gpa)

## step1: get a list of names
names = list(name_to_gpa.keys())
## step2: get a list of gpas
gpas = list(name_to_gpa.values())
## step3: get the maximum gpa
highest_gpa = max(gpas)
## step4: get the index of the highest_gpa in the gpas list
index = gpas.index(highest_gpa)
## step5: get the name at the same position of the index in gpas list
name = names[index]
## step6: Yayyyyy, print the name :)
print(name)

print(names[gpas.index(max(gpas))])


# -- how to ieterate (loop through) a dictionary
print('---- looping over a dict ----')
for name in name_to_gpa:
    gpa = name_to_gpa[name]
    print(name, gpa)



'''============= IMPORTANT EXAMPLE =============='''
def get_gpa_to_name(name_to_gpa: dict[str, float]) -> dict[float, list[str]]:
    """
    >>> d = {'alice': 4.0, 'bob': 0.7, 'carol': 4.0, 'elaine': 3.0}
    >>> r = get_gpa_to_name(d)
    >>> r == {4.0: ['alice', 'caorl'], 0.7: ['bob'], 3.0: ['elaine']}
    True
    """
    #                    

    # gpa_to_name -> {4.0: ['alice', 'carol'], 0.7: ['bob'], 3.0: ['elaine']}

    #           第一次      第二次       第三次        第四次
    # name ->   alice   ->  bob     ->  carol   ->  elaine
    # gpa  ->   4.0     ->  0.7     ->  4.0     ->  3.0


    gpa_to_name = {}

    for name in name_to_gpa:
        gpa = name_to_gpa[name]

        # ----------- IMPORTANT ----------
        # case1: if key is ALREADY in the result dictionary
        if gpa in gpa_to_name:
            # append to the end of the corresponding list
            gpa_to_name[gpa].append(name)

        # case2: key is not YET in the result dictionary
        else:
            # add new entry (pair) to the result dictionary
            gpa_to_name[gpa] = [name]
        # --------------------------------

        # --- OR ----
        if gpa not in gpa_to_name:
            gpa_to_name[gpa] = []
        gpa_to_name.append(name)


    return gpa_to_name

print("===== important example =====")
d = {'alice': 4.0, 'bob': 0.7, 'carol': 4.0, 'elaine': 3.0}
r = get_gpa_to_name(d)
print(r)




