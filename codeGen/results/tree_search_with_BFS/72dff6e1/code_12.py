def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    # Step 1: Initialize dp array
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Step 2: Base case
    for j in range(1, N + 1):
        dp[0][j] = 1
    
    # Step 3: Fill dp table
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if k <= A[k-1] and j <= A[j-1]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Step 4: Sum the results for sequences of length N
    result = 0
    for j in range(1, N + 1):
        result = (result + dp[N][j]) % MOD
    
    # Step 5: Print the result
    print(result)


