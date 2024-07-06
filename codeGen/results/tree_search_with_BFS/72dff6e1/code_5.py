python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))

    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i-1][k] > 0:
                    count_j = sum(1 for x in range(1, i) if dp[x][j] > 0)
                    count_k = sum(1 for x in range(1, i) if dp[x][k] > 0)
                    if count_j < A[j-1] and count_k < A[k-1]:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


