# Read the input string
s = input()

# Initialize pointers for 'AB' and 'BA'
i = 0  # Pointer for 'AB'
j = len(s) - 1  # Pointer for 'BA'

found_AB = False
found_BA = False

while i < j:
    if s[i:i+2] == 'AB':
        found_AB = True
        i += 2
    elif s[j:j-2] == 'BA':
        found_BA = True
        j -= 2
    else:
        i += 1
        j -= 1

# Check if both substrings were found
if found_AB and found_BA:
    print("YES")
else:
    print("NO")
