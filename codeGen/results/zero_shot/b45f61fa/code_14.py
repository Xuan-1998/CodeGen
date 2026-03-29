# Read the input
n = int(input())
p = list(map(int, input().split()))

# Create a table to store the minimum number of multiplications
dp = [[0] * len(p) for _ in range(len(p))]

# Fill up the dp table
for i in range(n - 1):
    dp[i][i + 1] = p[i] * p[i + 1] * (p[i + 2] if i < n - 2 else 0)

for L in range(3, n):
    for i in range(n - L):
        j = i + L
        dp[i][j] = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j]
            if q < dp[i][j]:
                dp[i][j] = q

# Construct the optimal parenthesization
optimal_parenthesis = []
i, j = 0, n - 1
while i < j:
    for k in range(i, j):
        if dp[i][k + 1] + dp[k + 1][j] == dp[i][j]:
            optimal_parenthesis.append((chr(ord('A') + i), chr(ord('A') + k)))
            i = k + 1
            break

# Print the result
print(''.join(f'({"".join([f"({'{:c}' '*k)}" for c, k in optimal_parenthesis])})' if len(optimal_parenthesis) > 0 else '{A}' * n))
