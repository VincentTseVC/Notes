x = 1
name = "Vincent"

#            0         1      2
names = ["Vincent", "Anya", "Nick"]

print(names[1][2])


#    0    1        2       3
#              0     1
#                   01
L = [1, 3.14, [[], 'vc'], None]

print(L[2][1][1]) # c




# --------
s = "Vincent"
# s[0] = "B"
s2 = s.upper()
print(s, s2)
# ------------

L = [1, 3, 5, 6]
L[0] = "vc"
print(L)

# ============== Methods ==============
# Modify the original list
# DON'T do: L = L.func(), becuase func() => None

names = ["Vincent", "Anya", "Nick"]

# add a new item to the end of the list
print("---- append ----")
names.append("Alice")
print(names)

# insert an item at a specific index
print("---- insert ----")
names.insert(1, "Bob")
print(names)

# remove item by giving its index
print("---- pop ----")
x = names.pop(3)
print(names)
print(x + " was removed")

# remove item by itself
print("---- remove ----")
names.remove("Bob")
print(names)

# extend the current list with another list
print("---- extend ----")
names.extend(["Carol", "Elaine"])
print(names)

# names.append(["Carol", "Elaine"])
# print(names)

# => ['Vincent', 'Anya', 'Alice', 'Carol', 'Elaine', ['Carol', 'Elaine']]

# find item
print("---- find (index) ----")
i = names.index("Anya")
print(i)
# print(names.index("Brian"))


# sort
print("---- sort ----")
names.sort()
# names.sort(reverse=True)
print(names)




# ========== Concatanation ==========
# Generate a new list, does not modify the original list
L = [1, 2, 3]
L2 = L + [5, 6]
print(L, L2)

L3 = L * 2
print(L, L3)

# ======= Slicing ========
# SAME AS STRING
print(names[1:3])




# ======= Alias ========
#     x=id0            id0: 1
#     y=id0            id1: 4
#     L=id3            id2: 5
#                      id3: [id0, id1, id2,   id4]
#                      id4: "vc"

#     L2=id3


x = 1
y = x

L = [1, 4, 5]
L2 = L
L2.append("vc")
print(L)




# ----------------------
#                     id0: 1
#                     id1: 4
#                     id2: 3
#                     id3: 6
#                     id4: [id2, id3]
#                     id5: [id0, id1, id4]


#     L=id5
#  f( L=id4    )

# Example 1:
print("example1: ")
def f(L):
    L = 4
    print(L)

L = [1, 4, [3, 6]]
f(L)
print(L)


# Example 2:
# ----------------------
#                     id0: 1
#                     id1: 4
#                     id2: 3
#                     id3: 6
#                     id4: [id2, id3]
#                     id5: [id0->id1, id1, id4]


#     L=id5
#  f( L=id5    )
print("example2: ")
def f(L):
    L[0] = 4
    print(L)

L = [1, 4, [3, 6]]
f(L)
print(L)


# Example 3:
# ----------------------
#                     id0: 1
#                     id1: 4
#                     id2: 3
#                     id3: 6
#                     id4: [id2, id3]
#                     id5: [id0, id1, id4]
#                     id6: [id0->id1, id1, id4]


#     L=id5
#  f( L=id6    )
print("example3: ")
def f(L):
    L[0] = 4
    print(L)

L = [1, 4, [3, 6]]
L2 = L[:]
f(L2)
print(L)




# Example 4:
# ----------------------
#                     id0: 1
#                     id1: 4
#                     id2: 3
#                     id3: 6
#                     id4: [id2->id1, id3]
#                     id5: [id0, id1, id4]
#                     id6: [id0, id1, id4]


#     L=id5
#  f( L=id6    )
print("example4: ")
def f(L):
    L[2][0] = 4
    print(L)

L = [1, 4, [3, 6]]
L2 = L[:]
f(L2)
print(L)



print("--------------")
# ===== Iterating over list ======
# for <var> in <collection>:
# for ch in "csca08":
# for n in [1, 4, 6, 8]:
# for name in ["vincent", "nick", ....]:

names = ["Vincent", "Ayna", "Nick"]
for name in names:
    print(name)


def sum_list(L: list[int]) -> int:
    # return sum(L)
    total = 0
    for num in L:
        total += num
    return total

print(sum_list([1, 6, 8, 4, 5]))



def filter_negative(L):
    new_L = []
    for num in L:
        if num >= 0:
            new_L.append(num)

    return new_L


print(filter_negative([1, -6, 8, -4, 5]))



# part a)
def count_vowel(s):
    count = 0
    for ch in s:
        if ch in "AEIOUaeiou":
            count = count + 1
    return count

# part b)
def count_total_vowel(L):
    total_count = 0
    for s in L:
        total_count += count_vowel(s)
    return total_count


print(count_total_vowel(["Vincent", "Anya", "Banana"]))




def extract_even(s):
    """
    >>> extract_even("csca08")
    'cc0'
    """
    return s[::2]

def sf(s):
    """
    >>> sf("I got 100 on csca08")
    Igotoncsca10008"
    """
    letters = ""
    digits = ""
    # for


    return letters + digits



