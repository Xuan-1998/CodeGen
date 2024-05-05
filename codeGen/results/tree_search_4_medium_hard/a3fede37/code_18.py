n = int(input())
arr = [int(x) for x in input().split()]

k = 10

dp = [[[float('-inf')] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][i][0] = arr[i]

for k in range(1, k + 1):
    for i in range(n - k + 1):
        j = i + k
        for node in range(i, j + 1):
            include_i = dp[node-1][j-1][k-1] + arr[node]
            exclude_i = max_sum_path(node+1, j, k)
            dp[i][j][k] = max(include_i, exclude_i)

print(dp[0][-1][-1])
