def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = {0: arr[0]}
    for i in range(1, n+1):
        if i <= k:
            dp[i] = max(dp.get(i-1, 0), arr[i])
        else:
            dp[i] = max(dp[i-k], dp.get(i-k-1, 0) + arr[i])
    return sum(dp.values())

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_after_partitioning(arr, k))
