# 你打我呀 哈哈哈

# Numbers:
# Integer (int): 1  2
# Float (flaot): 1.0 3.14

print(6 + 2)
print(6 - 2)
print(6 * 2)
print(6 / 2)    # -> float
print(3 // 2)   # integer division
print(10 % 4)   # mod, 餘數
print(2 ** 3)  
print(2 ** (1 + 2) + 2 * 3)
print(6 + 2.0)

# print(3 / 0) # ZeroDivisionError


# 文字, String (字符串)
print("I'm learning programming")
print('I\'m learning programming')
print('2')

print("My nams is " + "Vincent")
print("CSC108" * 3)

# print(3 + "2") # TypeErorr

print(str(3) + "2")
print(3 + int("2"))

# print(int("a")) # ValueError




# Variable
x = 1
print(x)
print('x')
# print(y)    # NameError


x = 1
y = 2
x = y
print(x)
print(y)


# SWAP
print("-----")
x = 1
y = 2

temp = x
x = y
y = temp

print(x) # 2
print(y) # 1





# boolean: True False
# ==, >, >=, <, <=, !=
print("----")
x = 3
print(x == 3)
print(x > 2)
print(x >= 4)

name = "vc"
print(name == "vc")


# a  b       a or b         a and b      not a
# ------------------------------------------------
# T  T         T               T           F
# T  F         T               F           F
# F  T         T               F           T
# F  F         F               F           T


# !!!!!!!!!!!!!!!!!!!!!!!!
print(2 == 2.0 or 3 > 5)


# 考試 一定考！！！！！！
# lazy evaluation
print(2 == 2.0 or 3 / 0 == 0)

# print(2 == 2.0 and 3 / 0 == 0)
# print(3 / 0 == 0 or 2 == 2.0)

print(False and 2 + "3" == 5)