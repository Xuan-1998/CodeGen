def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[float('inf')] * (2*s + 1) for _ in range(n)]
        for i in range(1, n+1):
            for j in range(-s, s+1):
                if i == 1:
                    for x in range(max(0, a[0]-s), min(a[0], s)+1):
                        dp[i-1][j+x] = min(dp[i-1][j+x], a[0]*x + (a[0]-s-x)*x)
                else:
                    for x in range(-min(s, j+a[i-1]), max(0, s-j+a[i-1])+1):
                        dp[i-1][j+x] = min(dp[i-1][j+x], a[i-1]*x + (a[i-1]-s-x)*x) + dp[i-2][j+(a[i-1]-x)]
        print(min(dp[-1]))

if __name__ == '__main__':
    solve()
