# Duplicate the string
s += s

# Compare the lexicographical order of the duplicated string and the one without the last character
if s < s[:-1]:
    print(s)
else:
    print(s[:-1])
