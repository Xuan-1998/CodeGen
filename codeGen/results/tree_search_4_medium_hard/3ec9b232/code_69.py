from collections import defaultdict

def ways_to_create_v(n, m):
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case: creating an empty array
    dp[0][0] = 1
    
    # Calculate the number of ways to create V for each i and j
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][i-1]
            else:
                for k in range(j, i+1):
                    dp[i][j] += (dp[k-1][j-1] * pow(i-k+1, MOD-2, MOD)) % MOD
    # Return the number of ways to create V with n elements and j subsets
    return dp[n][n]

# Receive inputs from stdin
n = int(input())
m = list(map(int, input().split()))

# Calculate the answer using the algorithm
ans = ways_to_create_v(n, m)
print(ans)
