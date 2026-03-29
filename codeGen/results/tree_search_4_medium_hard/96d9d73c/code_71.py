def can_partition(arr, k, m):
    n = len(arr)
    dp = [[False] * (n // k + 1) for _ in range(n)]

    # Base case: empty array can be partitioned into 0 partitions
    dp[0][0] = True

    for i in range(1, n):
        for j in range(min(i, n // k), -1, -1):
            if (i > 0 and all(abs(arr[m] - arr[i-1]) <= m for m in range(i))):
                # If we've reached this point, it means the current subarray can be
                # partitioned into j partitions. So, check if the remaining
                # elements can also be partitioned into (i-k) // k partitions.
                dp[i][j] = (dp[i-1][int((i-1)//k)] or i < k)
            else:
                # If we've reached this point, it means the current subarray cannot
                # be partitioned into j partitions. So, set dp[i][j] to False.
                dp[i][j] = False

    return dp[n-1][-1]

# Read input from stdin
n, k, m = map(int, input().split())
arr = list(map(int, input().split()))

print(can_partition(arr, k, m))
