import sys

def winners(M, X):
    dp = [[0] * (M + 1) for _ in range(X + 1)]

    # Base case: one player remains
    for j in range(1, M + 1):
        dp[1][j] = (X - j + 1) % M + 1

    # Bottom-up approach with two loops
    for i in range(2, X + 1):
        for j in range(M - 1, 0, -1):
            if i % 2 == 1:  # odd number of players
                dp[i][j] = ((X - j + 1) % M) + 1
            else:  # even number of players
                dp[i][j] = (j % M) + 1

    results = []
    for i in range(1, X + 1):
        results.append(dp[i][M - 1])

    return results

T = int(sys.stdin.readline().strip())
for _ in range(T):
    M, X = map(int, sys.stdin.readline().split())
    print(*winners(M, X), sep='\n')
