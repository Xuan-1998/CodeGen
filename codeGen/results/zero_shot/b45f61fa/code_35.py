# Take input for n (number of matrices) and p[] (dimensions)
n = int(input())
p = list(map(int, input().split()))

# Initialize a table dp[][] to store minimum number of multiplications
dp = [[0] * len(p) for _ in range(len(p))]

# Fill up the table using dynamic programming
for chain_length in range(2, n+1):
    for i in range(n-chain_length+1):
        j = i + chain_length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            if q < dp[i][j]:
                dp[i][j] = q

# Print the optimal parenthesization
print(''.join(f'({i})' for i in range(1, n)))
