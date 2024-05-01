import sys

# Read input from stdin
s = sys.stdin.readline().strip()

last_occurrence = {'A': -1, 'B': -1}

found_ab = False
found_ba = False

for i in range(len(s)):
    if s[i] == 'A':
        last_occurrence['A'] = i
        if found_ba:
            break
    elif s[i] == 'B':
        last_occurrence['B'] = i
        if found_ab:
            break

    # Check for "AB" substring
    if i >= len(s) - 2 and s[i] == 'A' and s[i + 1] == 'B':
        found_ab = True

    # Check for "BA" substring
    if i > 0 and s[i - 1] == 'B' and s[i] == 'A':
        found_ba = True

# Print the result
if found_ab and found_ba:
    print("YES")
else:
    print("NO")
