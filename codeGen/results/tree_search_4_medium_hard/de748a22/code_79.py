import sys

def query_sign_variable_sum(signs, l, r):
    total = 0
    for i in range(l-1, r):
        total += signs[i]
    return total

def dp_sign_variable_sum(signs, n, q, queries):
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 0
    for l in range(2, n+1):
        for r in range(l, n+1):
            if signs[r-1]:
                total = query_sign_variable_sum(signs, l-1, r)
                dp[l][r] = min(dp[l-1][r], abs(total))
            else:
                dp[l][r] = 0
    for l, r in queries:
        print(min(dp[l-1][r], abs(query_sign_variable_sum(signs, l-1, r))))
