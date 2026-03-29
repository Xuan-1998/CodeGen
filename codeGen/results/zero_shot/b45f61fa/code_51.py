def read_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

n, p = read_input()

# Initialize a table to store the minimum number of multiplications
dp = [[0] * len(p) for _ in range(len(p))]

for i in range(n - 1):
    dp[i][i + 1] = (p[i] * p[i + 1]) * log(p[i])

for L in range(2, n):
    for i in range(n - L):
        j = i + L
        dp[i][j] = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k + 1][j] + (p[i] * p[k + 1] * log(p[k]))
            if q < dp[i][j]:
                dp[i][j] = q

# Backtrack to find the optimal parenthesization
optimal_parentheses = []
def backtrack(i, j):
    if i == j:
        optimal_parentheses.append(str(ord('A') + i))
    else:
        for k in range(i, j):
            if dp[i][k] + dp[k + 1][j] == dp[i][j]:
                optimal_parentheses.append('(')
                backtrack(i, k)
                backtrack(k + 1, j)
                optimal_parentheses.append(')')

backtrack(0, n - 2)

# Print the result
print(''.join(optimal_parentheses))
