parrot  = "Norwegian Blue"
"""
print(parrot)
print(parrot[3] + parrot[4] + parrot[9] + parrot[3] + parrot[6] + parrot[8])
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
"""
x = 'ABCDEFG'
number = "9,223;372:036 854,775;807;;;;"
seperators = number[1::4]

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[len(letters) - 1:len(letters) - 9:-1])


