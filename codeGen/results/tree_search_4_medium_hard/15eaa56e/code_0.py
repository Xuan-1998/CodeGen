import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    dp = [[False] * m for _ in range(n)]
    
    for i in range(n):
        row = list(map(int, input().split()))
        
        for j in range(1, m):
            if row[j-1] > row[j]:
                for k in range(j):
                    if not dp[i-1][k]:
                        dp[i][j] = True
                        break
                else:
                    dp[i][j] = False
                    break
    
    ans = "No"
    for i in range(n):
        for j in range(m):
            if dp[i][j]:
                ans = "Yes"
                break
        if ans == "Yes":
            break
    
    print(ans)

solve()
