def longest_increasing_subsequence_count(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if arr[j - 1] > arr[j - i]:
                dp[i][j] = max(dp[i - 1][k] + 1 for k in range(i - 1, j))
            else:
                dp[i][j] = dp[i - 1][j]

    return sum(1 for x in dp[-1] if x == max(dp[-1]))

arr = [int(x) for x in input().split()]
print(longest_increasing_subsequence_count(arr))
