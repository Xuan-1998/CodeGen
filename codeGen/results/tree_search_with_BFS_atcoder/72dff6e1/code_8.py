MOD = 998244353

def solve(N, A):
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        dp_new = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
        for j in range(i+1):
            for k in range(j+1):
                # add a new element
                dp_new[j+1][k+1] += dp[j][k] * (N-j)
                dp_new[j+1][k+1] %= MOD
                # add an element that has appeared exactly once before
                if k > 0:
                    dp_new[j][k-1] += dp[j][k] * k
                    dp_new[j][k-1] %= MOD
                # add an element that has appeared more than once before
                if j > k:
                    dp_new[j][k] += dp[j][k] * (j-k)
                    dp_new[j][k] %= MOD
        dp = dp_new
    return sum(sum(dp[j][k] for k in range(j+1)) for j in range(N+1)) % MOD

N = int(input().strip())
A = list(map(int, input().strip().split()))
print(solve(N, A))

