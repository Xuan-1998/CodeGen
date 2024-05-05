t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = [[False for _ in range(2)] for _ in range(n + 1)]
    dp[0][0] = True
    
    min_diff = float('inf')
    for i in range(1, n):
        if b[i - 1] % 2 == 0:
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][1]
        else:
            for k in range(i):
                if (dp[k][0] and not dp[i][0]) or (not dp[k][0] and dp[i][0]):
                    dp[i][0] = True
                elif (dp[k][1] and not dp[i][1]) or (not dp[k][1] and dp[i][1]):
                    dp[i][1] = True
        
        if dp[i][0]:
            min_diff = min(min_diff, b[i] - b[0])
        if dp[i][1]:
            min_diff = min(min_diff, b[n - 1] - b[i])
    
    print('YES' if min_diff <= b[-1] else 'NO')
