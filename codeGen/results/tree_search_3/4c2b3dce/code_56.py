import sys

s = input()

found_ab = False
found_ba = False

for i in range(len(s) - 1):
    if s[i:i+2] == "AB":
        found_ab = True
    elif s[i:i+2] == "BA" and found_ab:
        print("YES")
        sys.exit(0)

if not found_ab or not found_ba:
    print("NO")
