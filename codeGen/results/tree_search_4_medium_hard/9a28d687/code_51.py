import sys

def min_cost(n, costs, strings):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = sys.maxsize
        for j in range(i):
            if strings[j].endswith(strings[i]):
                dp[i] = min(dp[i], dp[j] + costs[i - 1])
    return dp[n] if dp[n] != sys.maxsize else -1

n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]
print(min_cost(n, costs, strings))
