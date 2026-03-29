MOD = 998244353
N, M = map(int, input().split())

# Precompute factorials and inverse factorials
fact = [1]*(N+M+1)
ifact = [1]*(N+M+1)
for i in range(1, N+M+1):
    fact[i] = fact[i-1]*i%MOD
    ifact[i] = pow(fact[i], MOD-2, MOD)

# Function to calculate binomial coefficient
def choose(n, k):
    if k<0 or k>n:
        return 0
    return fact[n]*ifact[k]*ifact[n-k]%MOD

# Initialize dp table
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1

# Calculate dp table
for i in range(N+1):
    for j in range(M+1):
        for a in range(i+1):
            for b in range(j+1):
                if a*b < i*j:
                    continue
                ways = choose(i*j, a*b)*dp[a][b]%MOD
                ways *= choose((N-i)*(M-j), (i-a)*(j-b))%MOD
                ways *= fact[i]*fact[j]*fact[N-i]*fact[M-j]%MOD
                dp[i][j] += ways
                dp[i][j] %= MOD

print(dp[N][M])

