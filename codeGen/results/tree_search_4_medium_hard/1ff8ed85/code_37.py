import sys

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        state_dict = {}
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(i + 1):
                if not dp[j][i]:
                    continue
                
                for k in range(j, i):
                    if b[k] == i - j:
                        dp[i][k+1] = True
                        break
        
        print("YES" if any(dp[n][i] for i in range(n + 1)) else "NO")

solve()
