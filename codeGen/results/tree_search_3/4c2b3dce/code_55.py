code
s = input()

found_ab = False
found_ba = False

for i in range(len(s)):
    if s[i:i+2] == "AB":
        found_ab = True
        i += 1
        while i < len(s) and s[i:i+2] != "BA":
            i += 1
        if i < len(s) and s[i:i+2] == "BA":
            found_ba = True
    elif s[i:i+2] == "BA" and not found_ab:
        found_ba = True

if found_ab and found_ba:
    print("YES")
else:
    print("NO")
