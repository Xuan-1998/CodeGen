# Read input from stdin
s = input()

# Initialize flags for 'AB' and 'BA'
has_ab = False
has_ba = False

# Check if 'AB' appears in the string
for i in range(len(s) - 1):
    if s[i] == 'A' and s[i + 1] == 'B':
        has_ab = True
        break

# Check if 'BA' appears in the remaining part of the string
if not has_ab:
    for i in range(len(s) - 1, 0, -1):
        if s[i] == 'B' and s[i - 1] == 'A':
            has_ba = True
            break

# Print the result based on the flags
print("YES" if has_ab and has_ba else "NO")
