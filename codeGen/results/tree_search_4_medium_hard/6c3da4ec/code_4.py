import sys
from collections import defaultdict

def max_bitwise_or(s):
    n = len(s)
    dp = [0] * (n + 1)
    memo = defaultdict(int)

    def get_max_or(j):
        if j not in memo:
            if j == 0:
                memo[j] = 0
            else:
                memo[j] = max(dp[j - 1], int(s[j - 1]))
        return memo[j]

    for i in range(1, n + 1):
        dp[i] = get_max_or(i)
        if s[i - 1] == '0':
            dp[i] = min(dp[i], dp[i - 1])
        else:
            dp[i] = max(dp[i], int(s[i - 1]))

    return bin(max(1, dp[-1]))[2:]

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(max_bitwise_or(s))
