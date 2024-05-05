# Step 1: Define the input variables
n = int(input())
p = list(map(int, input().split()))

# Step 2: Create a table to store the minimum number of multiplications needed for each subproblem
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    dp[i][i-1] = (p[i-1][0] if i > 0 else 1) * p[i][0]

for L in range(2, n+1):
    for i in range(n-L+1):
        j = i + L - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            if k > 0:
                op = (dp[i][k-1] if k > 0 else 0) * p[k][1]
            else:
                op = 1
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + op)
        if j > i:
            dp[i][j] += (p[j][1] if j < n-1 else 0) * p[j][0]

# Step 3: Construct the optimal parenthesization of the matrix chain
s = []
def reconstruct(i, j):
    if i == j:
        s.append(chr(ord('A') + i))
    else:
        k = dp[i][j].index(min(dp[i][j]))
        reconstruct(i, k)
        reconstruct(k+1, j)
        s.append('(')
        s.append(s.pop(-1) + ')')

reconstruct(0, n-1)

# Step 4: Print the optimal parenthesization of the matrix chain
print(''.join(s))
