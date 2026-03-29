def solve():
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(10)]
    
    for i in range(10):
        dp[i][0] = 1
    
    for len_ in range(1, n + 1):
        for i in range(10):
            if len_ == 1:
                dp[i][len_] = 1
            else:
                if i == 0:
                    dp[i][len_] = (dp[9][len_ - 1] * len_) % 998244353
                elif i > 0 and i < 10:
                    dp[i][len_] = ((dp[i - 1][len_ - 1] + dp[i][len_ - 1]) * len_) % 998244353
    
    count = [0] * (n + 1)
    
    for i in range(10):
        count[len(count) - 1] += dp[i][n]
    
    print(*count, sep=' ')

solve()
