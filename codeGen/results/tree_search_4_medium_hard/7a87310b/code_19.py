def count_positive_invertible_matrices(N):
    dp = [[0] * (N+1) for _ in range(N+1)]

    # Base case
    if N <= 3:
        if N == 0: return 0
        elif N == 1: return 1
        else: return 2

    for i in range(1, N+1):
        for j in range(min(i, N), max(N-i, 0)):
            for k in range(max(0, i-1-k), min(i, N)):
                l = i - k - 1
                if (k+l) == i and is_positive_invertible(k, l, j):
                    dp[i][j] += 1

    return sum(dp[N])

def is_positive_invertible(a, b, c):
    det = a * (a + c) - b * b
    return det > 0

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_positive_invertible_matrices(N))
