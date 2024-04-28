def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    dp = [[0] * (n + 1) for _ in range(2)]
    
    for i in range(1, n + 1):
        if i == 1:
            dp[1][i] = 0
        elif a[i - 1] % 2 == 1:
            dp[1][i] = max(dp[1][i - 1], a[i - 1])
        else:
            dp[1][i] = dp[1][i - 1]
    
    print(max(dp[0]))
