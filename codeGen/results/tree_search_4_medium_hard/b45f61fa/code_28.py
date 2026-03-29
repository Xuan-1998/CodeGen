def get_parenthesization(i, j):
    if i == j:
        return str(chr(ord('A') + i))
    min_cost = float('inf')
    best_parenthesization = ''
    for k in range(i, j):
        cost = dp[i][k] + dp[k + 1][j]
        if cost < min_cost:
            min_cost = cost
            best_k = k
    left_parenthesization = get_parenthesization(i, best_k)
    right_parenthesization = get_parenthesization(best_k + 1, j)
    return '(' + left_parenthesization + 'x' + str(p[i]) + '[' + str(p[i]) + 'x' + str(p[best_k]) + ']' + right_parenthesization

print(get_parenthesization(0, n - 1))
