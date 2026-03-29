from math import sqrt

def count_invertible_matrices(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(i, -1, -1):
            if i == j:
                dp[i][j] = 1
            elif j > 0 and sqrt(4 * (i - j) + (i - j)**2) % 2 == 1:
                dp[i][j] = dp[j][i]
            else:
                for a in range(j, i):
                    for b in range(i - a):
                        if i == a + b and sqrt((a - c) * (b - c)) % 2 == 0:
                            dp[i][j] += 1

    return dp[N][N]

T = int(input())

for _ in range(T):
    N = int(input())
    print(count_invertible_matrices(N))
