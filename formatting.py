"""
The alignment is to right; For the first item it'll take 2 places, for the second item it'll take 3 places
and for the third - last one, it'll tale four places.
"""
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

"""
Due to  '<' sign, the alignment will be to left side.
As, if the number of the char are smaller than the mentioned number, so the alignment go to left side. 
"""
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

"""
If the items needed to be print are according to the order they'rementioned, so - there's no need to 
mention them; the second parameter is for the alignment. 
"""
for i in range(1, 13):
    print("No. {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))