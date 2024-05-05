import sys
from collections import namedtuple

Cost = namedtuple('Cost', 'cost reverse_cost')

n = int(input())
dp = [[0] * 10**5 for _ in range(n + 1)]
prev_strings = []

for i in range(n):
    cost, reverse_cost = map(int, input().split())
    prev_strings.append(Cost(cost, reverse_cost))

for i in range(1, n + 1):
    for j in range(10**5):
        if not dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j]
        else:
            cost = sys.maxsize
            for prev_cost, prev_reverse_cost in prev_strings:
                if prev_cost <= j and (not prev_reverse_cost or j >= prev_reverse_cost):
                    if not dp[i - 1][j]:
                        break
                    cost = min(cost, dp[i - 1][j] + prev_reverse_cost)
            if cost != sys.maxsize:
                dp[i][j] = cost
            else:
                print(-1)
                exit()

print(min(dp[n]))
