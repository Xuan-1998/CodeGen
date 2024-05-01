def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max(dp[i-1][j], arr[i-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-j][j-1] + max(arr[i-j:i]))

    return dp[n][k]

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxSumAfterPartitioning(arr, k))

if __name__ == "__main__":
    main()
