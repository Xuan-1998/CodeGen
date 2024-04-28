# Read the input string from standard input
s = input()

# Count the occurrences of 'A' and 'B'
a_count = s.count('A')
b_count = s.count('B')

# Check if both substrings are present
if a_count >= 1 and b_count >= 1:
    print("YES")
else:
    print("NO")
