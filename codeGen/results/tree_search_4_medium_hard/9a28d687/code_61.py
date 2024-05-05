import sys
from collections import defaultdict

def solve(n):
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    strings.sort(key=len)

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        prev_cost = 0
        for j in range(i-1, -1, -1):
            if strings[j] <= strings[i-1]:
                dp[i][j] = prev_cost + costs[j]
            else:
                min_cost = float('inf')
                for k in range(j+1, i):
                    min_cost = min(min_cost, dp[k][j] + costs[k])
                dp[i][j] = min_cost
            prev_cost = max(prev_cost, dp[i-1][j] + costs[j-1])

    return dp[-1][-1]

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
