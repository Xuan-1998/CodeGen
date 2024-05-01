def min_max_recompute(s, t, path):
    n = len(path)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        if path[i-1] == s or path[i-1] == t:
            dp[i][j] = 0
        else:
            min_val = float('inf')
            max_val = 0
            for j in range(i):
                if path[j] == path[i]:
                    break
                min_val = min(min_val, dp[j][k])
                max_val = max(max_val, dp[j][k])
            dp[i][j] = min_val + 1

    return dp[-1][-1], dp[-1][-2]

# Example usage:
s = 0
t = 4
path = [0, 1, 3, 2, 4]
min_recompute, max_recompute = min_max_recompute(s, t, path)
print(min_recompute, max_recompute)
