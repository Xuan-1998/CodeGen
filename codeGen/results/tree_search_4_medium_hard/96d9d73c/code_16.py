def canPartitionIntoKParts(arr, k, m):
    n = len(arr)
    dp = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i // k + 1, k + 1)):
            if i < k:
                dp[i][j] = True
            else:
                dp[i][j] = (dp[i - k][j - 1] and arr[i - k] - m <= arr[i - 1] <= arr[i - k] + m) and \
                           (arr[i - 1] - arr[i - k] + m >= 0)

    for j in range(1, k + 1):
        if dp[n][j]:
            return True

    return False


# Example usage:
n = int(input())  # Number of elements
k = int(input())  # Minimum number of partitions
m = int(input())  # Maximum difference between adjacent elements
arr = list(map(int, input().split()))

if canPartitionIntoKParts(arr, k, m):
    print("Yes")
else:
    print("No")
