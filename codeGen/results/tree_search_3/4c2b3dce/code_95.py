# Read the input string from stdin
s = input()

# Initialize sets for occurrences of 'AB' and 'BA'
ab_set = set()
ba_set = set()

# Iterate through the string, considering all possible substrings
for i in range(len(s)):
    for j in range(i + 3, len(s) + 1):
        substring = s[i:j]
        
        # Check if the substring is 'AB' or 'BA'
        if substring == "AB":
            ab_set.add(substring)
        elif substring == "BA":
            ba_set.add(substring)

# Check if both sets are non-empty, indicating the presence of both substrings
if len(ab_set) > 0 and len(ba_set) > 0:
    print("YES")
else:
    print("NO")
