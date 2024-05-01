import sys

def has_ab_ba(s):
    seen_as = 0
    seen_bs = 0
    for c in s:
        if c == 'A':
            seen_as += 1
        elif c == 'B':
            seen_bs += 1
        
        # Check if we've seen both 'AB' and 'BA'
        if (seen_as % 2 == 0) ^ (seen_bs % 2 == 0):
            continue
        if (seen_as >= 1 and seen_bs >= 1 and s[seen_as:seen_as+2] == "AB" and 
            s[-3:-1] == "BA"):
            return "YES"
    return "NO"

s = input()
print(has_ab_ba(s))
