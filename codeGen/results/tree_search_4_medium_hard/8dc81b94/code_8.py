from sys import stdin

def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    
    dp = [[False] * (n-1) for _ in range(n)]
    dp[0][n-1] = True
    
    for i in range(n):
        for j in range(n-1):
            if i == 0:
                dp[i][j] = a[j] - 1 <= n-1 and dp[i][j]
            elif j == n-2:
                dp[i][j] = a[j+1] - 1 >= i and dp[min(n-1, j+1)][j]
            else:
                dp[i][j] = (a[j] - 1 <= n-1 and dp[i-1][max(0, j-1)]) or \
                           (a[j+1] - 1 >= i and dp[min(n-1, j+1)][j])
    
    print("YES" if dp[0][n-2] else "NO")

if __name__ == "__main__":
    solve()
