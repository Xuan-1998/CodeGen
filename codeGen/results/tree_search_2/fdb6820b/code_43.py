def count_ways(arr, N):
    # Calculate the maximum value in the array
    max_val = max(arr)
    
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        if i >= max_val:
            dp[i] = sum(dp[j] for j in range(i))
        else:
            dp[i] = dp[i - max_val] + len([j for j in range(max_val + 1, i) if j % max_val == 0])
    
    return dp[N] % (10**9 + 7)

# Read input from stdin
m, N = map(int, input().split())
arr = list(map(int, input().split()))

print(count_ways(arr, N))
