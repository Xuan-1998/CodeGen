import sys

# Read the input string from stdin
s = sys.stdin.readline().strip()

# Check for characters common to 'AB' and 'BA'
for char in set('AB'):
    if s.count(char) >= 2:
        pivot_char = char
        break

if pivot_char is None:
    print("NO")
else:
    # Partition the string based on the pivot character
    a, b, c = s.partition(pivot_char)

    # Check for 'AB' in the first and second parts
    if 'AB' in a or 'BA' in a + b:
        print("YES")
    else:
        print("NO")
