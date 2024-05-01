import sys

s = sys.stdin.readline().strip()
if "AB" in s and "BA" not in s or "BA" in s and "AB" not in s:
    print("YES")
else:
    print("NO")
