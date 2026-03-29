def find_winner(T):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return 1

        winner = float('inf')
        for k in range(j - M + 1, j):
            winner = min(winner, dp(i - 1, k))
        memo[(i, j)] = winner
        return winner

    result = []
    for _ in range(T):
        M, X = map(int, input().split())
        for i in range(1, X + 1):
            result.append(dp(X - i + 1, M - 1))
    print(*result, sep='\n')

if __name__ == '__main__':
    T = int(input())
    find_winner(T)
