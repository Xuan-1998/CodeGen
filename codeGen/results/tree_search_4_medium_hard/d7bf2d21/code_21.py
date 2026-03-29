def count_lis(arr):
    n = len(arr)
    memo = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if arr[i] > arr[j]:
                memo[i] = max(memo[i], memo[j] + 1)
        dp[i] = memo[i]

    return max(dp)

# Example usage:
arr = list(map(int, input().split()))
print(count_lis(arr))
