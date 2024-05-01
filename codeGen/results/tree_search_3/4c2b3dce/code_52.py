# Read input string
s = input().strip()

# Count occurrences of 'A' and 'B'
a_count = s.count('A')
b_count = s.count('B')

# Check if string contains both 'AB' and 'BA' substrings
if a_count >= 1 and b_count >= 1:
    # If 'A' appears at least once, we can find 'BA' by checking the remaining part of the string
    if 'A' in s[s.index('A')+1:]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

