MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Adjust A to be 1-indexed for convenience
    A = [0] + A
    
    # Initialize dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: sequences of length 1
    for j in range(1, N + 1):
        dp[1][j] = 1
    
    # Fill the dp table
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i - 1][k] > 0 and dp[i - 1][k] <= A[k]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Calculate the final answer
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    print(result)


