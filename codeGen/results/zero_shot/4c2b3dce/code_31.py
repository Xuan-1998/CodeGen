s = input()
if "AB" in s or "BA" in s:
    remaining = s.replace("AB", "").replace("BA", "")
    if "AB" in remaining or "BA" in remaining:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
