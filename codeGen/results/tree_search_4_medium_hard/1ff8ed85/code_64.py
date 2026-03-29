t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    dp = [[False] * 2 for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(2):  # 0: all even, 1: all odd
            if j == 0 and all(x % 2 == 0 for x in b[:i]):
                dp[i][j] = True
            elif j == 1 and all(x % 2 != 0 for x in b[:i]):
                dp[i][j] = True
    
    print("YES" if any(dp[n][j]) else "NO")
