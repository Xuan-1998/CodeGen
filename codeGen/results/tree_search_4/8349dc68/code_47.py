from collections import defaultdict

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    memo = defaultdict(int)

    def dfs(i):
        if i > n:
            return 0
        if i not in memo:
            curr_max = max(arr[i-k+1:i+1])
            include_sum = curr_max + dfs(i+k-1)
            exclude_sum = dp[i-k]
            memo[i] = max(include_sum, exclude_sum)
        return memo[i]

    for i in range(1, n+1):
        if i <= k:
            dp[i] = max(arr[:i])
        else:
            dp[i] = dp[i-1]
            curr_max = max(arr[i-k:i])
            dp[i] += curr_max
    return dp[-1]

# Test the function
arr = list(map(int, input().split()))
k = int(input())
print(max_sum_after_partitioning(arr, k))
