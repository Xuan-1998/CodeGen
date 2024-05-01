def max_sum(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max(arr[:i])
            else:
                dp[i][j] = max(dp[m][j-1] + arr[m], dp[m][j] for m in range(i))
    return dp[n][k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_sum(arr, k))
