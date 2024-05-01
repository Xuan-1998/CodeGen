import sys

s = sys.stdin.readline().strip()

if "AB" in s and "BA" not in s:
    print("NO")
elif "BA" in s and "AB" not in s:
    print("NO")
elif ("AB" in s or "BA" in s) and len(s) > 2:
    if "AB" in s and "BA" in s:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
