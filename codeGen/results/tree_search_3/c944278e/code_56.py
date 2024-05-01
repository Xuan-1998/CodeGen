import sys
from collections import defaultdict

def solve(n, s):
    dp = [defaultdict(int) for _ in range(n + 1)]

    # base case: when only one team is left, it's the sole winner
    if n == 0:
        return []

    # transition function: update dp[i+1][k] based on dp[i][j]
    for i in range(1, n + 1):
        for j in range(2**i):
            k = (s[j] << (i - 1)) & 1
            for w in range(2**i):
                if s[w] == k:
                    dp[i][k] += dp[i-1][w]

    # find the winning teams by traversing the dp array from bottom to top
    winners = []
    for i in range(n, -1, -1):
        for k in range(2**i):
            if dp[i][k]:
                winners.append(k)
                break

    return winners


# test cases
for _ in range(int(input())):
    n, s = int(input()), bin(int(input()))[2:].zfill(n)
    print(' '.join(map(str, solve(n, s))))
