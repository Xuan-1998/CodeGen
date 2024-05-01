# Read input string from standard input
s = input()

# Check if "AB" appears in the string
if "AB" in s:
    # If it does, check if "BA" also appears in the remaining part of the string
    if "BA" in s[s.index("AB") + 2:]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
