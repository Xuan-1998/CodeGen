python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Step 1: Validate input
    assert 2 <= N <= 500
    assert len(d) == N
    assert sum(d) == N - 1
    assert d[0] >= 1
    
    # Step 2: Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Step 3: Populate DP table
    for i in range(1, N):
        for j in range(N + 1):
            if dp[i-1][j] > 0:
                for k in range(0, d[i] + 1):
                    if j + k <= N:
                        dp[i][j + k] = (dp[i][j + k] + dp[i-1][j]) % MOD
    
    # Step 4: Calculate the result
    result = 0
    for i in range(N + 1):
        result = (result + dp[N-1][i]) % MOD
    
    print(result)

if __name__ == "__main__":
    main()

