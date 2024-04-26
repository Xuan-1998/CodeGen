def contains_AB_and_BA(s):
    first_found = False
    i = 0
    while i < len(s) - 1:
        if not first_found and (s[i:i+2] == 'AB' or s[i:i+2] == 'BA'):
            first_found = True
            i += 2  # Skip over the found pair to ensure non-overlapping
        elif first_found and (s[i:i+2] == 'AB' or s[i:i+2] == 'BA'):
            return "YES"
        else:
            i += 1
    return "NO"

# Read input from stdin
s = input().strip()
print(contains_AB_and_BA(s))
