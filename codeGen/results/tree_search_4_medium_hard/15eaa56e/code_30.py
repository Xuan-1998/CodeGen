import sys

def solve():
    n, m = map(int, input().split())
    dp = [[False] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        row = list(map(int, input().split()))
        for j in range(1, m+1):
            if not dp[i][j-1]:
                break
            for k in range(j-1, -1, -1):
                if row[k] < row[k-1]:
                    break
            else:
                dp[i][j] = True
    
    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        print("Yes" if dp[r][m] else "No")

if __name__ == "__main__":
    solve()
