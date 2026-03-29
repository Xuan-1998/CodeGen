import sys; input = lambda:map(int,sys.stdin.readline().split())
from collections import defaultdict

def solve():
    t = int(input()[0])
    for _ in range(t):
        n, k = input()
        dp = [defaultdict(int) for _ in range(1 << k)]
        dp[0][0] = 1
        for i in range(k):
            new_dp = defaultdict(int)
            for mask in range(1 << (k - i - 1)):
                for j in range(2 ** i):
                    new_mask = mask | (j & ((1 << i) - 1))
                    new_dp[new_mask][i + 1] += dp[mask][i]
            dp = new_dp
        print(sum(dp[-1].values()) % (10**9 + 7))

solve()
