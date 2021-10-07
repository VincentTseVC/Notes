# 'r' -> reading
# 'w' -> writing
# 'a' -> appending

# READING FILE
## s.strip() - remove the leading (前) and trailing (後) white-space, \n, \t

# method 1:
# read() - reads everything from where 'f' points to, into a large string
print("------ read() -------")
f = open('week06.txt', 'r')
lines = f.read() # -> 'hello\nI like programming\nbye'
print(lines)
f.close()


# method 2:
# readlines() - reads everything from where 'f' points to, into a large list
print('------ readlines() ------')
f = open('week06.txt', 'r')
lines = f.readlines() # -> ['hello\n', 'I like programming\n', 'bye']
for line in lines:
    print(line.strip('\n'))
f.close()


# method 3:
# readline() - read ONE line where 'f' points to, move 'f' to the next line..
print('------ readline() ------')
f = open('week06.txt', 'r')
line = f.readline()
while not line.startswith('---'):
    print(line.strip('\n'))
    line = f.readline()
f.close()

# method 4:
# for loop
print('------ for loop ------')
f = open('week06.txt', 'r')
for line in f:
    print(line.strip('\n'))
f.close()



# WRITING FILE
f = open('week06_w.txt', 'w')
f.write('hello\n')
f.write('I hate programming\n')
f.close()

