def matrix_chain_order(p):
    n = len(p) - 1

    # Create a 2D dp table and fill it based on the recurrence relation
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    # Reconstruct the optimal parenthesization string
    s = ['A']
    i, j = 0, n - 1
    while j > 0:
        for k in range(i, j):
            if dp[i][k] + dp[k + 1][j] == dp[i][j]:
                s.append(chr(ord('A') + k))
                i, j = k + 1, j
                break

    return ''.join(reversed(s))

# Example usage:
n = int(input())
p = list(map(int, input().split()))
print(matrix_chain_order(p))
