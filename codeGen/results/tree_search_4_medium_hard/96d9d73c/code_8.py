def can_partition(arr):
    n = len(arr)
    k = int(input())
    m = int(input())

    dp = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if arr[i - 1] - m <= arr[0]:
                dp[i][j] = any(dp[p][j - 1] and arr[i - 1] - m <= arr[p - 1] <= arr[i - 1] + m for p in range(1, i))
            else:
                dp[i][j] = False

    return dp[n][k]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(can_partition(arr))
