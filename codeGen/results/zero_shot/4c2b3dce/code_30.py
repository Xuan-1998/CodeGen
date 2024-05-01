import sys

s = input()

if "AB" in s and "BA" in s[len("AB"):]:
    print("YES")
else:
    print("NO")
