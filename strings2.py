parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1])
print(parrot[-14])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])

print(parrot[:9])
print(parrot[10:14])

print(parrot[10:])
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

"""
I run over number by 'for char in number'; Then, I wanna filter the characters - so, I do it by
'char if char not in seperators else ""', which mean - take the current char on condition that 
it doesn't exist in the the string called seperators;
All of the above can can be written only in join function, so - we do it bu concatenating empty
string to desired string represented in join function.
"""
values = "".join(char if char not in seperators else "" for char in number).split()
print([int(val) for val in values])