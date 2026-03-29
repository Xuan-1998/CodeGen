import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, n) + 1):
            if p[2*i-1] + p[2*i] <= p[2*j-1] + p[2*j]:
                dp[i][j] = (dp[i-1][j-1] == 1) or (p[2*(i-1)]+p[2*(i-1)+1] > p[2*i-1]+p[2*i])
            else:
                dp[i][j] = 0
    
    print("YES" if dp[n][n] == 1 else "NO")

if __name__ == "__main__":
    solve()
