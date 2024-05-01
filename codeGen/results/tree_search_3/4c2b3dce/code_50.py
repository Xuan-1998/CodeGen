import sys

# Read input from stdin
s = input().strip()

# Initialize pointers
left = 0
right = len(s) - 1

while left <= right:
    # Check if "AB" is found at the beginning or end of the string
    if s[:2] == "AB":
        if s[-2:] == "BA":
            print("YES")
            sys.exit(0)
        else:
            left += 1
    # Check if "BA" is found at the beginning or end of the string
    elif s[-2:] == "BA":
        if s[:2] == "AB":
            print("YES")
            sys.exit(0)
        else:
            right -= 1

print("NO")
