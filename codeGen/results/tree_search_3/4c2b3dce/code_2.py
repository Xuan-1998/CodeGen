import sys

def find_substrings(s):
    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            remaining = s[i+2:]
            if remaining.startswith('BA'):
                return "YES"
    return "NO"

s = input().strip()
print(find_substrings(s))
