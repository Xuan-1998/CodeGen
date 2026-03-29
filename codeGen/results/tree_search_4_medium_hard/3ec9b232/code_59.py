def solve():
    n = int(input())
    M = list(map(int, input().split()))
    
    # Initialize dp array
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: dp[0][i] = 1 for all i
    for i in range(n + 1):
        dp[0][i] = 1
    
    # Calculate dp[i][j]
    for i in range(1, n + 1):
        for j in range(i + 1):
            if M[j - 1] == i:
                for p in range(i + 1):
                    dp[i][j] += dp[i - 1][p]
    
    # Calculate the final answer
    ans = sum(dp[n][i] for i in range(n + 1))
    
    print(ans % (10**9 + 7))

solve()
