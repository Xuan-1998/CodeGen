===BEGIN CODE===
def min_operations(arr):
    n = len(arr)
    memo = {}
    dp = [0] * n

    for i in range(n):
        dp[i] = float('inf')
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = min(dp[i], dp[j-1] + 1)

    return dp[-1]

arr = list(map(int, input().split()))
print(min_operations(arr))
===END CODE===
