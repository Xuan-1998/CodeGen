def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    for j in range(1, n):
        for i in range(j):
            if arr[j] > arr[i]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)

arr = list(map(int, input().split()))
print(longest_increasing_subsequence(arr))
