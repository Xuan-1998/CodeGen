def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[0] * (s+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            if i == 1:
                for j in range(s+1):
                    dp[i][j] = a[0] * max(0, s-j)
            else:
                for j in range(max(0, s-a[i]), min(s+1, 2*10**5)):
                    dp[i][j] = min(dp[i-1][k] + (a[i]-j)*max(0, s-k) for k in range(j+a[0], j+a[0]+s))

        print(min(dp[n]))

if __name__ == "__main__":
    solve()
