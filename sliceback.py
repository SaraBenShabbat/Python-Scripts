letters = "abcdefghijklmnopqrstuvwxyz"

# Reverse order, take every char.
backwards = letters[25: 0: -1]
print(backwards)

# Reverse order, take every char.
backwards = letters[::-1]
print(backwards)

# Reverse order, take a char with jumpings of 2.
backwards = letters[:: -2]
print(backwards)

# Create a slice that produce the characters qpo
backwards = letters[16: 13: -1]
print(backwards)

# Slice the string to produce edcba
backwards = letters[4: : -1]
print(backwards)

# Slice the string to produce the last 8 characters, in reverse order
backwards = letters[len(letters): len(letters) - 9: -1]
print(backwards)