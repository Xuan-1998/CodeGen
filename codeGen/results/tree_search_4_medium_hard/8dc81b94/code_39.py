def can_become_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * 2 for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in [0, 1]:
            if j == 0:
                dp[i][j] = (dp[i - 1][0] and arr[i - 1] > 0) or (arr[i - 1] == 0 and dp[i - 1][1])
            else:
                dp[i][j] = dp[i - 1][0]
    
    if dp[n][0]:
        print("YES")
    else:
        print("NO")

can_become_zero()
