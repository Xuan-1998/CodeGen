# Read the input string from standard input
s = input()

# Check if "AB" appears in the string
if "AB" in s:
    # If "AB" is found, check if the remaining part of the string contains "BA"
    if "BA" in s[s.index("AB") + 2:]:
        print("YES")
    else:
        print("NO")
else:
    # If "AB" is not found, check if "BA" appears in the string
    if "BA" in s:
        print("YES")
    else:
        print("NO")
