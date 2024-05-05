import sys
from collections import defaultdict

def min_cost_to_sort_strings(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    cost = []
    strings = []

    # Read input from stdin
    n = int(sys.stdin.readline())
    for i in range(n):
        c, s = sys.stdin.readline().strip().split()
        cost.append(int(c))
        strings.append(s)

    # Preprocess the cost array to store the length of each string
    len_cost = [0] * (n + 1)
    for i in range(1, n + 1):
        len_cost[i] = len_cost[i - 1] + len(strings[i - 1])

    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        if j == 0:
            return 0
        res = float('inf')
        for k in range(j + 1):
            res = min(res, dfs(i - 1, k) + cost[j - 1] + (i > 0))
        dp[i][j] = res
        return res

    # Calculate the minimum total cost using dynamic programming
    res = float('inf')
    for j in range(n):
        res = min(res, dfs(n, j) + len_cost[n] - len_cost[j])

    # Print the answer to stdout
    if res == float('inf'):
        print(-1)
    else:
        print(res)

min_cost_to_sort_strings(int(input()))
