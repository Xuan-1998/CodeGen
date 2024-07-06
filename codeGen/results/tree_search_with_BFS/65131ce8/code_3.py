python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Iterate over each node
    for i in range(1, N + 1):
        for j in range(N, 0, -1):
            for k in range(i):
                if j >= d[i-1]:
                    dp[j][d[i-1]] = (dp[j][d[i-1]] + dp[j-1][k]) % MOD

    # Calculate the result
    result = sum(dp[N]) % MOD
    print(result)


