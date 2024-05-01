import sys

def find_substrings(s):
    n = len(s)
    dp = [False] * (n - 1)

    for i in range(n):
        if i >= 2:
            if s[i-2:i] == 'AB':
                dp[i-3] = True

    for i in range(n-1, -1, -1):
        if i < n-2 and s[i:i+2] == 'BA':
            return "YES"

    return "NO" if any(dp) else "YES"

s = sys.stdin.readline().strip()
print(find_substrings(s))
