s = input()
if "AB" in s and "BA" in s.replace("AB", ""):
    print("YES")
else:
    print("NO")
