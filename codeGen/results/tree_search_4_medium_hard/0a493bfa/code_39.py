import sys

def read_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, m, a, b

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def update_dp(i, j, dp, a):
    if i == 0:
        return 0
    max_beauty = -sys.maxsize
    for k in range(i-1):
        gcd = calculate_gcd(a[k], a[i])
        if gcd not in [x for x in b if x <= a[i]]:
            beauty = dp[k][j] + gcd
            max_beauty = max(max_beauty, beauty)
    return max_beauty

n, m, a, b = read_input()
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(m+1):
        dp[i][j] = update_dp(i, j, dp, a)

print(dp[n][m])
