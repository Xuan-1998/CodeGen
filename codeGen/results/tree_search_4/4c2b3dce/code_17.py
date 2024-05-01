import sys

s = input()

found_ab = False
found_ba = False

for i in range(len(s) - 2):  # Check up to the third last character
    if s[i:i+2] == "AB":
        found_ab = True
        break
    elif s[i:i+2] == "BA" and not found_ab:
        found_ba = True
        break

if found_ab and found_ba:
    print("YES")
else:
    print("NO")
