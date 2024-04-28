import sys
s = input()
if "AB" in s and "BA" in s:
    if s.index("AB") < s.index("BA"):
        print("YES")
    else:
        print("YES")
else:
    print("NO")
