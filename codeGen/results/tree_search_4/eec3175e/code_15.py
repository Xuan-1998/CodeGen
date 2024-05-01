def find_subset_sum_divisible_by_m(n, m, arr):
    dp = [[False for _ in range(m)] for _ in range(n)]
    
    # Base case: dp[0][j] = 1 if j == 0, and 0 otherwise.
    for j in range(m):
        if j % m == 0:
            dp[0][j] = True
    
    for i in range(1, n):
        for k in range(m):
            # If sum is less than 0, there's no subset with this sum
            if k < 0:
                continue
            
            # If the current number is within the modulus m and adding it results in a valid sum
            if k % m == arr[i] % m:
                dp[i][k] = dp[i-1][k-arr[i]] or True
                
            # Otherwise, just check for the previous subset sums
            else:
                dp[i][k] = dp[i-1][k]
    
    return 1 if any(dp[-1][k] for k in range(m)) else 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(find_subset_sum_divisible_by_m(n, m, arr))
