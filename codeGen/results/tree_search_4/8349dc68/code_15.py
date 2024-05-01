import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    max_sum = [0] * (n + 1)

    for i in range(k, n + 1):
        dp[i] = max(dp[i-1], arr[i-k:i].max())

    for i in range(k, n + 1):
        max_sum[i] = max(max_sum[i-1], dp[i])

    return max_sum[-1]

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_after_partitioning(arr, k))
