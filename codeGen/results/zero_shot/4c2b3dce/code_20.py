import sys

s = sys.stdin.readline().strip()

if "AB" in s and "BA" in s[len("AB"):]:
    print("YES")
else:
    print("NO")
