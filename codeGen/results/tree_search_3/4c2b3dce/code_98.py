import sys

def find_substrings():
    s = sys.stdin.readline().strip()
    if len(s) < 3:
        return "NO"

    if 'A' not in s or 'B' not in s:
        return "NO"

    a_index = s.index('A')
    b_index = s.index('B')

    # Check if 'BA' is present
    if s[a_index:b_index+1] == "AB" and s[b_index+1:] != "BA":
        return "NO"
    
    return "YES"

print(find_substrings())
