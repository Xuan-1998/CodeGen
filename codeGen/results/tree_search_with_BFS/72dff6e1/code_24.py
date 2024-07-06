MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: there's one way to have a sequence of length 0
    dp[0][0] = 1
    
    # Count occurrences of each number in the sequence
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if A[j-1] >= i:  # Check if it's possible to have 'j' in the sequence
                dp[i][j] = dp[i-1][j-1]  # Start by inheriting from dp[i-1][j-1]
                for k in range(1, N + 1):
                    if k != j and A[k-1] >= i - 1:
                        dp[i][j] += dp[i-1][k]
                        dp[i][j] %= MOD
    
    # Sum up all ways to form a sequence of length N
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


