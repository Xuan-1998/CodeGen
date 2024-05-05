def solve():
    n, q = map(int, input().split())
    signs = list(input())
    dp = [0] * (n + 1)
    
    for i in range(n):
        if signs[i] == "+":
            dp[i + 1] += 1
        else:
            dp[i + 1] -= 1
    
    for _ in range(q):
        l, r = map(int, input().split())
        net_signs = dp[l - 1] - dp[r]
        ans = min(dp[l - 1], abs(net_signs) + dp[r])
        print(ans)

solve()
