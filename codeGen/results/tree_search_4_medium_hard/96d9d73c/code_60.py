from sys import stdin

def can_partition(arr, k, m):
    N = len(arr)
    dp = [[False] * (k + 1) for _ in range(N + 1)]

    dp[0][0] = True
    for i in range(1, N + 1):
        dp[i][0] = False
        if arr[i - 1] > m:
            for j in range(k + 1):
                dp[i][j] = False
            break

    for i in range(1, N + 1):
        for j in range(1, min(i, k) + 1):
            if all(abs(arr[x] - arr[0]) <= m for x in range(i)):
                if dp[i - 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                dp[i][j] = False

    return any(dp[N])

N, K, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
print(can_partition(arr, K, M))
