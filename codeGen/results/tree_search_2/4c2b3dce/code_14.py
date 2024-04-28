import sys

dp = {}

def solve(s):
    for i in range(len(s)):
        if s[i:i+2] == 'AB':
            j = i + 2
            while j < len(s) and s[j:j+2] != 'BA':
                j += 1
            if j < len(s) and s[j:j+2] == 'BA':
                return "YES"
        elif s[i:i+2] == 'BA' and i > 0 and s[i-1:i+1] == 'AB':
            return "YES"
    return "NO"

s = input().strip()
print(solve(s))
