import sys

def solve():
    s = input().strip()
    if len(s) < 3:
        return "NO"

    ab_count, ba_count = 0, 0
    rolling_hash = [ord(c) for c in s[0]]
    for i in range(1, len(s)):
        rolling_hash.append((rolling_hash[-1] * 31 + ord(s[i])) % (10**9 + 7))
    
    for i in range(len(s) - 2):
        if s[i:i+2] == "AB" and s[i+2:] != "BA":
            return "NO"
        elif s[i:i+2] == "BA" and s[:i][::-1] != "AB":
            return "NO"

    return "YES"

print(solve())
