x = 1
y = 2

#       0  1  2  3
nums = [1, 2, 5, 6]
print(nums[2])  # => 5


l = [1, 3.14, [[], 'vc'], None]

# >>> 'c'
print(l[2][1][1])



# ----------
s = 'vincent'
s = s.upper()
print(s) 

# ----------


# ============= Methods ============
# Modify the original list
# DON'T do: L = L.func()

L = [1, 3, 5, 6]

# add to the end of the list
L.append(8) 
print('append:', L)

# insert a new item at a specific index
L.insert(1, 4)
print('insert:', L)

# remove item by giving its index
x = L.pop(4)  # deleting the item at index 4 
print('pop [4]:', L, str(x) + ' was removed')

# remove item itself
L.remove(4)   # deleting the item '4'
print('remove:', L, '4 was removed')

# extend the current list by ANOTHER list
L.extend(['vc', '108'])
print('extend:', L)

# example
L.append([148, 'hello'])
print('append2:', L)



# ======== Concatanation =======
# Generate a new list, does not modify the original list, (just like string in python)
L = [1, 2, 3]
L2 = L + [4, 5]
print('L:', L)
print('L2:', L2)


# ======= Alias ========
# x and y both store the same memory address of integer '1'
x = 1
y = x

# L and L2 both points to the same memory address
L = [1, 2, 3]
L2 = L

L2.append(4)
print(L)
print(L2)


# ===== looping through a list ======
items = ['apple', 'banana', 'corrat', 42, None]
for item in items:
    print(item)



def sum_list(L):
    total = 0
    for num in L:
        total += num
    return total

print(sum_list([1, 6, 8, 4, 5]))


def filter_negative(L):
    new_list = []
    for num in L:
        if num >= 0:
            new_list.append(num)

    return new_list

print(filter_negative([1, -5, 3, -4, -2, 6]))


def count_vowels(words):
    count = 0
    for word in words:
        for ch in word:
            if ch in 'aeiouAEIOU':
                count += 1
    return count

print(count_vowels(['apple', 'vincent', 'banana']))
