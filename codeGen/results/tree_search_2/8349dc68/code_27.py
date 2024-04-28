def max_sum_subarrays(arr, k):
    n = len(arr)
    dp = {i: arr[i] for i in range(k)}
    
    for i in range(k, n):
        if i < k:
            dp[i] = max(dp[j] for j in range(i-k+1, i+1))
        else:
            dp[i] = max(dp[j] + arr[i], dp[max(j for j in range(i-k+1, i))])
    
    return max(dp.values())

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_sum_subarrays(arr, k))
