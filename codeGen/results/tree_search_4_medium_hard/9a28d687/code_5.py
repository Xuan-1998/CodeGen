from collections import deque

def min_cost_to_sort_strings():
    n = int(input())
    costs = [int(x) for x in input().split()]
    strings = [input() for _ in range(n)]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    prev = [-1] * (n + 1)

    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if strings[j] <= strings[i - 1]:
                dp[i][j] = min(dp[i - 1][j], costs[i - 1] + dp[i - 1][j - 1])
                prev[i] = j
            else:
                dp[i][j] = dp[i - 1][j]
        if dp[i][i] == -1:
            return -1

    return dp[n][0]

print(min_cost_to_sort_strings())
