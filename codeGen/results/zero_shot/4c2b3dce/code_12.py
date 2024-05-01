s = input()
found_AB = False

# Check if "AB" appears in the string s
for i in range(len(s) - 1):
    if s[i:i+2] == "AB":
        found_AB = True
        break

if not found_AB:
    print("NO")
else:
    # If "AB" is found, check if "BA" also appears in the remaining part of the string
    for i in range(len(s) - 1):
        if s[i:i+2] == "BA":
            print("YES")
            return

print("NO")
