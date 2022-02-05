x = 1
name = 'Vincent'
#            0         1        2
names = ['Vincent', 'Chris', 'Alice']
print(names[1][2])


#    0    1        2       3
#              0     1
#                   01
L = [1, 3.14, [[], 'vc'], None]

print(L[2][1][1]) # -> c



# Immutable
#  - int, float, bool, None, str, (tuple)
s = 'Vincent'
# s[0] = 'B'
s2 = s.upper()
print(s, s2)


# Mutable
#  - list, (dict, set)
L = [1, 3, 5, 6]
L[0] = 'vc'
print(L)



# ========== Methods =============
# Modify the original list
# DON'T do: L = L.func(), because func() => None

names = ['Vincent', 'Chris', 'Alice']

# -- add a new item to the end of the list
print('---- append ----')
# names = names.append('Bob')
# print(names) # -> None

names.append('Bob')
print(names) # -> None

# -- insert an tiem at a specific index
print('---- insert ----')
names.insert(1, 'Brian')
print(names)

# -- remove item by giving its index
print('---- pop ----')
x = names.pop(3)
print(names)
print(x + " was removed")

# -- remove item by itself
print('---- remove ----')
names.remove('Chris')
print(names)

# -- extend the current list with another list
print('---- extend ----')
names.extend(['Carol', 'Elaine'])
print(names)

# names.append(['Carol', 'Elaine'])
# print(names)
# => ['Vincent', 'Brian', 'Bob', 'Carol', 'Elaine', ['Carol', 'Elaine']]

# -- find item
print('---- find item (index) ----')
i = names.index('Bob')
print(i)

# i = names.index('Chris') # ValueError

# if item in lst:
#     list.index(item)


# -- sort the list
print('---- sort ----')
# names.sort(reverse=True)
names.sort()
print(names)


# ======= Concatanation =======
# Generate a new list, does not modify the orginal list
L = [1, 2, 3]
L2 = L + [5, 6]
print(L, L2)

L3 = L * 2
print(L, L3)


# ====== Slicing ======
# SAME AS STRING
print(names[1:3])


# ========== Alias ==========
#         x=id0           id0: 1
#         y=id0           id1: 4
#         L=id3           id2: 5
#                         id3: [id0, id1, id2,    id4]
#                         id4: 'vc'
#                         id5: 'b'
#         L2=id3
#         s=id4
x = 1
y = x
L = [1, 4, 5]
L2 = L
L2.append('vc')
print(L)

s = 'vc'
# s[0] = 'b'

print()

# ------- Example 1 -------------
#                   id0: 1
#                   id1: 4
#                   id2: 3
#                   id3: 6
#                   id4: [id2, id3]
#                   id5: [id0, id1, id4]

#     L=id5

#  f (   L=id5->id1    )

print('example 1:')
def f(L):
    L = 4
    print(L)

L = [1, 4, [3, 6]]
f(L)
print(L)


# ------- Example 2 -------------
#                   id0: 1
#                   id1: 4
#                   id2: 3
#                   id3: 6
#                   id4: [id2, id3]
#                   id5: [id0->id1, id1, id4]

#     L=id5

#  f (   L=id5   )

print('example 2:')
def f(L):
    L[0] = 4
    print(L)

L = [1, 4, [3, 6]]
f(L)
print(L)


# ------- Example 3 -------------
#                   id0: 1
#                   id1: 4
#                   id2: 3
#                   id3: 6
#                   id4: [id2, id3]
#                   id5: [id0, id1, id4]
#                   id6: [id0->id1, id1, id4]

#     L=id5
#     L2=id6

#  f (   L=id6   )

print('example 3:')
def f(L):
    L[0] = 4
    print(L)

L = [1, 4, [3, 6]]
L2 = L[:]
f(L2)
print(L)


# ------- Example 4 -------------
#                   id0: 1
#                   id1: 4
#                   id2: 3
#                   id3: 6
#                   id4: [id2->id1, id3]
#                   id5: [id0, id1, id4]
#                   id6: [id0, id1, id4]

#     L=id5

#  f (   L=id6   )

print('example 4:')
def f(L):
    L[2][0] = 4
    print(L)

L = [1, 4, [3, 6]]
f(L[:])
print(L)


# iterate (loop through) list
# for <var> in <collection>:
# for ch in "CSC108":
# for n in [1, 4, 6, 8]:
# for name in ['VIncent', 'chris', 'bob', ....]

# part a)
def count_vowel(s: str) -> int:

    count = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count += 1
    return count

# part b)
def count_total_vowel(L: list[str]) -> int:
    total_count = 0
    for s in L:
        total_count += count_vowel(s)
    return total_count

names = ['Vincent', 'Chris', 'Alice']
print(count_total_vowel(names))



def sum_list(L: list[int]) -> int:
    # return sum(L)
    total = 0
    for num in L:
        total += num
    return total


print(sum_list([1, 6, 8, 4, 5]))


def filter_negative(L: list[int]) -> list[int]:
    new_L = []
    for num in L:
        if num >= 0:
            new_L.append(num)
            # new_L.extend([num])
            # new_L += [num]

    return new_L

print(filter_negative([1, -6, 8, -4, 5]))






# IMPORTANT 
def square_it(L: list[int]) -> None:
    """Update L so that every number is squared

    >>> nums = [2, 4, 5]
    >>> square_it(nums)
    >>> nums == [4, 16, 25]
    True
    """
    # L -> [2, 4, 5]

    # 第一次：num -> 2 -> 4
    # 第二次：num -> 4 -> 16
    # 第三次: num -> 5 -> 25

    # for num in L:
    #     num = num ** 2



    # L -> [4, 16, 25]

    # 第一次: i -> 0
    # 第二次: i -> 1
    # 第三次: i -> 2

    for i in range(0, len(L), 1):
        L[i] = L[i] ** 2


for x in range(1, 10, 2):
    print(x)



x = 1
y = 2

temp = x
x = y
y = temp