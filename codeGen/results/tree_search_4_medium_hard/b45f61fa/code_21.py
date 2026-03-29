===BEGIN CODE===
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 3):
            j = i + chain_length - 1
            min_cost = float('inf')
            for k in range(i, j + 1):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j]
                if cost < min_cost:
                    min_cost = cost
                    best_split = (i, k)
            dp[i][j] = min_cost

    # Backtrack to construct the optimal parenthesization
    s = ''
    i, j = 0, n - 1
    while i < j:
        if p[i + 1] > p[j]:
            s += '('
            j -= 1
        else:
            s += ')'
            i += 1
    for _ in range(n):
        s += 'A'

    return s

n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
