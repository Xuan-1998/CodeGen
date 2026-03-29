import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            for x in range(max(0, s - a[i]), min(a[i], s + 1)):
                y = a[i] - x
                if (x - s) * (y - s) >= 0:
                    dp[i + 1] = min(dp[i + 1], dp[i] + x * a[i])
        
        print(min(dp))

solve()
