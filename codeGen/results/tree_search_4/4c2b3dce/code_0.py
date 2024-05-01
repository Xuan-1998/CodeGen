import sys

def has_non_overlapping_AB_BA(s):
    dp = [False] * (len(s) - 2 + 1)
    for i in range(1, len(s) - 2):
        if s[i-1:i+1] == "AB" or s[i-1:i+1] == "BA":
            dp[i] = not dp[i-1]
    return "YES" if dp[-1] else "NO"

s = input()
print(has_non_overlapping_AB_BA(s))
