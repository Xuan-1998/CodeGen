def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    s = [[0] * (n+1) for _ in range(n+1)]

    for i in range(2, n+1):
        dp[i-1][i-1] = 0

    for chain_len in range(2, n+1):
        for i in range(1, n-chain_len+2):
            j = i + chain_len - 1
            min_cost = float('inf')
            for k in range(i, j):
                cost = dp[i-1][k] + dp[k][j-1] + p[i-1]*p[k]*p[j]
                if cost < min_cost:
                    min_cost = cost
                    s[i-1][j] = k+1
            dp[i-1][j] = min_cost

    return build_order(s, n)

def build_order(s, n):
    order = []
    for i in range(2, n+1):
        j = i + 1
        while j > 0:
            k = s[i-1][j-1]-1
            order.append((chr(i+64), chr(j+65)))
            j = k
    return " -> ".join(f"({a}{b})" for a, b in order[::-1])

p = [int(x) for x in input().split()]
print(build_order(*matrix_chain_order(p.split())))
