# mode:
#  'r' -> reading
#  'w' -> writing
#  'a' -> appending



# method 1:
# .read() - reads everything from where 'f' points to, into a large string
print('----- read() -----')
f = open("week07.txt", "r")
lines = f.read() # => 'hello\nI like programming\nbye'
print(lines)
f.close()


# method 2:
# .readlines() - reads everything from where 'f' points to, into a large list
print('----- readlines() -----')
f = open("week07.txt", "r")
lines = f.readlines() # => ['hello\n', 'I like programming\n', 'bye']
for line in lines:
    print(line.strip())
f.close()


# method 3:
# .readline() - read ONE line where 'f' points to, move 'f' to the next line
print('----- readline() -----')
f = open("week07.txt", "r")
line = f.readline() # => 'hello\n'
while line != "":
    print(line.strip())
    line = f.readline()
f.close()


# method 4:
# for loop
print('----- for loop-----')
f = open("week07.txt", "r")
for line in f:
    print(line.strip())
f.close()


# WRITING FILE
f = open('week07_w.txt', 'w')
f.write('hello\n')
f.write('I hate programming\n')
f.close()