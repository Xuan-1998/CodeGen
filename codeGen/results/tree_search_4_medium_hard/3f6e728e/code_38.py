import sys

MOD = 10**9 + 7

def solve():
    N, M, C = map(int, input().split())
    upper_hemispheres = list(map(int, input().split()))
    lower_hemispheres = list(map(int, input().split()))

    dp = [[0] * (M+1) for _ in range(C+1)]
    
    for c in range(1, C+1):
        dp[c][0] = 1
    for i in range(1, C+1):
        for j in range(max(0, N-M), min(N,M)+1):
            if (i == 1) and (j > 0):
                dp[i][j] = 0
            else:
                for k in range(min(i,C)+1):
                    if i-k <= C:
                        dp[i][j] += dp[max(0, i-k)][min(j, M+k)]
    for c in range(C+1):
        print(sum(dp[c][j] for j in range(N)) % MOD)

if __name__ == "__main__":
    solve()
