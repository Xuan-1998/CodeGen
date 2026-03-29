from sys import stdin

def read_int():
    return int(stdin.readline())

n, m = map(read_int, [stdin.readline().split() for _ in range(2)][0])
A = list(map(int, stdin.readline().split()))
bad_primes = list(map(int, stdin.readline().split()))

dp = [[False] * (n + 1) for _ in range(n + 1)]
Beauty = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    dp[i][i] = A[i] % 2 == 0

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length
        for k in range(i + 1, j + 1):
            if (dp[i][k-1] and dp[k][j]) or not dp[i][j]:
                Beauty[i][j] = max(Beauty[i][k-1] + 1 if A[k] % 2 == 0 else -1, Beauty[i][k-1])
        if Beauty[i][j] > 0:
            dp[i][j] = True

print(Beauty[0][n-1])
