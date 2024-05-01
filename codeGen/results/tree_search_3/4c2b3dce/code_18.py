import sys

def has_ab_ba(s):
    n = len(s)
    for i in range(n-1):
        if s[i:i+2] == 'AB' and s[i+n-3:i+n] == 'BA':
            return "YES"
    return "NO"

s = input()
print(has_ab_ba(s))
