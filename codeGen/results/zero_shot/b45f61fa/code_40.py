import sys

def matrix_chain_order(p):
    n = len(p)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(i-1, -1, -1):
            if j == i-1:
                dp[i][j] = 0
            else:
                min_mult = sys.maxsize
                for k in range(j, i):
                    mult = dp[k][j-1] + p[j-1][0]*p[k][1]*p[i-1][1] + dp[i-1][i]
                    if mult < min_mult:
                        min_mult = mult
                dp[i][j] = min_mult

    order = []
    i, j = n-1, 0
    while j > 0:
        if j == i-1:
            order.append('A' + str(i))
            break
        for k in range(j, i+1):
            if dp[i][j] == dp[k][j-1] + p[j-1][0]*p[k][1]*p[i-1][1] + dp[i-1][i]:
                order.append('(')
                order.append('A' + str(k))
                j = k
                break

    return ''.join(reversed(order))

n = int(input())
p = [int(x) for x in input().split()]
print(matrix_chain_order(p))
