def matrix_chain_order(p):
    n = len(p) - 1

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp


def matrix_chain_parenthesis(p, dp):
    n = len(p) - 1

    s = []
    i, j = 1, n
    while i < j:
        min_cost = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
            if cost < min_cost:
                min_cost = cost
                break
        s.append('(')
        s.append(chr(ord('A') + i - 1))
        s.append(')')
        i, j = k + 1, j
    return ''.join(s)


def main():
    n = int(input())
    p = list(map(int, input().split()))
    dp = matrix_chain_order(p)
    print(matrix_chain_parenthesis(p, dp))


if __name__ == "__main__":
    main()
