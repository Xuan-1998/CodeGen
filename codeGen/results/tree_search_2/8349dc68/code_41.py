import sys

def max_sum_of_subarrays(arr, k):
    n = len(arr)
    if k > n:
        return max(arr)

    dp = {i: 0 for i in range(k)}
    total_max_sum = max(sum(arr[:k]), sum(arr[k-n+k//2:k+n//2]))

    for i in range(k, n):
        dp[i] = max(dp[i-1], arr[i] + dp.get(i-k, 0))
        total_max_sum = max(total_max_sum, dp[i])

    return total_max_sum

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_sum_of_subarrays(arr, k))
