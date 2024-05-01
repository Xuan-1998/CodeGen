# Read the input string from stdin
s = input()

found_ab = False

for i in range(len(s) - 1):
    if s[i:i+2] == "AB":
        found_ab = True
        break

if not found_ab:
    print("NO")
else:
    for i in range(len(s) - 1, 0, -1):
        if s[i-1:i+1] == "BA":
            print("YES")
            break
