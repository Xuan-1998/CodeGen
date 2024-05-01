code
s = input()
if "AB" in s:
    left = s[:s.index("AB")]
    right = s[s.index("AB") + 2:]
    if "BA" in left:
        print("YES")
else:
    print("NO")
