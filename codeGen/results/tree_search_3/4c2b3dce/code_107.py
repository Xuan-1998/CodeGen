import sys

def has_substrings(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n):
        state = 0 if s[i] == 'A' else 2
        if i > 0:
            prev_state = dp[i - 1]
            dp[i] = (state == 1 and prev_state == 2) or (state == 2 and prev_state == 1)
        else:
            dp[i] = state in [1, 2]

    return "YES" if any(dp[i:i+3] == [True, True, False] for i in range(n - 2)) else "NO"

s = input()
print(has_substrings(s))
