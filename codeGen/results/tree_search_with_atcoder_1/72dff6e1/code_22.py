python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Fill dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i-1][k-1] > 0 and A[j-1] > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][k-1]) % MOD
    
    # Calculate the final answer
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


