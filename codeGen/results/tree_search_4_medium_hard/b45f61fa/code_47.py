===BEGIN CODE===
from sys import stdin

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        dp[i][i] = p[i-1] * p[i] * p[i]
    
    for length in range(3, n + 1):
        for start in range(1, n - length + 2):
            end = start + length - 1
            min_cost = float('inf')
            for k in range(start, end):
                cost = dp[start][k-1] if k > start else 0
                cost += p[k]*p[end]*p[k+1]
                cost += dp[k+1][end]
                min_cost = min(min_cost, cost)
            dp[start][end] = min_cost

    return "({})".format(" ".join(str(i) for i in range(1, n)))

n = int(stdin.readline())
p = [int(x) for x in stdin.readline().split()]

print(matrix_chain_order(p))
