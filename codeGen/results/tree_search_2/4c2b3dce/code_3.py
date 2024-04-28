import sys

s = input().strip()

def check_substrings(s):
    seen_a = False
    for i, c in enumerate(s):
        if c == 'A':
            seen_a = True
        elif c == 'B' and seen_a:
            return "YES"
    return "NO"

print(check_substrings(s))
