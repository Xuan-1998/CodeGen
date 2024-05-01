import sys

s = input().strip()

def has_abba(s):
    for i in range(len(s) - 3):
        if s[i:i+2] == "AB" and s[i+2:i+4] == "BA":
            return True
    return False

if has_abba(s):
    print("YES")
else:
    print("NO")
