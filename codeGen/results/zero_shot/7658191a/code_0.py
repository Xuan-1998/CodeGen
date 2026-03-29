def max_score(n, k, z, arr):
    dp = [[0] * (k + 1) for _ in range(z + 1)]

    for i in range(1, n + 1):
        for j in range(min(i - 1, z) + 1):
            if j == 0:
                dp[j][i - 1] = arr[i]
            else:
                dp[j][i - 1] = max(dp[j - 1][i - 2] + arr[i], dp[j][i - 2] + arr[i])

    return dp[z][k]

n = int(input())
for _ in range(n):
    k, z, n = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
