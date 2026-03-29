from collections import defaultdict

def min_steps_to_color(t, n, memo=defaultdict(lambda: float('inf'))):
    m = len(t)
    for i in range(m):
        if t[i] in 'abcdefghijklmnopqrstuvwxyz':
            return -1  # If there are any characters left that can't be colored, return -1
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    def dfs(i, j):
        if memo[(i, j)] != float('inf'):
            return memo[(i, j)]
        if i == m:
            return 1
        dp[i][j] = min((dfs(i + k, j) for s in strings for k, start in enumerate(s) if start <= i < i + len(s)) or [float('inf')]) + (0 if t[i] not in 'abcdefghijklmnopqrstuvwxyz' else 1)
        memo[(i, j)] = dp[i][j]
        return dp[i][j]

    return min(dfs(i, j) for i in range(m) for j in range(m + 1)) or -1

t = input()
n = int(input())
strings = [input() for _ in range(n)]
print(min_steps_to_color(t, n))
