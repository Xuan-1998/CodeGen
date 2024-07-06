python
MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    # Initialize the dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: empty sequence
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = 0
            for k in range(1, N + 1):
                if k != j and dp[i-1][k] > 0:
                    # Check if the sequence can have j at the end
                    count_j = sum(1 for x in range(1, i+1) if x == j)
                    count_k = sum(1 for x in range(1, i+1) if x == k)
                    if count_j <= A[j-1] and count_k <= A[k-1]:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Calculate the result
    result = sum(dp[N][j] for j in range(1, N + 1)) % MOD
    print(result)


