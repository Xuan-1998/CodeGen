def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(s):
    if s % 2 == 0:
        return 0
    else:
        return -s

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1:
            dp[i][j] = f(gcd(a[0], b[j-1]))
        else:
            max_beauty = 0
            for k in range(i):
                gcd_val = gcd(a[k], a[i-1])
                beauty = dp[k][j-1] + f(gcd_val)
                max_beauty = max(max_beauty, beauty)
            dp[i][j] = max_beauty

print(dp[n][m])
