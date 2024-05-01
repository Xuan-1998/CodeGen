import sys

s = sys.stdin.readline().strip()

def check_substring(s):
    return ("AB" in s) or ("BA" in s)

if check_substring(s):
    if "AB" in s:
        if "BA" not in s[:s.index("AB")]:
            print("YES")
        else:
            print("NO")
    elif "BA" in s:
        if "AB" not in s[:s.index("BA")]:
            print("YES")
        else:
            print("NO")
else:
    print("NO")
