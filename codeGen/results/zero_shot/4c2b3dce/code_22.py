import sys

s = input().strip()
if "AB" in s and "BA" not in s:
    print("NO")
elif "BA" in s and "AB" not in s:
    print("NO")
elif "AB" in s and "BA" in s:
    print("YES")
else:
    print("NO")
