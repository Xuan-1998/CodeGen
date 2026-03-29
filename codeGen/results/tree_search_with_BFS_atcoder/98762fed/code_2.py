MOD = 998244353
N, M = map(int, input().split())
dp = [[0]*(M+1) for _ in range(N+1)]
power = [[0]*(M+1) for _ in range(N+1)]
S = [[0]*(M+1) for _ in range(N+1)]

def fastPower(a, b):
    result = 1
    while b > 0:
        if b & 1:
            result = result * a % MOD
        a = a * a % MOD
        b >>= 1
    return result

for i in range(N+1):
    for j in range(M+1):
        if i == 0 or j == 0:
            dp[i][j] = power[i][j] = 1
        else:
            power[i][j] = fastPower(2, i*j)
            dp[i][j] = (power[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD
            S[i][j] = (dp[i][j] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]) % MOD

result = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        result = (result + dp[i][j] * (power[N-i][M-j] + S[i-1][j-1] - 1)) % MOD

print(result)

