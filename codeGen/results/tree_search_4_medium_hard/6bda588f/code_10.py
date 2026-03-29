from sys import stdin

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, s = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        
        dp = [[0] * (2*s+1) for _ in range(n-1)]
        
        for i in range(1, n-1):
            for k in range(2*s+1):
                if k - (a[i] - s) >= 0:
                    dp[i][k] = min(dp[i-1][k-(a[i]-s)] + a[i]*min(k, a[i]-s), k)
        
        print(min(dp[-1]))

if __name__ == "__main__":
    solve()
