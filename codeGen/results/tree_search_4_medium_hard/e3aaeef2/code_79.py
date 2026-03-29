def count_digits(n):
    return len(str(n))

def modulo(n, m):
    return n % 10

dp = [[0] * (200005) for _ in range(1000000)]

for i in range(1000000):
    dp[i][0] = 1

for i in range(1, 1000000):
    for j in range(2, 200005):
        if j <= count_digits(i):
            k = count_digits(modulo(i, 10)) - 1
            dp[i][j] = max(dp[modulo(i, 10)][k], dp[i][j-1])
        else:
            dp[i][j] = dp[i][j-1]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m]%1000000007)
