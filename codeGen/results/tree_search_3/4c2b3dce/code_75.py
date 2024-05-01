# Initialize variables to track the number of 'A's and 'B's seen so far.
a_count = 0
b_count = 0

# Iterate through the string:
for char in s:
    # If the character is 'A', increment the count of 'A's seen.
    if char == 'A':
        a_count += 1
    # If the character is 'B', increment the count of 'B's seen.
    elif char == 'B':
        b_count += 1

    # Check if the current state matches the required pattern for "AB" (i.e., 1 'A' and 1 'B'):
    if a_count == 1 and b_count == 1:
        # Check if there are any remaining characters in the string that could form "BA". If yes, return YES. If no, continue iterating through the string.
        if s[a_count + 1:] != s[a_count:][::-1]:
            continue
        else:
            print("YES")
            break

    # Check if the current state matches the required pattern for "BA" (i.e., 1 'B' and 1 'A'):
    elif b_count == 1 and a_count == 1:
        # Check if there are any remaining characters in the string that could form "AB". If yes, return YES. If no, continue iterating through the string.
        if s[b_count + 1:] != s[b_count:][::-1]:
            continue
        else:
            print("YES")
            break

# If neither "AB" nor "BA" is found anywhere in the string, return NO.
else:
    print("NO")
