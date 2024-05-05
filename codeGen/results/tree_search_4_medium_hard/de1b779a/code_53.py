import sys
from collections import defaultdict

def solve():
    n, m, c0, d0 = map(int, input().split())
    dp = defaultdict(lambda: defaultdict(int))
    max_profit = 0

    for _ in range(m):
        ai, bi, ci, di = map(int, input().split())
        for i in range(n // ci + 1):
            if c0 >= ci and d0 >= ai:
                dp[(True, c0 - ci, d0 - ai)][0] = max(dp[(True, c0 - ci, d0 - ai)][0], di)
            c0 -= min(c0, ci)
            d0 -= min(d0, ai)

    for state in dp:
        if state[0]:
            max_profit = max(max_profit, dp[state][0])

    print(max_profit)

if __name__ == "__main__":
    solve()
