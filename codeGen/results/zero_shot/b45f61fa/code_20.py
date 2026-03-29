n = int(input())  # number of matrices
p = list(map(int, input().split()))  # dimensions of each matrix

dp = [[0] * len(p) for _ in range(len(p))]
for i in range(n):
    dp[i][i] = 0  # base case: no multiplications are needed to multiply a single matrix

for length in range(2, n):
    for i in range(n-length):
        j = i + length - 1
        min_cost = float('inf')
        for k in range(i, j+1):
            cost = dp[i][k-1] + p[i]*p[k]*p[j+1] + dp[k+1][j]
            if cost < min_cost:
                min_cost = cost
                dp[i][j] = cost

def print_parenthesization(i, j):
    if i == j:
        return str(ord('A') + i)  # single matrix, no need for parentheses
    min_cost = dp[i][j]
    for k in range(i, j):
        if dp[i][k] + p[k+1]*p[k]*p[j-1] + dp[k+1][j] == min_cost:
            return f"({print_parenthesization(i, k)} {print_parenthesization(k+1, j)})"

print(print_parenthesization(0, n-2))  # print the optimal parenthesization
