import sys

def check_substr(s):
    if "AB" in s and "BA" not in s:
        print("YES")
    elif "BA" in s and "AB" not in s:
        print("YES")
    else:
        print("NO")

s = input()
check_substr(s)
