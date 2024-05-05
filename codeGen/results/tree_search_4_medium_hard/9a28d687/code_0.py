import sys

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if all(strings[k] <= strings[i - 1] for k in range(j)):
                dp[i][j] = min(dp[i-1][k] + costs[j] for k in range(j))
            else:
                dp[i][j] = min((dp[i-1][k] + costs[j]) for k in range(j) if strings[k] <= strings[i - 1])
    
    return min(dp[n][-1], cost=10**9)

print(solve())
