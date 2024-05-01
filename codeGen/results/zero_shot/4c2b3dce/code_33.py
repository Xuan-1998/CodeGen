import sys

s = sys.stdin.readline().strip()

if "AB" in s and "BA" in s:
    if "AB" not in s[2:] or "BA" not in s[1:]:
        print("NO")
else:
    print("NO")

print("YES")
