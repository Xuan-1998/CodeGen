def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k

    def get_parenthesization(i, j):
        if i == j:
            return f'A{i}'
        return '(' + get_parenthesization(i, s[i][j]) + ')' + get_parenthesization(s[i][j] + 1, j)

    print(get_parenthesization(0, n - 1))

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    matrix_chain_order(p)
