# Let's start with the problem statement:
n = int(input())
p = list(map(int, input().split()))

# The first step is to create a 2D table dp where dp[i][j] will store the minimum number of scalar multiplications needed to multiply matrices p[i] through p[j].
dp = [[0] * (n+1) for _ in range(n+1)]

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            if cost < dp[i][j]:
                dp[i][j] = cost

# Now we have the minimum number of scalar multiplications needed to multiply matrices p[0] through p[n-1].
min_cost = dp[0][n-1]

# The next step is to construct a table m where m[i][j] will store the matrix that should be multiplied with p[i] and p[j+1] to get the minimum number of scalar multiplications.
m = [[i+1] for _ in range(n+1)]

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j]
        min_cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
        m[i][j] = k+1

# Finally, we can construct the optimal parenthesization by tracing back through the table m.
optimal_parenthesis = ""
for i in range(n-1):
    if m[i][i+n-i-2] == i:
        optimal_parenthesis += "( " + str(i) + " * "
    else:
        optimal_parenthesis += "("
print(optimal_parenthesis[:-4])
