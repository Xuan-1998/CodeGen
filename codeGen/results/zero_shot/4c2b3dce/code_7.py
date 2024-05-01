import sys

def find_substrings():
    s = input().strip()
    
    if "AB" in s and "BA" not in s:
        remaining_s = s.replace("AB", "", 1)
        if "BA" in remaining_s:
            print("YES")
        else:
            print("NO")
    elif "BA" in s and "AB" not in s:
        remaining_s = s.replace("BA", "", 1)
        if "AB" in remaining_s:
            print("YES")
        else:
            print("NO")
    elif ("AB" in s) and ("BA" in s):
        print("YES")
    else:
        print("NO")

find_substrings()
