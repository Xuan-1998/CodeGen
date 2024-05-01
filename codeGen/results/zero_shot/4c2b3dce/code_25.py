import sys

def check_substrings(s):
    if "AB" in s and "BA" not in s[s.index("AB") + 2:]:
        return "YES"
    elif "BA" in s and "AB" not in s[s.index("BA") + 2:]:
        return "YES"
    else:
        return "NO"

s = sys.stdin.readline().strip()
print(check_substrings(s))
