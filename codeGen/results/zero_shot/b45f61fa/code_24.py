# Read input
n = int(input())
p = list(map(int, input().split()))

# Create a table to store the solutions to subproblems
dp = [[0] * n for _ in range(n)]
for gap in range(2, n):
    for i in range(n - gap):
        j = i + gap
        dp[i][j] = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j]
            if q < dp[i][j]:
                dp[i][j] = q

# Construct the optimal parenthesization
result = []
i = 0
while i < n - 1:
    j = i + 1
    while j < n - 1 and dp[i][j] == float('inf'):
        j += 1
    result.append(chr(ord('A') + i))
    if j != i + 1:
        result.append('(')
    for k in range(i, j):
        result.append(chr(ord('A') + k))
    result.append(')')
    i = j

# Print the result
print(''.join(result))
