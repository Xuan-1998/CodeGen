# Step 1: Read input
n = int(input())  # number of matrices
p = list(map(int, input().split()))  # dimensions of matrices

# Step 2: Initialize a table for dynamic programming
dp = [[0] * (n+1) for _ in range(n+1)]

# Step 3: Fill the table using dynamic programming
for i in range(1, n):
    dp[i][i] = 0  # minimum cost to multiply 1 matrix is 0

for L in range(2, n+1):  # consider all lengths of subchains from 2 to n
    for i in range(n-L+1):  # start of the subchain
        j = i + L - 1  # end of the subchain
        dp[i][j] = float('inf')  # initialize minimum cost as infinity

        for k in range(i, j):  # consider all possible cuts
            q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            if q < dp[i][j]:
                dp[i][j] = q

# Step 4: Construct the optimal parenthesization tree
s = ''
for i in range(n-1):
    if p[i]*p[i+1] == min(p[i:] + [0]):
        s += '('
    else:
        s += ')(' * (dp[i][i+1] - 1) + ')'

# Step 5: Print the result
print(s)
