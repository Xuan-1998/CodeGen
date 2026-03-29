def solve(t):
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[0] * (n + 1) for _ in range(2)]
        
        for i in range(n - 1):
            left_sum = sum(a[:i+1])
            right_sum = sum(a[i:])
            
            dp[0][i+1] = min(dp[0][i], a[i] * min(s, n-i-s) + left_sum)
            dp[1][i+1] = min(dp[1][i], a[n-1-i] * min(s, i-s) + right_sum)
        
        print(min(dp[0][-1], dp[1][-1]))

t = int(input())
solve(t)
