def LIS(a):
    n = len(a)
    dp = [[1] * (n+1) for _ in range(n+1)]
    
    max_length = 0
    
    for i in range(2, n+1):
        for j in range(i-1, -1, -1):
            for k in range(j+1, i+1):
                if a[k-1] < a[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + 1)
                    break
            else:
                continue
            break
        
        max_length = max(max_length, dp[i][j])
    
    return max_length

# Read input from stdin
a = [int(x) for x in input().split()]

# Calculate the length of LIS and print to stdout
print(LIS(a))
