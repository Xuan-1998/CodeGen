import sys

def min_cost_to_sort(strings):
    n = len(strings)
    dp = [[0] * (n + 1) for _ in range(n)]
    
    for i in range(1, n + 1):
        cost = strings[i - 1][::-1].count(strings[i - 1]) if strings[i - 1] < strings[i - 2] else strings[i - 1].count(strings[i - 1][::-1])
        dp[i - 1][i] = min(dp[i - 2][i - 1] + cost, dp[i - 2][i - 2] + 2 * cost) if i > 1 else cost
    
    return dp[-1][-1] if dp[-1][-1] != n else -1

strings = [input().strip() for _ in range(int(input()))]
print(min_cost_to_sort([s[::-1].count(s) for s in strings]))
