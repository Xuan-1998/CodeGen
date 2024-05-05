import sys

def max_bitwise_or(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], int(s[i:], 2) | int(s[:i], 2))

    return bin(dp[0])[2:]

n = int(input())
s = input()
print(max_bitwise_or(s))
