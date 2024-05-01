def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(k + 1):
        if i == 0:
            continue
        j = i - 1
        while j <= k:
            dp[i][j] = max(dp[i-1][j], arr[j-i:j+1])
            j -= 1

    return sum(arr) - dp[k][k]

# Read input from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(max_sum_after_partitioning(arr, k))
