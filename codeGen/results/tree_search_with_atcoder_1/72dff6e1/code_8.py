python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    
    # Base case
    for j in range(1, N+1):
        if A[j-1] >= 1:
            dp[1][j][1] = 1
    
    # Fill DP table
    for i in range(2, N+1):
        for j in range(1, N+1):
            for k in range(1, A[j-1]+1):
                for p in range(1, N+1):
                    if k == 1:
                        for q in range(1, A[p-1]+1):
                            dp[i][j][k] = (dp[i][j][k] + dp[i-1][p][q]) % MOD
                    elif j == p:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
    
    # Sum up all valid sequences of length N
    result = 0
    for j in range(1, N+1):
        for k in range(1, A[j-1]+1):
            result = (result + dp[N][j][k]) % MOD
    
    print(result)

if __name__ == "__main__":
    solve()

