import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
size_dp = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 or j == 1:
            dp[i][j] = 1
        else:
            min_val = sys.maxsize
            size_min = []
            for s in range(1, min(i, j) + 1):
                remaining_i = (i - s)
                remaining_j = (j - s)
                if remaining_i == 0 or remaining_j == 0:
                    dp[i][j] = min_val
                    size_dp[i][j] = size_min
                    break
                for k in range(1, min(remaining_i, remaining_j) + 1):
                    new_remaining_i = (remaining_i - k)
                    new_remaining_j = (remaining_j - k)
                    if dp[new_remaining_i][new_remaining_j] < min_val:
                        min_val = dp[new_remaining_i][new_remaining_j]
                        size_min.append(s)
            if i == n and j == m:
                break
        if len(size_dp[i][j]) == 0:
            size_dp[i][j] = [s for s in size_dp[i-1][j] + size_dp[i][j-1]]
        else:
            size_dp[i][j] = list(set([s for s in size_dp[i-1][j] + size_dp[i][j-1]]))
            size_dp[i][j].sort()

print(dp[n][m])
