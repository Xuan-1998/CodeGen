def process_query(signs, l, r):
    n = len(signs)
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][i] = 0
    
    for length in range(2, n+1):
        for i in range(1, n-length+2):
            j = i + length - 1
            if signs[i-1] == signs[j]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1)
            else:
                dp[i][j] = min(dp[i-1][j-1], 2)
    
    return dp[0][r-l+1]

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    signs = list(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(process_query(signs, l-1, r-1))
