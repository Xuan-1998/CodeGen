===BEGIN CODE===
def solve():
    n = int(input())
    p = list(map(int, input().split()))
    ranges = []
    for i in range(1, n):
        l, r = map(int, input().split())
        ranges.append((l, r))
    
    dp = [[float('inf')] * 1000000 for _ in range(n)]
    dp[0][0] = 0
    
    for i in range(1, n):
        l, r = ranges[i-1]
        for j in range(max(l, dp[i-1][min(r, l)]), min(r+1, len(dp[i])) + 1):
            if dp[i-1][j] != float('inf'):
                dp[i][j] = dp[i-1][j]
    
    print(min(dp[-1]))

solve()
===END CODE===
