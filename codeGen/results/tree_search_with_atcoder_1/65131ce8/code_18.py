python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    d = list(map(int, data[1:]))
    
    MOD = 998244353
    
    # Step 1: Initialize the dp table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Step 2: Base case
    dp[1][1] = 1
    
    # Step 3: Transition
    for i in range(2, N + 1):
        for j in range(1, i + 1):
            for k in range(1, i):
                if i - k >= 1:
                    dp[i][j] = (dp[i][j] + dp[k][j - 1] * dp[i - k][1]) % MOD
    
    # Step 4: Sum the results
    result = 0
    for i in range(1, N + 1):
        result = (result + dp[N][i]) % MOD
    
    # Step 5: Print the result
    print(result)


