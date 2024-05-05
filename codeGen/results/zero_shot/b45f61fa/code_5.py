import sys

def matrix_chain_order(n, p):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    s = ['A'] * n  # initial state: no parentheses

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            min_mults = sys.maxsize
            for k in range(i, j):  # try all possible splits
                mults = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if mults < min_mults:
                    min_mults = mults
                    s[i] = '('
                    for l in range(i, k):
                        s[l] = ')'
                    s[k] = '('
            dp[i][j] = min_mults

    return ''.join(s)

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(n, p))
