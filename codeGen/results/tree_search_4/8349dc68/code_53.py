def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        local_max_sum = arr[i - 1]
        for j in range(1, min(i, k) + 1):
            if j > 1:
                local_max_sum = max(local_max_sum, dp[i - j] + arr[i - 1])
            else:
                local_max_sum += arr[i - 1]
        dp[i] = local_max_sum
    
    return dp[n]

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(maxSumAfterPartitioning(arr, k))

if __name__ == "__main__":
    main()
