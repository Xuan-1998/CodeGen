import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        dp = [[False] * 2 for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(n+1):
            for p in range(2):
                if not dp[i-1][p]:
                    dp[i][p] = False
                else:
                    for k in range(min(i, n)+1):
                        if (dp[k][1-p] and b[i-k]%2 == p) or (dp[k][p] and b[i-k]%2 != p):
                            dp[i][p] = True
                            break
        
        print("YES" if any(dp[n]) else "NO")

solve()
