import sys

# Read the input string from stdin
s = sys.stdin.readline().strip()

found_AB = False
found_BA = False

for i in range(len(s) - 1):
    # Check for 'AB' or 'BA' within the current window
    if s[i:i+2] == "AB" and not found_AB:
        found_AB = True
    elif s[i:i+2] == "BA" and not found_BA:
        found_BA = True

    # If we've found both substrings, break out of the loop
    if found_AB and found_BA:
        break

# Print the result to stdout
if found_AB and found_BA:
    print("YES")
else:
    print("NO")
