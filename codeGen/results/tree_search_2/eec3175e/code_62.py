def subset_sum_divisible_by_m(arr, m):
    n = len(arr)
    dp = {0: 1}
    
    for i in range(n):
        for r in range(m):
            if (r + arr[i]) % m in dp:
                dp[(r + arr[i]) % m] = 1
            else:
                dp[r] = 0
                
    return 1 if 0 in dp else 0

# Example usage:
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(subset_sum_divisible_by_m(arr, m))
