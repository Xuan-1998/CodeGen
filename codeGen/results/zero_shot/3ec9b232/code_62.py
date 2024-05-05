def solve():
    n = int(input())
    m = list(map(int, input().split()))
    
    # Sort the array
    m.sort()
    
    dp = [[0]*n for _ in range(n+1)]
    
    # Base case: when k is equal to 0, there is only one way to partition the numbers
    for i in range(n):
        dp[0][i] = 1
    
    # Transition rule
    for k in range(1, n+1):
        for i in range(k-1, -1, -1):
            if m[i] == i + 1:
                break
            else:
                dp[k][i] += (k-1)*dp[0][m[i-1]] - dp[k-1][m[i-1]]
    
    # The answer is stored in dp[n][n]
    print(dp[n][n]%10**9+7)

solve()
