# Read input
n = int(input())
p = list(map(int, input().split()))

# Initialize 2D array dp with all elements initialized to infinity
dp = [[float('inf')] * n for _ in range(n)]

# Fill up the dp table using bottom-up dynamic programming
for i in range(1, n):
    dp[i][i] = 0  # The minimum number of multiplications needed to multiply a single matrix is 0

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + p[i] * p[k + 1] * p[j + 1])
        if dp[i][j] == float('inf'):
            break

# Construct the optimal parenthesization by tracing back the minimum number of multiplications
parentheses = []
i, j = n - 1, 0
while i > 0:
    for k in range(i):
        if dp[j + 1][k + 1] + p[k] * p[i] * p[i] <= dp[j + 1][i]:
            parentheses.append(chr(ord('A') + j))
            j = k
            break
    i -= 1

# Reverse the optimal parenthesization and print the result
parentheses = parentheses[::-1]
for i in range(len(parentheses) - 1):
    print(f"({parentheses[i]})", end="")
print(parentheses[-1])
