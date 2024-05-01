code
import sys

def contains_ab_and_ba(s):
    ab_found = False
    ba_found = False
    
    for i in range(len(s) - 1):  # iterate over the string, considering substrings of length 2
        if s[i:i+2] == "AB":
            ab_found = True
        elif s[i:i+2] == "BA":
            ba_found = True
    
    if ab_found and ba_found:
        return "YES"
    else:
        return "NO"

s = sys.stdin.readline().strip()
print(contains_ab_and_ba(s))
