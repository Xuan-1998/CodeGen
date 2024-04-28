from collections import defaultdict

def solve():
    s = input().strip()
    dp = defaultdict(bool)
    
    for i in range(len(s)):
        if i < 2:
            continue
        if (s[i-1] == 'A' and s[i-2] == 'B') or (s[i-1] == 'B' and s[i-2] == 'A'):
            dp[(i, len(set(s[:i])) % 2)] = True

    return "YES" if any(dp.values()) else "NO"

print(solve())
